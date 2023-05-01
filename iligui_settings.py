from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6 import uic, QtGui
import sys


class ilisettingsgui(QDialog):
    def __init__(self):
        super(ilisettingsgui, self).__init__()

        # Load UI File
        uic.loadUi("window_settings.ui", self)

        # Define our Widgets----------------------------------------------------------------------------------------------
        self.closeButton
        self.saveButton
        self.stackedWidget

        self.settingButton1 #Validation Settings
        self.setting1_1 # Force Type Validation
        self.setting1_2 #Disable Area Validation
        self.setting1_3 #Disable Constraining Validation
        self.setting1_4 #All Objects Accessible

        self.settingButton2 #Config Files
        self.setting2_1 # Set Config File
        self.setting2_2 # Set Metaconfig File

        self.settingButton3 #Log Settings
        self.setting3_1 #Enable Log Time
        self.setting3_2 #Enable Trace Logs
        self.setting3_3 #Log Export Location

        self.settingButton4 #Proxy Access
        self.setting4_11 # Checkbox Proxy Host Server
        self.setting4_12 # Lineedit ex: Server Nr: 192.168.1.100
        self.setting4_13 # Toolbutton Proxy Host Server
        self.setting4_21 # Checkbox Proxy Host Port
        self.setting4_22 # Lineedit ex: Port Nr: 8080
        self.setting4_23 # Toolbutton Proxy Host Port

        self.settingButton5 # Plugins
        self.setting5_11 # Checkbox Plugins
        self.setting5_12 # Lineedit ex: Plugins Directory Path
        self.setting5_13 # Toolbutton Plugins

        # Options Bin to pass to command
        self.options = []

        # Define our Connections------------------------------------------------------------------------------------------
        self.closeButton.clicked.connect(lambda: self.close())
        #TODO: CREATE A CONGIF FILE ANDS SAVE OUR SETTINGS SO WE CAN CALL IT WHEN OPENING AGAIN!
        #self.saveButton.clicked.connect(self.setsettings)

        self.settingButton1.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.settingButton2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.settingButton3.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))
        self.settingButton4.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(3))
        self.settingButton5.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(4))

        # Validation Setting
        self.setting1_1.toggled.connect(lambda : self.setsettings("--forceTypeValidation")) #Force Type Validation
        self.setting1_2.toggled.connect(lambda : self.setsettings("--disableAreaValidation")) #Disable Area Validation
        self.setting1_3.toggled.connect(lambda : self.setsettings("--disableConstraintValidation")) #Disable Constraining Validation
        self.setting1_4.toggled.connect(lambda : self.setsettings("--allObjectsAccessible")) #All Objects Accessible
        #-----------------------------------------------------------------------------------------------------------------

        # Options Verbose to Pass as commands
        self.commands = [
        ["--forceTypeValidation", "--disableAreaValidation", "--disableConstraintValidation", 
         "--allObjectsAccessible", "--multiplicityOff", "--singlePass", "--skipPolygonBuilding"
          "--allowItfAreaHoles"],
        ["--config filename", "--metaConfig filename"],
        ["--models modelnames", "--modeldir path"],
        ["--check-repo-data repositoryUrl"],
        ["--createIliData --ilidata ilidata.xml --repos repository"],
        ["--srcfiles files.txt"],
        ["--updateIliData --ilidata updatedIlidata.xml --repos repository --dataset datasetId newVersionOfData.xml"],
        ["--logtime", "--log filename", "--xtflog filename"],
        ["--plugins folder"],
        ["--proxy host", "--proxyPort port"],
        ["--gui"],
        ["--verbose", "--trace", "--help", "--version"]
          ]
        #-----------------------------------------------------------------------------------------------------------------

        # Show the App directly at the end of initialization
        self.exec()
        self.myWidth = self.width()
        self.myHeight = self.minimumHeight()
        self.resize(self.myWidth, self.myHeight)

    # Methods to Run TODO: SEPERATE FROM THIS FILE AND IMPORT-------------------------------------------------------------
    def setsettings(self, command):
        if command not in self.options:
            self.options.append(command)
        else:
            self.options.remove(command)

    #---------------------------------------------------------------------------------------------------------------------
    #commands-------------------------------------------------------------------------------------------------------------
    """
    "--forceTypeValidation"
    "--disableAreaValidation"
    "--disableConstraintValidation"
    "--allObjectsAccessible"
    "--multiplicityOff"
    "--singlePass"
    "--skipPolygonBuilding"
    "--allowItfAreaHoles"

    self.options.append("--singlePass")
    self.Terminal.appendPlainText("settingselect --singlePass")
    """
    #---------------------------------------------------------------------------------------------------------------------

