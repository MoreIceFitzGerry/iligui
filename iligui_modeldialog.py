from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QInputDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6.QtCore import QUrl,QPropertyAnimation, QThread
from PyQt6 import uic, QtGui
from urllib import request
import re
import webbrowser
import os

basedir = os.path.normpath(os.path.dirname(__file__))
basedir = basedir.replace('\\', '/')
print("basedir_modeldialog: ", basedir)

class ilimodelselectgui(QDialog):
    def __init__(self, model_name, saved_model_link):
        super(ilimodelselectgui, self).__init__()
        # Load UI File
        uic.loadUi(os.path.join(basedir, "ui_files/dialog_modelselect.ui"), self)
        # Load External Variable
        self.model_name_tf = model_name # Model name we read out from the transferfile
        self.model_link = saved_model_link

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Frame
        self.queryFrame.setVisible(False)
        ## Radiobutton
        self.onlinesearchRadiobutton
        ## QueryEntry
        self.lineEdit
        ## Button
        self.searchButton
        self.okButton

        # Define our Connections------------------------------------------------------------------------------------------
        # self.closeButton.clicked.connect(lambda: self.close())
        # Radiobutton connection
        self.onlinesearchRadiobutton.toggled.connect(self.onlineselect)
        # Text entry connection
        self.lineEdit.textChanged.connect(self.update_icon)
        # Button connection
        self.searchButton.clicked.connect(self.searchmodel) # Find model and display if valid link
        self.okButton.clicked.connect(self.ok) # Result code and closes dialog
        # self.okButton.clicked.connect(lambda: self.accept()) # Result code and closes dialog

        self.adjustSize() # Adjusts the main window to fit its contents minimally
        
        ### STYLESHEET ADJUSTEMENTS BASE ON LOGIC - NECESSARY FOR PACKAGING OF APP TO DECLARE HERE
        checked_icon = basedir + "/icons/check-circle-green.svg"
        unchecked_icon = basedir + "/icons/circle.svg"
        self.setStyleSheet("""
        QRadioButton::indicator:checked {{image: url({0});}}
        QRadioButton::indicator:unchecked {{image: url({1});}}
        """.format(checked_icon, unchecked_icon))

    def onlineselect(self, checked):
        if checked:
            self.queryFrame.setVisible(True)
        else:
            self.queryFrame.setVisible(False)
            self.resize(self.width(), self.height()-self.queryFrame.height())

    def ok(self):
        if self.onlinesearchRadiobutton.isChecked():
            print("online search")
            self.model_path = self.lineEdit.text()
            # Parse the URL Model to get the Model Name
            if self.model_path.endswith('.ili'):
                response = request.urlopen(self.model_path)
                html_content = response.read().decode('utf-8')
                match = re.search(r'MODEL\s+(\w+)', html_content)
                if match:
                    self.model_name_mf = match.group(1)
                else:
                    self.model_name_mf = ""

        elif self.localsearchRadiobutton.isChecked():
            print("local search")
            self.model_path, ok = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
            # Parse the local model to get the Model Name
            if self.model_path.endswith('.ili'):
                with open(self.model_path, 'r') as f:
                    text = f.read()
                match = re.search(r'MODEL\s+(\w+)', text)
                if match:
                    self.model_name_mf = match.group(1)
                else:
                    self.model_name_mf = ""

        else:
            print("auto search")
            self.model_path = "auto"
            # model.name will not be adjusted

        self.accept()

    def update_icon(self):
        url = self.lineEdit.text()
        if self.lineEdit.text() and self.check_valid_url(url):
            self.lineEdit.setStyleSheet("QLineEdit { color: green; }")
        elif not self.lineEdit.text():
            self.lineEdit.setStyleSheet("QLineEdit { color: black; }")
        else:
            self.lineEdit.setStyleSheet("QLineEdit { color: red; }")

    def check_valid_url(self, url):
        url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') # definition of a valid URL Code
        # Check if Valid URL and if it ends with .ili since we want to check if it fits the model later
        if url_regex.match(url) and re.search(r'\.ili$', url):
            return True
        else:
            print(f"{url} is not a valid URL")
            return False
    
    def searchmodel(self):
        # TODO: Check for validity of URL
        webbrowser.open("https://ilimodels.ch/")