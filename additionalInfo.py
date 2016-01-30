from PyQt4 import QtCore, QtGui
from infoGui import Ui_infoDialog
import sys, datetime


class additional_info(QtGui.QDialog, Ui_infoDialog):

    def __init__(self):

        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
        self.datesentEdit.setDate(QtCore.QDate.currentDate())
        self.show()


    def getValues(self):

        values = {}
        values['Reason'] = self.reasonEdit.text()
        values['Requested'] = self.requestedEdit.text()
        values['Recipicant'] = self.RecipicantEdit.text()
        values['Watermarked'] = self.watermarkedEdit.text()
        values['PrintedBy'] = self.printedEdit.text()
        values['PaperSize'] = self.psizeEdit.text()
        values['DateSent'] = self.datesentEdit.text()

        return values

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    addInfo = additional_info()
    sys.exit(app.exec_())