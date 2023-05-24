from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit, QProgressBar, QToolBox
from PyQt6.QtCore import QPropertyAnimation, QSize, QRect, QVariantAnimation
from PyQt6 import uic, QtGui
from iligui_settings import ilisettingsgui
import sys
import logic_playbutton
import xml.etree.ElementTree as ET
import webbrowser
import time


class iligui(QMainWindow):
    def __init__(self):
        super(iligui, self).__init__()

        # Load UI File
        uic.loadUi("window_main.ui", self)
        # Set the Icon -> do this with Pyinstaller!
        #self.setWindowIcon(QtGui.QIcon("icons/interlis.png"))

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Central Widget
        self.centralwidget

        ## Main Widgets
        self.interlisButton
        self.settingsButton
        self.fileselectButton
        self.modelselectButton
        self.playButton
        self.topFrame
        self.errorFrame
        self.errorFrame.setVisible(False) # hide frame
        self.errorText
        self.errorButton
        self.helpFrame
        self.helpFrame.setVisible(False) # hide frame
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
        self.errorButton.clicked.connect(self.helptoggle)
        self.helpButton.clicked.connect(self.furtherhelp)

        # Ensure Readiness for Java Interoperability----------------------------------------------------------------------
        # Check JRE Installation in Current working directory, if not install in CWD
        import logic_checkjava
        logic_checkjava.checkinstall_cwdjava()
        #-----------------------------------------------------------------------------------------------------------------

        # Show the App directly at the end of initialization
        self.show()
        # self.resize(self.width(), self.topFrame.sizeHint().height())
        # self.centralwidget.adjustSize() # Adjusts the central widget to fit its contents minimally
        self.adjustSize() # Adjusts the main window to fit its contents minimally

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
        try:
            # Use subprocess method to run the Jar file with the selected input options
            xtflog_path = logic_playbutton.run_ilivalidator(self.settings, self.file_path)
            # Prepare the XTF File for element finding
            tree = ET.parse(xtflog_path)
            root = tree.getroot()
            # Get the namespace of the root element
            ns = root.tag.split('}')[0].strip('{')

            # Find Elements of the IliVErrors.Errorlog where <Type> has text "Error"
            error_elements = []
            for element in root.findall(".//{%s}IliVErrors.ErrorLog.Error" % ns):
                element_type = element.find("{%s}Type" % ns).text
                if element_type == "Error":
                    errorMessage = element.find("{%s}Message" % ns)
                    DataSource = element.find("{%s}DataSource" % ns)
                    # Then find the following elements, IF THEY EXIST (Can vary depending on the error)
                    Line = element.find("{%s}Line" % ns)
                    objectTag = element.find("{%s}ObjTag" % ns)
                    tagIdentification = element.find("{%s}Tid" % ns)

                    if objectTag is None or tagIdentification is None or Line is None:
                        # print("errorMessage: ", errorMessage.text)
                        error_elements.append(f"<a href='file:///{self.file_path}' style='color:red;'>Error found: {errorMessage.text}</a>")
                    else:
                        # print("errorMessage: ", errorMessage.text, "objectTag: ", objectTag.text, "tagIdentification: ", tagIdentification.text, "DataSource: ", DataSource.text, "Line: ", Line.text)
                        error_elements.append(f"<a href='file:///{self.file_path}' style='color:red;'>Error found: Line {Line.text}, TagID {tagIdentification.text}, objectTag {objectTag.text}: {errorMessage.text}</a>")

            # Preload the Help text for the Found Errors
            """
            import errorMessages
            for error_element in error_elements:
                for errorMessage in errorMessages:
                    if error_element in errorMessage:
                        print(errorMessage)
            """
            # Convert the error_elements list to a string for printing
            print(error_elements)
            if (len(error_elements) == 1):
                error_text = error_elements[0]
            else:
                error_text = "<br>".join(error_elements) # Join them with breaks
            print(error_text)

            with open(xtflog_path, 'r') as f:
                xtflog_content = f.read()
                # Parse the xtf log file here and extract the relevant information

            if "...validation done" in xtflog_content:
                self.playButton.setIcon(QtGui.QIcon("icons/circle_good_green.png"))
                self.hideErrorFrame()
            else:
                print("Validation Error...")
                self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
                self.showErrorFrame()
                self.errorText.setText(error_text)

        except AttributeError as e:
            print("Execution Error...")
            self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
            self.showErrorFrame()
            self.errorText.setText(f"<a style='color:red;'>Error found: {repr(e)}</a>")

    # Resize-Animation of MainWindow Height
    def updateHeight(self, value):
        self.resize(self.width(), value)
    def resizeMainWindowHeight(self, oldHeight, newHeight):
        self.resizeAnimation = QVariantAnimation()
        self.resizeAnimation.setDuration(300)
        self.resizeAnimation.setStartValue(oldHeight)
        self.resizeAnimation.setEndValue(newHeight)
        self.resizeAnimation.valueChanged.connect(self.updateHeight) # Update the main window's height with current value of the animation
        self.resizeAnimation.start()

    def mainWindowHeightShrink(self):
        oldHeight = self.height() # Get current height
        newHeight = self.height() - self.errorFrame.sizeHint().height() # Get the recommended height from sizeHint

    def showErrorFrame(self):
        # Regrow the frame to its recommended size
        # newHeight = self.errorFrame.sizeHint().height() # Get recommended height
        self.errorFrame.setVisible(True) # Show the Frame
        # newHeight = self.errorFrame.sizeHint().height()
        # self.errorFrame.resize(self.width(), newHeight)
        
        oldHeight = self.height() # Get current height
        newHeight = self.sizeHint().height() # Get the recommended height from sizeHint
        self.mainWindowHeightGrow()

    def hideErrorFrame(self):
        self.errorFrame.setVisible(False) # Hide the Frame
        self.mainWindowHeightShrink()
        # if self.errorFrame.height() != 1: # Skip animation if frame is already shrunk
            # Shrink the frame to minimal height
            # oldHeight = self.errorFrame.height() # Get current height
            # newHeight = 1
            # self.animation = QVariantAnimation()
            # self.animation.setDuration(300)
            # self.animation.setStartValue(oldHeight)
            # self.animation.setEndValue(newHeight)
            # self.animation.valueChanged.connect(self.updateErrorFrameHeight)
            # self.animation.finished.connect(self.mainWindowHeightResize)
            # self.animation.start()
        # else:
            # pass

    # Resize-Animations of helpFrame Height
    def updateHelpFrameHeight(self, value):
        self.helpFrame.resize(self.width(), value)
    def helptoggle(self):
        if self.helpFrame.height() == 1: # If frame is already shrunk, grow animation
            self.helpFrame.setVisible(True) # Show the Frame
            newHeight = self.helpFrame.sizeHint().height()
            self.helpFrame.resize(self.width(), newHeight)
            self.mainWindowHeightResize()
        else:
            # Shrink the frame to minimal height
            newHeight = 1
            self.helpFrame.resize(self.width(), newHeight)
            self.helpFrame.setVisible(False)# Hide the Frame
            self.mainWindowHeightResize()

    def furtherhelp(self):
        # TODO: Check for validity of URL
        webbrowser.open("https://geostandards-ch.github.io/doc_refhb24/")

    def interlisselect(self):
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

# self.errorFrame.setFixedHeight(self.errorFrame.sizeHint().height()) # show frame
# self.errorFrame.setFixedHeight(0) # hide frame