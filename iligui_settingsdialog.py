from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox, QCheckBox
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QSettings
import os

basedir = os.path.normpath(os.path.dirname(__file__))
basedir = basedir.replace('\\', '/')

class ilisettingsgui(QDialog):
    def __init__(self, savesettings):
        super(ilisettingsgui, self).__init__()

        # Load UI File
        uic.loadUi(os.path.join(basedir, "ui_files/dialog_settings.ui"), self)

        # Use the QSettings object passed from the main window
        self.savesettings = savesettings

        # Options Bin to pass to command
        self.options = []

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Buttons
        self.configButton
        self.okButton
        ## Checkboxbuttons and immediate restoring of each saved state
        self.validationOption0.setChecked(self.savesettings[0])
        self.validationOption1.setChecked(self.savesettings[1])
        self.validationOption2.setChecked(self.savesettings[2])
        self.validationOption3.setChecked(self.savesettings[3])

        # Define our Connections------------------------------------------------------------------------------------------
        # Accept
        self.okButton.clicked.connect(self.ok)
        #-----------------------------------------------------------------------------------------------------------------

        self.adjustSize() # Adjusts the main window to fit its contents minimally
        
        ### STYLESHEET ADJUSTEMENTS BASE ON LOGIC - NECESSARY FOR PACKAGING OF APP TO DECLARE HERE
        print(basedir)
        checked_icon = basedir + "/icons/check-circle-green.svg"
        unchecked_icon = basedir + "/icons/circle.svg"
        print(checked_icon, unchecked_icon)
        self.setStyleSheet("""
        QCheckBox::indicator:checked {{image: url({0});}}
        QCheckBox::indicator:unchecked {{image: url({1});}}
        """.format(checked_icon, unchecked_icon))

    # Methods to Run TODO: SEPERATE FROM THIS FILE AND IMPORT-------------------------------------------------------------
    def setsetting(self, option, nr, command):
        if option.isChecked() == True:
            self.savesettings[nr] = True
            if command not in self.options:
                self.options.append(command)
            else:
                pass
        if option.isChecked() == False:
            self.savesettings[nr] = False
            if command in self.options:
                self.options.remove(command)
            else:
                pass

    def ok(self):
        # Save the state of each checkbox into a reset form when the dialog is closed
        self.setsetting(self.validationOption0, 0, "--forceTypeValidation") #Force Type Validation
        self.setsetting(self.validationOption1, 1, "--disableAreaValidation") #Force Type Validation
        self.setsetting(self.validationOption2, 2, "--disableConstraintValidation") #Force Type Validation
        self.setsetting(self.validationOption3, 3, "--allObjectsAccessible") #Force Type Validation

        self.accept()
    #---------------------------------------------------------------------------------------------------------------------
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

