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
        self.inputFileList.itemClicked.connect(self.updatePicture)
        self.inputFileList.currentItemChanged.connect(self.updatePicture)
        self.multiCheckBox.toggled.connect(self.multiCheckBoxChecked)

        self.destinationDirLineEdit.setText(os.path.dirname(os.path.realpath(__file__)))
        self.destinationDirLineEdit.setToolTip(os.path.dirname(os.path.realpath(__file__)))
        self.destinationDirSelectButton.clicked.connect(self.changeDestinationDir)

        self.setupGraphics()
        self.show()

    def setupGraphics(self):

        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsScene.clear()

    def addItemsToList(self):

        fileNames = QtGui.QFileDialog.getOpenFileNamesAndFilter(filter="Images (*.png *.jpg *.bmp *.tiff)")
        iconPath = None

        for file in fileNames[0]:

            name, exten = os.path.splitext(os.path.basename(file))
            if exten == '.jpg':
                iconPath = os.path.join('Images', 'jpgs.png')
            elif exten == '.png':
                iconPath = os.path.join('Images', 'pngs.png')
            elif exten == '.bmp':
                iconPath = os.path.join('Images', 'bmp.png')
            else:
                iconPath = os.path.join('Images', 'tiff.png')

            itemIn = QtGui.QListWidgetItem(name+exten)
            itemIn.setToolTip(file)
            itemIn.setIcon(QtGui.QIcon(iconPath))
            self.inputFileList.addItem(itemIn)

            #needs work here to add details of the file in the name
            itemOut = QtGui.QListWidgetItem(name+'.pdf')
            itemOut.setToolTip(os.path.join(self.destinationDirLineEdit.text(), name + '.pdf'))
            itemOut.setIcon(QtGui.QIcon(os.path.join('Images', 'pdfs.png')))
            self.outputFileList.addItem(itemOut)

    def removeItemsFromList(self):

        for item in self.inputFileList.selectedItems():
            row = self.inputFileList.row(item)
            self.inputFileList.takeItem(row)
            self.outputFileList.takeItem(row)

    def updatePicture(self, item):

        if item:
            self.graphicsScene.clear()
            im = Image.open(item.toolTip())
            im = wm.gen_watermark(im, 'Done it')
            qtim = ImageQt.ImageQt(im)
            qtim2 = qtim.copy()
            pix = QtGui.QPixmap.fromImage(qtim2)
            self.graphicsScene.addPixmap(pix)
            self.graphicsView.fitInView(QtCore.QRectF(0,0,im.size[0], im.size[1]), QtCore.Qt.KeepAspectRatio)
            self.graphicsScene.update()
        else:
            self.graphicsScene.clear()

    def multiCheckBoxChecked(self, state):

        selectionMode = None

        if state:
            selectionMode = QtGui.QAbstractItemView.MultiSelection
        else:
            selectionMode = QtGui.QAbstractItemView.SingleSelection

        self.inputFileList.setSelectionMode(selectionMode)

    def changeDestinationDir(self):

        newDir = str(QtGui.QFileDialog.getExistingDirectory(
                caption='Select a new output directory'))

        if newDir:
            self.destinationDirLineEdit.setText(newDir)
            self.destinationDirLineEdit.setToolTip(newDir)

    def closeEvent(self, *args, **kwargs):
        exit()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MainGUI()
    sys.exit(app.exec_())