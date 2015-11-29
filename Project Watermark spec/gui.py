__author__ = 'Pysenberg'

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):


        #init window class from inherited class, set the size, set the title and set the window icon
        QtGui.QMainWindow.__init__(self)
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('PyQt Tuts')
        self.setWindowIcon(QtGui.QIcon('1445659698_rocket.png'))
        #enable the status bar
        self.statusBar()
        #create the action with an icon and call it urbek, bind its triggered event to the close_application method,
        #set its shortcut to Ctrl+Q
        testAction = QtGui.QAction(QtGui.QIcon('Log Out.png'),'urbek',self)
        testAction.triggered.connect(self.close_application)
        testAction.setStatusTip('Leave the application')
        testAction.setShortcut('Ctrl+Q')
        #Initialise the menu bar, add a file menu and then add the testAction to the file menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(testAction)


        openEditor = QtGui.QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Ediotr')
        openEditor.triggered.connect(self.editor)

        editorMenu = mainMenu.addMenu('Editor')
        editorMenu.addAction(openEditor)

        openFile = QtGui.QAction('Open file', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('open file')
        openFile.triggered.connect(self.open_file)
        fileMenu.addAction(openFile)

        savFile = QtGui.QAction('Save File', self)
        savFile.setShortcut('Ctrl+S')
        savFile.setStatusTip('Save your file dread')
        savFile.triggered.connect(self.save_file)

        fileMenu.addAction(savFile)

        #call home method to add other stuff
        self.home()

    def home(self):

        #create a button and give it a label, then connect its clicked event to the close_application method,
        #Also size the button to the min recommended size and give is a status bar tip. finally move it to a pos
        btn = QtGui.QPushButton('Quit',self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.setStatusTip('Leave the app')
        btn.move(0, 100)
        #Create a new action, give it an icon and call it urbek, connect its triggered event to the close_application
        logout = QtGui.QAction(QtGui.QIcon('Log Out.png'), 'flee the seen', self)
        logout.triggered.connect(self.close_application)
        #Init the toolbar and give it a name, add our new action too it
        self.toolBar = self.addToolBar('logOut')
        self.toolBar.addAction(logout)


        fontChoice = QtGui.QAction('font', self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar('font')
        self.toolBar.addAction(fontChoice)

        color = QtGui.QColor(0,0,0)
        fontcolor = QtGui.QAction('Font colour bg', self)
        fontcolor.triggered.connect(self.color_pick)
        self.toolBar.addAction(fontcolor)



        #create a checkbox and name it, connect it state changed event to the resized method, move checkbox
        checkBox = QtGui.QCheckBox('Resize', self)
        checkBox.stateChanged.connect(self.resizedfunc)
        checkBox.move(100, 100)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btnDown = QtGui.QPushButton('Download', self)
        self.btnDown.move(200,120)
        self.btnDown.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel('Windows', self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsVista')
        comboBox.addItem('macintosh')
        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        cal = QtGui.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200,200)

        self.show()

    def close_application(self):

        #Inits a message box question, and waits for a response
        choice = QtGui.QMessageBox.question(self, 'Quittitng', 'do you really want to quit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        #if statement depending on what user chooses
        if choice == QtGui.QMessageBox.Yes:
            print('closing app')
            sys.exit()
        else: pass

    def resizedfunc(self, state):
        #if checked make the window bigger, if not reset
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50, 500,300)

    def download(self):

        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def style_choice(self, text):

        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def font_choice(self):

        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def color_pick(self):

        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget {background-color: %s}" % color.name())

    def editor(self):
        self.textEd = QtGui.QTextEdit()
        self.setCentralWidget(self.textEd)

    def open_file(self):

        name = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        file = open(name, 'r')
        self.editor()

        with file:
            text = file.read()
            self.textEd.setText(text)

    def save_file(self):

        name = QtGui.QFileDialog.getSaveFileName(self, 'save file')
        with open(name, 'w') as file:
            file.write(self.textEd.toPlainText())

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()