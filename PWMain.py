from PyQt4 import QtGui, QtCore
from BaseGUI import Ui_MainWindow
from PIL import Image, ImageQt
import Watermarking as wm
import xlhelper as xl
import sys, os


class MainGUI(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):

        # ---SETUP GUI---

        # Inherit from the form class "QMainWindow"
        QtGui.QMainWindow.__init__(self)
        # Setup the GUI using the base class. ***BaseGUI must be updated using UiUpdate.bat Whenever any changes are
        # made in PyQt Designer***
        self.setupUi(self)
        # Set the style of the GUI
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('CleanLooks'))

        # ---CONNECT/SETUP IMAGE LOADING CONTROLS---

        self.addImagesButton.clicked.connect(self.addItemsToList)
        self.removeImagesButton.clicked.connect(self.removeItemsFromList)
        self.inputFileList.itemClicked.connect(self.updatePicture)
        self.inputFileList.currentItemChanged.connect(self.updatePicture)
        self.multiCheckBox.toggled.connect(self.multiCheckBoxChecked)

        # ---CONNECT/SETUP WATERMARK EDITING CONTROLS---

        self.topLineEdit.editingFinished.connect(self.updatePicture)
        self.centLineEdit.editingFinished.connect(self.updatePicture)
        self.botLineEdit.editingFinished.connect(self.updatePicture)
        self.topFitToCheckBox.stateChanged.connect(self.updatePicture)
        self.centFitToCheckBox.stateChanged.connect(self.updatePicture)
        self.botFitToCheckBox.stateChanged.connect(self.updatePicture)
        self.topOpacitySpinBox.valueChanged.connect(self.updatePicture)
        self.centOpacitySpinBox.valueChanged.connect(self.updatePicture)
        self.botOpacitySpinBox.valueChanged.connect(self.updatePicture)
        self.exportButton.clicked.connect(self.exportImages)
        self.progressBar.setValue(0)

        # ---CONNECT/SETUP IMAGE OUTPUT CONTROLS---

        self.destinationDirLineEdit.setText(os.path.dirname(os.path.realpath(os.getcwd())))
        self.destinationDirLineEdit.setToolTip(os.path.dirname(os.path.realpath(os.getcwd())))
        self.destinationDirSelectButton.clicked.connect(self.changeDestinationDir)

        # ---SETUP GRAPHICSVIEW AND SHOW GUI---

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

    def updatePicture(self):

        if self.inputFileList.currentRow()>=0:
            self.graphicsScene.clear()
            im = Image.open(self.inputFileList.item(self.inputFileList.currentRow()).toolTip())
            #im = wm.gen_watermark(im, 'Done it')

            if self.topLineEdit.text():
                if self.topFitToCheckBox.isChecked():
                    fntSize = 0
                else:
                    fntSize = 50
                topText = [self.topLineEdit.text(), 'arial', fntSize, self.topOpacitySpinBox.value()]
            else:
                topText=None

            if self.centLineEdit.text():
                if self.centFitToCheckBox.isChecked():
                    fntSize = 0
                else:
                    fntSize = 50
                centText = [self.centLineEdit.text(), 'arial', fntSize, self.centOpacitySpinBox.value()]
            else:
                centText=None

            im = wm.watermark_full_beans(im, '11', printNo = '000', top=topText, cent=centText)
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
            for i in range(self.outputFileList.count()):
                self.outputFileList.item(i).setToolTip(os.path.join(newDir, self.outputFileList.item(i).text()))

    def selectFont(self):

        font = QtGui.QFontDialog.getFont()
        font = font[0]
        print(font.style())

    def exportImages(self):

        try:
            wb = xl.workbook(os.path.join(os.getcwd(), 'Log.xlsx'))
            self.progressBar.setMaximum(self.inputFileList.count())

            for i in range(self.inputFileList.count()):
                im = Image.open(self.inputFileList.item(i).toolTip())
                #im = wm.gen_watermark(im, 'Done it')

                if self.topLineEdit.text():
                    if self.topFitToCheckBox.isChecked():
                        fntSize = 0
                    else:
                        fntSize = 50
                    topText = [self.topLineEdit.text(), 'arial', fntSize, self.topOpacitySpinBox.value()]
                else:
                    topText=None

                if self.centLineEdit.text():
                    if self.centFitToCheckBox.isChecked():
                        fntSize = 0
                    else:
                        fntSize = 50
                    centText = [self.centLineEdit.text(), 'arial', fntSize, self.centOpacitySpinBox.value()]
                else:
                    centText=None

                im = wm.watermark_full_beans(im, '11', printNo = '000', top=topText, cent=centText)
                wm.saveImage(im=im, savePath=self.outputFileList.item(i).toolTip())
                xl.append_row(wb,[1,2,3,4,5,6,7,8,9,0])
                self.progressBar.setValue(i+1)

            wb.save(os.path.join(os.getcwd(), 'Log.xlsx'))
            self.showMessage('Export of images successful!', 'All images were succesfully exported to the desination folder!',
                             QtGui.QMessageBox.Information)
            self.progressBar.setValue(0)

        except Exception as e:

            self.showMessage('Error',e,QtGui.QMessageBox.Information)


    def showMessage(self, title, text, icon):

        msg = QtGui.QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtGui.QMessageBox.Ok)

        result = msg.exec_()
        print(result)


    def closeEvent(self, *args, **kwargs):
        exit()


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MainGUI()
    sys.exit(app.exec_())