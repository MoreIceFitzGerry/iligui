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
        self.Button_Modelselect
        self.Button_Play
        self.Terminal
        self.Terminal.setReadOnly(True)

        self.Icon_Interlis
        self.Tool_Select
        self.Setting01
        self.progressBar

        # Define our Connections
        self.Button_Fileselect.clicked.connect(self.fileselect)
        self.Button_Modelselect.clicked.connect(self.modelselect)
        self.Button_Play.clicked.connect(self.playselect)
        self.Icon_Interlis.clicked.connect(self.interlisselect)
        self.Tool_Select.activated.connect(self.toolselect)
        self.Setting01.clicked.connect(self.setting01select)

        # Show the App
        self.show()

    def fileselect(self):
        # Open a file dialog and allow the user to select a file
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis-1 Files (*.itf);;Interlis-2 Files (*.xtf);;XML Files (*.xml)")
    def modelselect(self):
        # Open a file dialog and allow the user to select a file
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")

    def playselect(self):
        import logic_playbutton
        # Use subprocess method to run the Jar file with the selected input options
        #file_path = "tests\RoadsSimple.xml"
        logic_playbutton.checkinstall_cwdjava()
        textoutput = logic_playbutton.run_ilivalidator(self.file_path)
        self.Terminal.appendPlainText(textoutput)

    def interlisselect(self):
        import webbrowser
        # TODO: Check for validity of URL
        webbrowser.open("https://github.com/claeis/ilivalidator/blob/master/docs/ilivalidator.rst")

    def toolselect(self):
        # Open a file dialog and allow the user to select a file
        file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis-1 Files (*.itf);;Interlis-2 Files (*.xtf)")

    def setting01select(self):
        # Open a file dialog and allow the user to select a file
        file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis-1 Files (*.itf);;Interlis-2 Files (*.xtf)")


# Initialize the App
app = QApplication(sys.argv)
UIWindow = iligui()
app.exec_()