from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6 import uic
import sys

class iligui(QMainWindow):
    def __init__(self):
        super(iligui, self).__init__()

        # Load UI File
        uic.loadUi("iligui.ui", self)

        # Define our Widgets
        self.Button_Fileselect
        self.Button_Modelselect
        self.Button_Play
        self.Terminal
        self.Terminal.setReadOnly(True)

        self.Icon_Interlis
        self.Tool_Select

        self.Button_Menu
        self.Setting01
        #self.Setting01.setVisible(False)
        self.Setting02
        #self.Setting02.setVisible(False)
        self.Setting03
        #self.Setting03.setVisible(False)
        self.Setting04
        #self.Setting04.setVisible(False)
        self.Setting05
        #self.Setting05.setVisible(False)
        self.Setting06
        #self.Setting06.setVisible(False)
        

        # Define our Connections
        self.Button_Fileselect.clicked.connect(self.fileselect)
        self.Button_Modelselect.clicked.connect(self.modelselect)
        self.Button_Play.clicked.connect(self.playselect)
        self.Icon_Interlis.clicked.connect(self.interlisselect)
        self.Tool_Select.activated.connect(self.toolselect)
        self.Button_Menu.clicked.connect(self.menuselect)
        self.Setting01.clicked.connect(self.setting01select)
        self.Setting02.clicked.connect(self.setting02select)
        self.Setting03.clicked.connect(self.setting03select)
        self.Setting04.clicked.connect(self.setting04select)
        self.Setting05.clicked.connect(self.setting05select)
        self.Setting06.clicked.connect(self.setting06select)


        # Show the App
        self.show()

    def fileselect(self):
        # Open a file dialog and allow the user to select a file
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis Files (*.itf *.xtf *.xml)")
        if self.file_path != "":
            self.Terminal.appendPlainText("Loaded Transfer File from " + self.file_path)
    def modelselect(self):
        # Open a file dialog and allow the user to select a file
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
        self.Terminal.appendPlainText("Loaded Model from " + self.model_path)

    def playselect(self): # Check JRE Installation in Current working directory and Run JAR through it
        import logic_playbutton
        # Use subprocess method to run the Jar file with the selected input options
        logic_playbutton.checkinstall_cwdjava()

        try:
            textoutput = logic_playbutton.run_ilivalidator(self.file_path)
            self.Terminal.appendPlainText(textoutput)
        except AttributeError:
            self.Terminal.appendPlainText("An XML Transfer-File must be selected!")
            
    def interlisselect(self):
        import webbrowser
        # TODO: Check for validity of URL
        webbrowser.open("https://github.com/claeis/ilivalidator/blob/master/docs/ilivalidator.rst")

    def toolselect(self):
        self.Terminal.appendPlainText("Toolsselect ...")

    def menuselect(self):
        if self.Setting01.isVisible() == False:
            # Unhide all the settings buttons
            self.Setting01.setVisible(True)
            self.Setting02.setVisible(True)
            self.Setting03.setVisible(True)
            self.Setting04.setVisible(True)
            self.Setting05.setVisible(True)
            self.Setting06.setVisible(True)
        else:
            # Hide all the settings buttons
            self.Setting01.setVisible(False)
            self.Setting02.setVisible(False)
            self.Setting03.setVisible(False)
            self.Setting04.setVisible(False)
            self.Setting05.setVisible(False)
            self.Setting06.setVisible(False)

    def setting01select(self):
        self.Terminal.appendPlainText("settingselect 01...")
    def setting02select(self):
        self.Terminal.appendPlainText("settingselect 02...")
    def setting03select(self):
        self.Terminal.appendPlainText("settingselect 03...")
    def setting04select(self):
        self.Terminal.appendPlainText("settingselect 04...")
    def setting05select(self):
        self.Terminal.appendPlainText("settingselect 05...")
    def setting06select(self):
        self.Terminal.appendPlainText("settingselect 06...")

# Initialize the App
app = QApplication(sys.argv)
UIWindow = iligui()
app.exec()