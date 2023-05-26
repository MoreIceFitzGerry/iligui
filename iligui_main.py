from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit, QProgressBar, QToolBox, QDialog
from PyQt6.QtCore import QPropertyAnimation, QSize, QRect, QVariantAnimation, Qt, QUrl
from PyQt6 import uic, QtGui
from iligui_modeldialog import ilimodelselectgui
from iligui_settings import ilisettingsgui
import sys
import logic_playbutton
import xml.etree.ElementTree as ET
import webbrowser
import os
import re


class iligui(QMainWindow):
    def __init__(self):
        super(iligui, self).__init__()

        # Load UI File
        uic.loadUi("window_main.ui", self)
        # Set the Icon -> do this with Pyinstaller!
        #self.setWindowIcon(QtGui.QIcon("icons/interlis.png"))

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Main Widgets for Overviews sake -> definition not strictly necessary, but help to make sure the naming is correct
        # Layout Frames
        self.MainFrame
        # ---
        self.selectedFileFrame
        self.selectedFileFrame.setVisible(False) # hide frame
        self.selectedModelFrame
        self.selectedModelFrame.setVisible(False) # hide frame
        # ---
        self.errorFrame
        self.errorFrame.setVisible(False) # hide frame
        # ---
        self.infoFrame
        self.infoFrame.setVisible(False) # hide frame
        # Buttons
        self.interlisButton
        self.settingsButton
        self.infoButton
        self.fileselectButton
        self.fileselectButtontext.setVisible(False)
        self.modelselectButton
        self.modelselectButtontext.setVisible(False)
        self.playButton
        self.playButtontext.setVisible(False)
        # ---
        self.addinfoButton
        self.openfileButton
        self.openmodelButton
        # ---
        self.extinfoButton
        # Text Fields
        self.fileText
        self.modelText
        # ---
        self.errorText
        # ---
        self.infoText

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
        self.infoButton.toggled.connect(self.infotoggle)
        self.fileselectButton.clicked.connect(self.fileselect)
        self.modelselectButton.clicked.connect(self.modelselect)
        self.playButton.clicked.connect(self.playselect)
        self.addinfoButton.clicked.connect(self.addinfotoggle)
        self.openfileButton.clicked.connect(self.openfile)
        self.openmodelButton.clicked.connect(self.openmodel)
        self.extinfoButton.clicked.connect(self.furtherhelp)
        

        # Ensure Readiness for Java Interoperability----------------------------------------------------------------------
        # Check JRE Installation in Current working directory, if not install in CWD
        import logic_checkjava
        logic_checkjava.checkinstall_cwdjava()
        #-----------------------------------------------------------------------------------------------------------------

        # Show the App directly at the end of initialization
        self.show()
        # self.resize(self.width(), self.MainFrame.sizeHint().height())
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
        # Reset Play Button
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        # Open a file dialog and allow the user to select a file
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis Files (*.itf *.xtf *.xml)")

        ## Get the Modelname that the File was written in.
        if self.file_path != "":
            # Reset Modelselect Button
            self.modelselectButton.setIcon(QtGui.QIcon("icons/model_lightblue.png"))
            self.hideerrorframe()
            """
            The ilivalidator does not get the model name from the header.
            In INTERLIS1 it reads the transferfile to the first basket.
            In INTERLIS2 it reads the first element in the DATASECTION.
            This is a Python implementation of this Process the ilivalidator does again byitself.
            The Purpose is to be able to give the User Feedback on the Modelname immediately
            """
            ### INTERLIS 1
            if self.file_path.endswith('.itf'):
                with open(self.file_path, 'r') as f:
                    text = f.read()
                match = re.search(r'MODEL\s+(\w+)', text)
                if match:
                    self.model_name = match.group(1)
                    print(self.model_name)
                else:
                    print('MODEL not found')
            ### INTERLIS 2
            else:
                tree = ET.parse(self.file_path)
                root = tree.getroot()
                ns = "{" + root.tag.split('}')[0].strip('{') + "}" # Get the namespace of the root element for further parsing
                for section in root:
                    if section.tag == ns + 'DATASECTION':
                        first_tag = section[0].tag
                        first_tag_name = first_tag.split('}')[1]
                        self.model_name = first_tag_name.split('.')[0]
                        break
            print("Loaded Transfer File from " + self.file_path)
            print("Model Name Found" + self.file_path)
            self.fileselectButton.setIcon(QtGui.QIcon("icons/circle_good_green.png"))
            filename = os.path.basename(self.file_path)
            self.fileText.setText(filename)
            self.showselectedfileframe()

    def modelselect(self):
        # Reset Play Button
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        try:
            self.modelselectUIWindow = ilimodelselectgui(self) # Create new window and pass all of self over
            result = self.modelselectUIWindow.exec()
            if result == QDialog.DialogCode.Accepted:
                self.model_path = self.modelselectUIWindow.model_path # overwrite self.model_path with the selection from modelselect window
                print(f"Current Path: {self.model_path}")
                self.modelselectButton.setIcon(QtGui.QIcon("icons/circle_good_green.png"))
                self.modelname = os.path.basename(self.model_name)
                self.modelText.setText(self.modelname)
                self.showselectedmodelframe()
        except AttributeError as e:
            print("Execution Error...")
            self.modelselectButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
            self.errorText.setText(f"Failed to execute: {repr(e)}")
            self.infoText.setText("Make sure you selected a file first!")
            self.showerrorframe()

        # Open a file dialog and allow the user to select a file
        """
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
        print("Loaded Model from " + self.model_path)
        """

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
            help_elements = []
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
                        objectTag = "Not Available"
                        tagIdentification = "Not Available"
                        Line = "Not Available"
                        # error_elements.append(f"<a href='file:///{self.file_path}' style='color:red;'>Error found: {errorMessage.text}</a>")
                    # print("errorMessage: ", errorMessage.text, "objectTag: ", objectTag.text, "tagIdentification: ", tagIdentification.text, "DataSource: ", DataSource.text, "Line: ", Line.text)
                    # error_elements.append(f"<a href='file:///{self.file_path}' style='color:red;'>Error found: Line {Line.text}, TagID {tagIdentification.text}, objectTag {objectTag.text}: {errorMessage.text}</a>")
                    error_elements.append(f"Error found: Line {Line.text}, {errorMessage.text}")
                    help_elements.append(errorMessage.text)

            # Convert the error_elements list to a string for printing
            if (len(error_elements) == 1):
                error_text = error_elements[0]
            else:
                error_text = "<br>".join(error_elements) # Join them with breaks

            # Identify the Error Name from the Text, and pass HelpMessage
            import difflib
            from errorDictionary import error_dictionary # Dictionary listing all possible errors -> Key: Error Name, Value 1: Error Text, Value 2 Error Help
            first_Values = [values[0] for values in error_dictionary.values()]
            error_help = []
            for element in help_elements:
                closest_match = difflib.get_close_matches(element, first_Values, n=1)
                if closest_match:
                    closest_match = closest_match[0]
                    for key, values in error_dictionary.items():
                        if values[0] == closest_match:
                            # error_help.append(key)
                            # error_help.append(values[1])
                            error_help.append(f"Error Name: {key}\nHelp Advice: {values[1]}\n")
                            # error_help.append(f"Help Advice: {values[1]}\n")

            # Convert the error_help list to a string for printing
            if (len(error_help) == 1):
                help_text = error_help[0]
            else:
                help_text = "".join(error_help) # Join them with breaks
            print(help_text)


            # Parse the xtf log file again to see if process succeeded or not
            with open(xtflog_path, 'r') as f:
                xtflog_content = f.read()

            if "...validation done" in xtflog_content:
                self.playButton.setIcon(QtGui.QIcon("icons/circle_good_green.png"))
                if self.infoFrame.isVisible() == True:
                    self.addinfotoggle()
                self.hideerrorframe()
                
            else:
                print("Validation Error...")
                self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
                self.errorText.setText(error_text)
                self.infoText.setText(help_text)
                self.showerrorframe()

        except AttributeError as e:
            print("Execution Error...")
            self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
            self.errorText.setText(f"Failed to execute: {repr(e)}")
            self.infoText.setText("Make sure you have selected files correctly!")
            self.showerrorframe()

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
    
    # Adjust MainWindow Height for selectedfileFrame
    def showselectedfileframe(self):
        self.selectedFileFrame.setVisible(True) # Show the Frame
        if self.height() > self.sizeHint().height(): # If Current Frame is Bigger than it needs to be, no resize needs to be done
            pass
        else:
            oldHeight = self.height() # Get current height
            # newHeight = self.height() + self.errorFrame.sizeHint().height() # Add the recommended height from sizeHint
            newHeight = self.sizeHint().height()
            self.resizeMainWindowHeight(oldHeight, newHeight)
    
    # Adjust MainWindow Height for selectedmodelFrame
    def showselectedmodelframe(self):
        self.selectedModelFrame.setVisible(True) # Show the Frame
        if self.height() > self.sizeHint().height(): # If Current Frame is Bigger than it needs to be, no resize needs to be done
            pass
        else:
            oldHeight = self.height() # Get current height
            # newHeight = self.height() + self.errorFrame.sizeHint().height() # Add the recommended height from sizeHint
            newHeight = self.sizeHint().height()
            self.resizeMainWindowHeight(oldHeight, newHeight)

    # Adjust MainWindow Height for selectedmodelFrame for errorFrame
    def showerrorframe(self):
        self.errorFrame.setVisible(True) # Show the Frame
        if self.height() > self.sizeHint().height(): # If Current Frame is Bigger than it needs to be, no resize needs to be done
            pass
        else:
            oldHeight = self.height() # Get current height
            # newHeight = self.height() + self.errorFrame.sizeHint().height() # Add the recommended height from sizeHint
            newHeight = self.sizeHint().height()
            self.resizeMainWindowHeight(oldHeight, newHeight)

    def hideerrorframe(self):
        self.errorFrame.setVisible(False) # Hide the Frame
        if self.windowState() == Qt.WindowState.WindowMaximized or self.windowState() == Qt.WindowState.WindowFullScreen:  # If in Fullscreen, no resize needs to be done
            pass
        else:
            oldHeight = self.height() # Get current height
            newHeight = self.MainFrame.sizeHint().height()
            self.resizeMainWindowHeight(oldHeight, newHeight)

    # Adjust MainWindow Height for infoFrame
    def updateinfoframeheight(self, value):
        self.infoFrame.resize(self.width(), value)
    def addinfotoggle(self):
        if self.infoFrame.isVisible() == False: # If frame is hidden, show infoFrame
            self.addinfoButton.setIcon(QtGui.QIcon("icons/chevron-down.svg"))
            self.infoFrame.setVisible(True) # Show the Frame
            if self.windowState() == Qt.WindowState.WindowMaximized or self.windowState() == Qt.WindowState.WindowFullScreen:  # If in Fullscreen, no resize needs to be done
                pass
            else:
                oldHeight = self.height()
                newHeight = self.sizeHint().height()
                self.resizeMainWindowHeight(oldHeight, newHeight)
        else:
            self.addinfoButton.setIcon(QtGui.QIcon("icons/info.svg"))
            self.infoFrame.setVisible(False) # Hide the Frame
            if self.windowState() == Qt.WindowState.WindowMaximized or self.windowState() == Qt.WindowState.WindowFullScreen:  # If in Fullscreen, no resize needs to be done
                pass
            else:
                oldHeight = self.height()
                newHeight = self.MainFrame.height() + self.errorFrame.height()
                self.resizeMainWindowHeight(oldHeight, newHeight)

    def infotoggle(self,checked):
        self.fileselectButtontext.setVisible(checked)
        self.modelselectButtontext.setVisible(checked)
        self.playButtontext.setVisible(checked)
    def openfile(self):
        # Reset Play Button
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        # Open the file in the preferred editor
        QtGui.QDesktopServices.openUrl(QUrl.fromLocalFile(self.file_path))
    def openmodel(self):
        # Reset Play Button
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        # Open the file in the preferred editor
        QtGui.QDesktopServices.openUrl(QUrl.fromLocalFile(self.model_path))

    def furtherhelp(self):
        # TODO: Check for validity of URL
        webbrowser.open("https://geostandards-ch.github.io/doc_refhb24/")

    def interlisselect(self):
        # TODO: Check for validity of URL
        webbrowser.open("https://www.interlis.ch/en")

    def settingsselect(self):
        # Reset Play Button
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        from iligui_settings import ilisettingsgui
        self.settingsUIWindow = ilisettingsgui()
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