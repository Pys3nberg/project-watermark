# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaseGUI.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 511)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.inputFileList = QtGui.QListWidget(self.centralwidget)
        self.inputFileList.setGeometry(QtCore.QRect(10, 10, 171, 421))
        self.inputFileList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.inputFileList.setIconSize(QtCore.QSize(24, 32))
        self.inputFileList.setObjectName(_fromUtf8("inputFileList"))
        self.addImagesButton = QtGui.QPushButton(self.centralwidget)
        self.addImagesButton.setGeometry(QtCore.QRect(10, 440, 75, 23))
        self.addImagesButton.setObjectName(_fromUtf8("addImagesButton"))
        self.removeImagesButton = QtGui.QPushButton(self.centralwidget)
        self.removeImagesButton.setGeometry(QtCore.QRect(100, 440, 75, 23))
        self.removeImagesButton.setObjectName(_fromUtf8("removeImagesButton"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 10, 481, 421))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 200, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.addImagesButton.setText(_translate("MainWindow", "Add Images", None))
        self.removeImagesButton.setText(_translate("MainWindow", "Remove", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))

