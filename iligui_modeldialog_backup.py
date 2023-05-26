from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6.QtCore import QUrl
from PyQt6 import uic, QtGui
from PyQt6.QtWebEngineWidgets import QWebEngineView
import webbrowser
import sys
import os


class ilimodelselectgui(QDialog):
    def __init__(self, main_window):
        super(ilimodelselectgui, self).__init__()
        # Load UI File
        uic.loadUi("dialog_modelselect.ui", self)
        
        # Get main_window data
        self.mainWindow = main_window
        # Get file_path from Main Window
        self.file_path = self.mainWindow.file_path
        # Get model_name from Main Window (Model name found in Transfer file)
        self.model_name = self.mainWindow.model_name
        self.model_path = "Automatic Search on Validation Begin"
        # First Values are these since no input results in this
        self.modelName_text.setText(self.model_name)
        self.modelPath_text.setText(self.model_path)

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Frames
        self.onlinesearchButtonFrame.setVisible(False)
        self.localsearchButtonFrame.setVisible(False)
        ## Radiobuttons
        self.transferfileRadiobutton
        self.onlinesearchRadiobutton
        self.localsearchRadiobutton
        ## Buttons
        self.onlinesearchButton
        self.localsearchButton
        self.okButton
        ## Textfields
        self.modelName_text
        self.modelPath_text

        # Define our Connections------------------------------------------------------------------------------------------
        # self.closeButton.clicked.connect(lambda: self.close())
        # Radiobutton connections
        self.transferfileRadiobutton.toggled.connect(self.showtransferfilesource)
        self.onlinesearchRadiobutton.toggled.connect(self.showonlinesource)
        self.localsearchRadiobutton.toggled.connect(self.showlocalsource)
        # Button connections
        self.onlinesearchButton.clicked.connect(self.getonlinemodel)
        self.localsearchButton.clicked.connect(self.getlocalmodel)
        self.okButton.clicked.connect(lambda: self.accept()) # Result code and closes dialog

         # Validation Setting
        # self.setting1_1.toggled.connect(lambda : self.setsettings("--forceTypeValidation")) #Force Type Validation

        # Show the App directly at the end of initialization
       # Run this window, locking the other window behind it
        # self.exec()
        # self.resize(self.width(), self.MainFrame.sizeHint().height())
        self.adjustSize() # Adjusts the main window to fit its contents minimally

    def  showtransferfilesource(self, checked):
        if checked == True:
            self.model_name = self.mainWindow.model_name # Reset the model name
            self.model_path = "Automatic Search on Validation Begin"
            self.modelName_text.setText(self.model_name)
            self.modelPath_text.setText(self.model_path)

    def  showonlinesource(self, checked):
        self.onlinesearchButtonFrame.setVisible(checked)

    def  showlocalsource(self, checked):
        if checked == True:
            self.modelName_text.setText(self.model_name)
            self.modelPath_text.setText(self.model_path)
        self.localsearchButtonFrame.setVisible(checked)

    def getonlinemodel(self):
        view = QWebEngineView()
        view.load("https://ilimodels.ch/")
        view.show()

    def getlocalmodel(self):
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
        self.model_name = os.path.basename(self.model_path)
        self.modelName_text.setText(self.model_name)
        self.modelPath_text.setText(self.model_path)
