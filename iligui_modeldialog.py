from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6 import uic, QtGui
import sys
import os


class ilimodelselectgui(QDialog):
    def __init__(self, main_window):
        super(ilimodelselectgui, self).__init__()
        # Load UI File
        uic.loadUi("dialog_modelselect.ui", self)

        # Pass Values from Main Window self over to this window
        self.mainwindow = main_window
        self.model_name = self.mainwindow.model_name
        self.model_url = self.mainwindow.model_url
        self.localmodel_filename = ""
        self.localmodel_path = ""
        self.modelName_text.setText(self.model_name)
        self.modelPath_text.setText(self.model_url)
        # Prepare Value that will be passed back to mainwindow
        self.model_path = self.model_url

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Frames
        self.transferfileButtonFrame.setVisible(True)
        self.onlinesearchButtonFrame.setVisible(False)
        self.localsearchButtonFrame.setVisible(False)
        ## Radiobuttons
        self.transferfileRadiobutton
        self.onlinesearchRadiobutton
        self.localsearchRadiobutton
        ## Buttons
        self.transferfileButton
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
        self.transferfileButton.clicked.connect(self.opentransferfilemodel)
        self.onlinesearchButton.clicked.connect(self.getonlinemodel)
        self.localsearchButton.clicked.connect(self.getlocalmodel)
        self.okButton.clicked.connect(lambda: self.close())

         # Validation Setting
        # self.setting1_1.toggled.connect(lambda : self.setsettings("--forceTypeValidation")) #Force Type Validation

        # Show the App directly at the end of initialization
       # Run this window, locking the other window behind it
        self.exec()
        # self.resize(self.width(), self.MainFrame.sizeHint().height())
        self.adjustSize() # Adjusts the main window to fit its contents minimally

    def  showtransferfilesource(self, checked):
        if checked == True:
            self.model_name = self.mainwindow.model_name
            self.model_url = self.mainwindow.model_url
            self.modelName_text.setText(self.model_name)
            self.modelPath_text.setText(self.model_url)
        self.transferfileButtonFrame.setVisible(checked)

    def  showonlinesource(self, checked):
        self.onlinesearchButtonFrame.setVisible(checked)

    def  showlocalsource(self, checked):
        if checked == True and self.localmodel_filename != "":
            self.modelName_text.setText(self.localmodel_filename)
            self.modelPath_text.setText(self.localmodel_path)
            self.model_path = self.localmodel_path
        self.localsearchButtonFrame.setVisible(checked)

    def opentransferfilemodel(self):
        self.modelname.setText("B")
        self.modelVersion.setText("HaHa")
        self.modelPath.setText("Nana")
        print("banana")

    def getonlinemodel(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec() # modal dialog, blocks input to other visible windows in the same application until it is closed

    def getlocalmodel(self):
        self.localmodel_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
        self.localmodel_filename = os.path.basename(self.model_path)
        self.modelName_text.setText(self.localmodel_filename)
        self.modelPath_text.setText(self.localmodel_path)
        self.model_path = self.localmodel_path
