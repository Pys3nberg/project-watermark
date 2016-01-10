from PyQt4 import QtGui, QtCore
from BaseGUI import Ui_MainWindow
from PIL import Image, ImageQt
import Watermarking as wm
import sys, os


class MainGUI(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('CleanLooks'))
        self.addImagesButton.clicked.connect(self.addItemsToList)
        self.removeImagesButton.clicked.connect(self.removeItemsFromList)
        self.inputFileList.itemClicked.connect(self.updatePicture2)
        self.setupGraphics()
        self.show()

    def addItemsToList(self):

        fileNames = QtGui.QFileDialog.getOpenFileNamesAndFilter(filter="Images (*.png *.jpg *.bmp *.tiff)")
        iconPath = None

        for item in fileNames[0]:

            name, exten = os.path.splitext(os.path.basename(item))
            if exten == '.jpg':
                iconPath = os.path.join('Images', 'jpgs.png')
            elif exten == '.png':
                iconPath = os.path.join('Images', 'pngs.png')
            elif exten == '.bmp':
                iconPath = os.path.join('Images', 'bmp.png')
            else:
                iconPath = os.path.join('Images', 'tiff.png')

            item = QtGui.QListWidgetItem(item)
            item.setIcon(QtGui.QIcon(iconPath))
            self.inputFileList.addItem(item)

    def removeItemsFromList(self):

        for item in self.inputFileList.selectedItems():
            self.inputFileList.takeItem(self.inputFileList.row(item))

    def setupGraphics(self):
        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.graphicsScene)

        self.graphicsScene.clear()
        pix = QtGui.QPixmap('Penguins.jpg')
        imSize = pix.size()
        pixMap = QtGui.QGraphicsPixmapItem(pix)
        self.graphicsScene.addItem(pixMap)
        self.graphicsView.fitInView(QtCore.QRectF(0,0,imSize.width(), imSize.width()), QtCore.Qt.KeepAspectRatio)
        self.graphicsScene.update()

    def updatePicture(self, item):

        self.graphicsScene.clear()
        pix = QtGui.QPixmap(item.text())
        imSize = pix.size()
        pixMap = QtGui.QGraphicsPixmapItem(pix)
        self.graphicsScene.addItem(pixMap)
        self.graphicsView.fitInView(QtCore.QRectF(0,0,imSize.width(), imSize.width()), QtCore.Qt.KeepAspectRatio)

        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(50)

        self.graphicsScene.addText('sample text', font)
        self.graphicsScene.update()

    def updatePicture2(self, item):

        self.graphicsScene.clear()
        im = Image.open(item.text())
        im = wm.gen_watermark(im, 'Done it')
        qtim = ImageQt.ImageQt(im)
        qtim2 = qtim.copy()
        pix = QtGui.QPixmap.fromImage(qtim2)
        self.graphicsScene.addPixmap(pix)
        self.graphicsView.fitInView(QtCore.QRectF(0,0,im.size[0], im.size[1]), QtCore.Qt.KeepAspectRatio)
        self.graphicsScene.update()



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MainGUI()
    sys.exit(app.exec_())