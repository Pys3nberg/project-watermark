from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import os

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

def gen_watermark(im):

    layer = Image.new('RGBA', im.size, (0,0,0,0))
    draw = ImageDraw.Draw(layer)
    fnt = ImageFont.truetype('arial.ttf', 50)
    draw.text((0,0), "Sample text",font=fnt,fill=(225,225,225,128))
    #layer.show()
    return Image.alpha_composite(im.convert('RGBA'), layer)

def main():

    im = Image.open('Jellyfish.jpg')
    mark = Image.open(os.path.join('Project Watermark spec', 'Watermark Eren Ramadan.jpg'))
    final = gen_watermark(im)
    #final = watermark(im, mark, 0.4)

    final.show()
    final.save('hello.jpg')


if __name__ == '__main__':

    main()