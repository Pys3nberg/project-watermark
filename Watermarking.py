from PIL import Image, ImageEnhance, ImageDraw, ImageFont, PdfImagePlugin
from numpy import polyfit, poly1d
import os, datetime
# PdfImagePlugin only imported so that compile applications can save to pdf

def reduce_opacity(im, opacity):

    if not im.mode == 'RGBA':
        im = im.convert('RGBA')
    else:
        im=im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def watermark(im, mark, opacity=1):

    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if not im.mode == 'RGBA':
        im = im.convert('RGBA')

    layer = Image.new('RGBA', im.size, (0,0,0,0))

    # just scale it for now
    ratio = min(float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
    w = int(mark.size[0]*ratio)
    h = int(mark.size[1]*ratio)
    mark = mark.resize((w,h))
    layer.paste(mark,(int((im.size[0] - w)/2),int((im.size[1]-h)/2)))
    return Image.composite(layer, im, layer)

def gen_watermark(im, inText):

    # Initial Font size
    fntSize = 12
    # Create a new layer the size of the input image, in RGBA mode and set all components to zero
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    # Using the layer create a ImageDraw object
    draw = ImageDraw.Draw(layer)
    # Get the font size and text size of the desired input
    fntSize, tSize = get_fntSize(im, draw, inText, 'arial')
    # create a font object
    fnt = ImageFont.truetype('arial.ttf', fntSize)
    # using the image and text size, calculate the co-ords of top left point of the text rectangle, such that the text
    # will appear in the centre of the layer
    pos = ((im.size[0] - tSize[0])/2, (im.size[1] - tSize[1])/2)
    # Actually draw the text on the layer in white with 0.5 Alpha
    draw.text(pos, inText,font=fnt,fill=(225,225,225,128))
    fntSize, tSize = get_fntSize(im, draw, 'For Reference Only - Do Not distribute', 'arial', scale=0.75)
    fnt = ImageFont.truetype('arial.ttf', fntSize)
    pos = ((im.size[0] - tSize[0])/2, 50)
    draw.text(pos, 'For Reference Only - Do Not distribute',font=fnt,fill=(225,225,225,128))
    # Add print number in pure red
    draw.text((10,10), 'Print 001', font=ImageFont.truetype('arial.ttf', 18), fill=(225,0,0,255))
    # return a composite image, a combination of the the input image and the new layer.
    return Image.alpha_composite(im.convert('RGBA'), layer)

def watermark_full_beans(im, fileName, printNo = '000', top=None, cent=None, bot=None):

    layer = Image.new('RGBA', im.size, (0,0,0,0))
    draw = ImageDraw.Draw(layer)

    draw.text((10,10), 'Print ' + printNo, font=ImageFont.truetype('arial.ttf', 18), fill=(225,0,0,255))


    if top:
        if top[2] == 0:
            fntSize, tSize = get_fntSize_poly(im, draw, top[0], top[1])
            fnt = ImageFont.truetype(top[1]+'.ttf', fntSize)
        else:
            fnt = ImageFont.truetype(top[1]+'.ttf', top[2])
            tSize = draw.textsize(top[0], ImageFont.truetype(top[1]+'.ttf', top[2]))
        pos = ((im.size[0] - tSize[0])/2, 50)
        draw.text(pos, top[0],font=fnt,fill=(225,225,225,int(top[3]*255)))

    if cent:
        if cent[2] == 0:
            fntSize, tSize = get_fntSize_poly(im, draw, cent[0], cent[1])
            fnt = ImageFont.truetype(cent[1]+'.ttf', fntSize)
        else:
            fnt = ImageFont.truetype(cent[1]+'.ttf', cent[2])
            tSize = draw.textsize(cent[0], ImageFont.truetype(cent[1]+'.ttf', cent[2]))
        pos = ((im.size[0] - tSize[0])/2, (im.size[1] - tSize[1])/2)
        draw.text(pos, cent[0],font=fnt,fill=(225,225,225,int(cent[3]*255)))

    if not bot:
        bot = [datetime.datetime.now().strftime('%d/%m/%Y'), 'arial', 50,128]

    if bot[2] == 0:
        fntSize, tSize = get_fntSize_poly(im, draw, bot[0], bot[1])
        fnt = ImageFont.truetype(bot[1]+'.ttf', fntSize)
    else:
        fnt = ImageFont.truetype(bot[1]+'.ttf', bot[2])
        tSize = draw.textsize(bot[0], ImageFont.truetype(bot[1]+'.ttf', bot[2]))


    pos = ((im.size[0]/2 - tSize[0]/2), (im.size[1] - tSize[1])-50)
    draw.text(pos, bot[0],font=fnt,fill=(225,225,225,bot[3]))


    return Image.alpha_composite(im.convert('RGBA'), layer)


def get_fntSize(im, drawObj, text, fntName, scale=1):

    """in this function we get the text size in pixels using the current fontsize, the widths of the text and the image
    are compared, if the text fits inside the image, increase the font size until the text does not fit. At that
    point set the font size one step down. (Note that scale can be used to determin what teh fontsize must be to
    roughly fit in the scaled im size, default=1)"""

    # Start with a fntsize of 10
    fntSize = 10
    while True:
        tSize = drawObj.textsize(text, ImageFont.truetype(fntName+'.ttf', fntSize))
        if tSize[0] < im.size[0]*scale:
            fntSize += 10
        else:
            fnt = ImageFont.truetype('arial.ttf', fntSize-10)
            break
    # return the final fontsize and the size of the text
    return fntSize-10, drawObj.textsize(text, ImageFont.truetype(fntName+'.ttf', fntSize-10))


def get_fntSize_poly(im, drawObj, text, fntName, scale=1):

    """
    This function is an evolution of the get_fntSize which was proving to take some time in some cases. Instead of
    looping for a undefined amount of time, we use 5 test point to fit a quadratic curve (relationship is roughly of
    2nd order). Then finally we get the font size needed to fit the width of the image.
    """

    # List of test font sizes
    fntSizeList = [12 ,25, 50, 75, 100]
    textSizes = []

    # Loop through sizes and get the text size in pixels using the string
    for s in fntSizeList:
        tSize = drawObj.textsize(text, ImageFont.truetype(fntName+'.ttf', s))
        textSizes.append(tSize[0])

    # calculate polynomial using the text size in  pixels as x, and font size as y
    z = polyfit(textSizes,fntSizeList, 2)
    f = poly1d(z)

    # Calculate the font size needed to get the desired text size
    fntSize = int(f((im.size[0] - 50)*scale))

    return fntSize, drawObj.textsize(text, ImageFont.truetype(fntName+'.ttf', fntSize))


def saveImage(im=None, savePath = None):
    if savePath and im:
        im.convert("RGB").save(savePath, "PDF", resolution=50.0)


def main():


    # im = Image.open('Lighthouse.jpg')
    # im = watermark_full_beans(im, '11', printNo = '000', top=['For Reference Only - Do Not distribute',
    #                                                           'arial', 0, 0.5],
    #                           cent=['Eren Ramadan', 'arial', 0, 0.5])
    # im.show()
    saveImage(savePath='hello.pdf')

if __name__ == '__main__':

    main()