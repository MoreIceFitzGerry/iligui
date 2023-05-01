from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6 import uic, QtGui
from iligui_settings import ilisettingsgui
import sys


class iligui(QMainWindow):
    def __init__(self):
        super(iligui, self).__init__()

        # Load UI File
        uic.loadUi("window_main.ui", self)

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Main Widgets
        self.interlisButton
        self.settingsButton
        self.fileselectButton
        self.modelselectButton
        self.playButton
        self.errorFrame
        self.errorFrame.setVisible(False)
        self.errorText
        self.errorText.setReadOnly(True)
        self.errorButton
        self.helpFrame
        self.helpFrame.setVisible(False)
        self.helpText
        self.helpButton

        # Options Bin to pass to commands
        self.settings = []
        #-----------------------------------------------------------------------------------------------------------------

        # Custom Widget Adjustements--------------------------------------------------------------------------------------
        # DragNdrop functionality for Button_Fileselect Widget
        # TODO: NEED TO MAKE SURE ONLY CORRECT INPUT ARE ALLOWED, JUST LIKE IN THE DIALOG
        def handleDragEvent(event):
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
        def handleDropEvent_filepath(event):
            for url in event.mimeData().urls():
                self.file_path = url.toLocalFile()
                print("Loaded Transfer File from Dropped File: " + self.file_path)
        def handleDropEvent_modelpath(event):
            for url in event.mimeData().urls():
                self.model_path = url.toLocalFile()
                print("Loaded Model File from Dropped File: " + self.model_path)
        # Find the QToolButton and connect its signals to custom slots
        self.fileselectButton.dragEnterEvent = handleDragEvent
        self.modelselectButton.dragEnterEvent = handleDragEvent
        self.fileselectButton.dropEvent = handleDropEvent_filepath
        self.modelselectButton.dropEvent = handleDropEvent_modelpath
        #-----------------------------------------------------------------------------------------------------------------

        # Define our Connections------------------------------------------------------------------------------------------
        self.interlisButton.clicked.connect(self.interlisselect)
        self.settingsButton.clicked.connect(self.settingsselect)
        self.fileselectButton.clicked.connect(self.fileselect)
        self.modelselectButton.clicked.connect(self.modelselect)
        self.playButton.clicked.connect(self.playselect)
        self.errorButton.clicked.connect(self.errorselect)

        # Ensure Readiness for Java Interoperability----------------------------------------------------------------------
        # Check JRE Installation in Current working directory, if not install in CWD
        import logic_checkjava
        logic_checkjava.checkinstall_cwdjava()
        #-----------------------------------------------------------------------------------------------------------------

        # Show the App directly at the end of initialization
        self.show()
        self.myWidth = self.width()
        self.myHeight = self.minimumHeight()
        self.resize(self.myWidth, self.myHeight)


    # Methods to Run TODO: SEPERATE FROM THIS FILE AND IMPORT-------------------------------------------------------------
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressPos = event.pos()
    #https://stackoverflow.com/questions/72940478/pyqt-event-when-button-clicked
    #https://stackoverflow.com/questions/67638434/detect-single-mouse-click-in-pyqt5-widgets-missing-mouseclickevent-function

    def reset_PlayButton(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
    """

    def fileselect(self):
        # Open a file dialog and allow the user to select a file
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis Files (*.itf *.xtf *.xml)")
        if self.file_path != "":
            print("Loaded Transfer File from " + self.file_path)

    def modelselect(self):
        # Open a file dialog and allow the user to select a file
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
        print("Loaded Model from " + self.model_path)

    def playselect(self):
        # Use subprocess method to run the Jar file with the selected input options
        import logic_playbutton
        try:
            textoutput = logic_playbutton.run_ilivalidator(self.settings, self.file_path)
            if "Info: ...validation done" in textoutput:
                self.errorFrame.setVisible(False)
                self.helpFrame.setVisible(False)
                self.playButton.setIcon(QtGui.QIcon("icons/circle_good_green.png"))
                self.resize(self.myWidth, self.myHeight)
            else:
                self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
                self.errorFrame.setVisible(True)
                self.errorText.appendPlainText(textoutput)

        except AttributeError as e:
            self.errorFrame.setVisible(True)
            self.errorText.appendPlainText(repr(e))
            self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
            self.errorText.appendPlainText("An XML Transfer-File must be selected!")

    def errorselect(self):
        self.helpFrame.setVisible(True)
        self.helpText.appendPlainText("Some Help Suggestions")

    def interlisselect(self):
        import webbrowser
        # TODO: Check for validity of URL
        webbrowser.open("https://github.com/claeis/ilivalidator/blob/master/docs/ilivalidator.rst")

    def settingsselect(self):
        from iligui_settings import ilisettingsgui
        self.secondUIWindow = ilisettingsgui()
        # overwrite self.options with new settings from settingswindow
        self.settings = self.secondUIWindow.options
        print(f"Current Settings: {self.settings}")
    #---------------------------------------------------------------------------------------------------------------------

# Initialize the App
app = QApplication(sys.argv)
UIWindow = iligui()
app.exec()