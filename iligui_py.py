from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt5 import uic
import sys

class iligui(QMainWindow):
    def __init__(self):
        super(iligui, self).__init__()

        # Load UI File
        uic.loadUi("iligui_ui.ui", self)

        # Define our Widgets
        self.Button_Fileselect

        # Define our Connections
        self.Button_Fileselect.clicked.connect(self.fileselect)

        # Show the App
        self.show()

    def fileselect(self):
        # Open a file dialog and allow the user to select a file
        file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis-1 Files (*.itf);;Interlis-2 Files (*.xtf)")


# Initialize the App
app = QApplication(sys.argv)
UIWindow = iligui()
app.exec_()