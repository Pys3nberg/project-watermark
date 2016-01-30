# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_infoDialog(object):
    def setupUi(self, infoDialog):
        infoDialog.setObjectName(_fromUtf8("infoDialog"))
        infoDialog.resize(242, 402)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Images/water.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoDialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(infoDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 381))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.reasonEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.reasonEdit.setObjectName(_fromUtf8("reasonEdit"))
        self.verticalLayout.addWidget(self.reasonEdit)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.requestedEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.requestedEdit.setObjectName(_fromUtf8("requestedEdit"))
        self.verticalLayout.addWidget(self.requestedEdit)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.RecipicantEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.RecipicantEdit.setObjectName(_fromUtf8("RecipicantEdit"))
        self.verticalLayout.addWidget(self.RecipicantEdit)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.watermarkedEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.watermarkedEdit.setObjectName(_fromUtf8("watermarkedEdit"))
        self.verticalLayout.addWidget(self.watermarkedEdit)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.printedEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.printedEdit.setObjectName(_fromUtf8("printedEdit"))
        self.verticalLayout.addWidget(self.printedEdit)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.psizeEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.psizeEdit.setObjectName(_fromUtf8("psizeEdit"))
        self.verticalLayout.addWidget(self.psizeEdit)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.datesentEdit = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.datesentEdit.setCalendarPopup(True)
        self.datesentEdit.setObjectName(_fromUtf8("datesentEdit"))
        self.verticalLayout.addWidget(self.datesentEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.okButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(infoDialog)
        QtCore.QMetaObject.connectSlotsByName(infoDialog)

    def retranslateUi(self, infoDialog):
        infoDialog.setWindowTitle(_translate("infoDialog", "Additional Info", None))
        self.label.setText(_translate("infoDialog", "Reason", None))
        self.label_2.setText(_translate("infoDialog", "Requested By", None))
        self.label_3.setText(_translate("infoDialog", "Recipicant", None))
        self.label_4.setText(_translate("infoDialog", "Watermarked", None))
        self.label_5.setText(_translate("infoDialog", "Printed By", None))
        self.label_6.setText(_translate("infoDialog", "Size Paper", None))
        self.label_7.setText(_translate("infoDialog", "Date Sent", None))
        self.okButton.setText(_translate("infoDialog", "OK", None))
        self.cancelButton.setText(_translate("infoDialog", "Cancel", None))

