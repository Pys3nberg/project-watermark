from PyQt4 import QtGui, uic
from PIL import Image, ImageQt
import sys

class MainGUI(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        uic.loadUi('BaseGUI.ui', self)
        self.setLabel()
        self.show()

    def setLabel(self):

        im = Image.open('Penguins.jpg')
        im = im.convert('RGBA')
        im = im.tobytes('raw','RGBA')
        image = QtGui.QImage.fromData(im)
        image = QtGui.QPixmap(image)
        print(type(image))
        self.picLabel.setPixmap(image)


    def pil_Image_to_QPixmap(self, im):

        im = ImageQt.ImageQt(im)
        im = QtGui.QImage(im)
        im = QtGui.QPixmap.fromImage(im)
        return im

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MainGUI()
    sys.exit(app.exec_())