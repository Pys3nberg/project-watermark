from PIL import Image, ImageQt
from PyQt4 import QtGui, QtCore

PilImage = Image.open('Penguins.jpg')
QtImage1 = ImageQt.ImageQt(PilImage)
QtImage2 = QtGui.QImage(QtImage1)
pixmap = QtGui.QPixmap.fromImage(QtImage2)