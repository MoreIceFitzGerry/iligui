from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QInputDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6.QtCore import QUrl,QPropertyAnimation, QThread
from PyQt6 import uic, QtGui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

# from PyQt6.QtWebEngineWidgets import QWebEngineView # Note: PyQt6-WebEngine still builds upon requisits from its older version, PyQTWebEngine-qt5 so it is also necessary to install this




class ilimodelselectgui(QDialog):
    def __init__(self):
        super(ilimodelselectgui, self).__init__()
        # Load UI File
        uic.loadUi("dialog_modelselect.ui", self)

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Frame
        self.queryFrame.setVisible(False)
        ## Radiobutton
        self.onlinesearchRadiobutton
        ## Button
        self.okButton
        ## QueryEntry
        self.lineEdit

        # Define our Connections------------------------------------------------------------------------------------------
        # self.closeButton.clicked.connect(lambda: self.close())
        # Radiobutton connection
        self.onlinesearchRadiobutton.toggled.connect(self.onlineselect)
        # Button connection
        self.okButton.clicked.connect(self.ok) # Result code and closes dialog
        # self.okButton.clicked.connect(lambda: self.accept()) # Result code and closes dialog

        self.adjustSize() # Adjusts the main window to fit its contents minimally

    def onlineselect(self, checked):
        if checked:
            self.queryFrame.setVisible(True)
        else:
            self.queryFrame.setVisible(False)
            self.resize(self.width(), self.height()-self.queryFrame.height())
    
    def ok(self):
        if self.onlinesearchRadiobutton.isChecked():
            # text, ok = QInputDialog.getText(None, "Search INTERLIS Model Browser", "Enter Model Name:")
            text = self.lineEdit.text()
            options = Options()
            options.headless = True
            options.add_argument("--ignore-certificate-errors") # CANNOT GET CORRECT RESULTS FROM https://ilimodels.ch OTHERWISE, BUT NOTE SECURITY RISK!
            driver = webdriver.Chrome(options=options)
            url = f"https://ilimodels.ch/?query={text}"
            driver.get(url)
            html = driver.page_source
            driver.quit()
            soup = BeautifulSoup(html, "html.parser")
            links = soup.find_all("a", href=lambda href: href and href.endswith(".ili"))
            if links:
                first_link = links[0].get("href")
                print(f"First .ili link: {first_link}")
                self.model_path = first_link
            else:
                print("No .ili links found")
                self.model_path = ""
            self.accept()
        elif self.localsearchRadiobutton.isChecked():
            self.model_path, ok = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
            self.accept()
        else:
            self.reject()

        # document.querySelector("#root > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-1qsxih2 > div > div.MuiBox-root.css-w2uu6y > div:nth-child(1) > div.css-1bcexqj > div:nth-child(6) > a")
        # <a href="https://models.geo.admin.ch/BAFU/NoisePollutionRegisterForNationalRoads_V1_1.ili" target="_blank" rel="noreferrer">BAFU/NoisePollutionRegisterForNationalRoads_V1_1.ili</a>
        #root > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-1qsxih2 > div > div.MuiBox-root.css-w2uu6y > div:nth-child(1) > div.css-1bcexqj > div:nth-child(6) > a