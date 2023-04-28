from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtWidgets import QLabel, QToolButton, QPlainTextEdit,QProgressBar, QToolBox
from PyQt6 import uic, QtGui
import sys

class iligui(QMainWindow):
    def __init__(self):
        super(iligui, self).__init__()

        # Load UI File
        uic.loadUi("iligui.ui", self)

        # Define our Widgets----------------------------------------------------------------------------------------------
        ## Main Widgets
        self.interlisButton
        self.menuButton
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
        """
        ## Sidebar Widgets
        self.Button_Menu
        # Validation Settings, Config Files, Log Settings, Proxy Access, Plugins
        self.settings = [self.setting1, self.setting2, self.setting3, self.setting4, self.setting5]
        # Frames for each setting
        self.settings_sub = [self.setting1_sub, self.setting2_sub, self.setting3_sub, self.setting4_sub, self.setting5_sub]
        # Validation Settings > Force Type Validation, Disable Area Validation, Disable Constraining Validation, All Objects Accessible
        self.settings1 = [self.setting1_1, self.setting1_2, self.setting1_3, self.setting1_4]
        # Config Files > Set Config File, Set Metaconfig File
        self.settings2 = [self.setting2_1, self.setting2_2]
        # Log Settings > Enable Log Time, Enable Trace Logs, Log Export Location
        self.settins3 = [self.setting3_1, self.setting3_2, self.setting3_3]
        # Proxy Access > Proxy Host Server ex: 192.168.1.100, Proxy Host Port ex: 192.168.1.100
        self.settings4 = [self.setting4_11, self.setting4_12, self.setting4_21, self.setting4_22]
        # Plugins > Plugins folder ex: Directory Path
        self.settings5 = [self.setting5_11, self.setting5_12]
        """
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
        #self.menuButton.clicked.connect()
        self.fileselectButton.clicked.connect(self.fileselect)
        self.modelselectButton.clicked.connect(self.modelselect)
        self.playButton.clicked.connect(self.playselect)
        self.errorButton.clicked.connect(self.errorselect)


        """
        # Validation Settings > Force Type Validation, Disable Area Validation, Disable Constraining Validation, All Objects Accessible
        self.settings1[0].toggled.connect(self.forcevalidation)
        self.settings1[1].toggled.connect(self.areavalidation)
        self.settings1[2].toggled.connect(self.constrainvalidation)
        self.settings1[3].toggled.connect(self.objectaccessibility)
        #-----------------------------------------------------------------------------------------------------------------
        """

        # Ensure Readiness for Java Interoperability----------------------------------------------------------------------
        # Check JRE Installation in Current working directory, if not install in CWD
        import logic_checkjava
        logic_checkjava.checkinstall_cwdjava()
        # Options Bin to pass to command
        self.options = []
        #-----------------------------------------------------------------------------------------------------------------

        # Show the App
        self.show()

    # Methods to Run TODO: SEPERATE FROM THIS FILE AND IMPORT-------------------------------------------------------------
    def fileselect(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        # Open a file dialog and allow the user to select a file
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Transfer-file", "", "Interlis Files (*.itf *.xtf *.xml)")
        if self.file_path != "":
            print("Loaded Transfer File from " + self.file_path)

    def modelselect(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        # Open a file dialog and allow the user to select a file
        self.model_path, _ = QFileDialog.getOpenFileName(None, "Select an Interlis Model-File", "", "Interlis Model (*.ili);")
        print("Loaded Model from " + self.model_path)

    def playselect(self):
        # Use subprocess method to run the Jar file with the selected input options
        import logic_playbutton
        try:
            Options = " ".join(self.options)
            file = self.file_path
            command = Options, file
            textoutput = logic_playbutton.run_ilivalidator(Options, file)
            if "Info: ...validation done" in textoutput:
                self.playButton.setIcon(QtGui.QIcon("icons/circle_good_green.png"))
            else:
                self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
                self.errorFrame.setVisible(True)
                self.errorText.appendPlainText(textoutput)

        except AttributeError as e:
            self.errorFrame.setVisible(True)
            self.errorText.appendPlainText(repr(e))
            self.playButton.setIcon(QtGui.QIcon("icons/circle_bad_red.png"))
            self.errorText.appendPlainText("An XML Transfer-File must be selected!")

    def interlisselect(self):
        import webbrowser
        # TODO: Check for validity of URL
        webbrowser.open("https://github.com/claeis/ilivalidator/blob/master/docs/ilivalidator.rst")

    def errorselect(self):
        self.helpFrame.setVisible(True)
        self.helpText.appendPlainText("Some Help Suggestions")

    """
    # Validation Settings
    def forcevalidation(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        if "--forceTypeValidation" not in self.options:
            self.options.append("--forceTypeValidation")
        else:
            self.options.remove("--forceTypeValidation")
        self.Terminal.appendPlainText(f"Current options: {self.options}")
    def areavalidation(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        if "--disableAreaValidation" not in self.options:
            self.options.append("--disableAreaValidation")
        else:
            self.options.remove("--disableAreaValidation")
        self.Terminal.appendPlainText(f"Current options: {self.options}")
    def constrainvalidation(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        if "--disableConstraintValidation" not in self.options:
            self.options.append("--disableConstraintValidation")
        else:
            self.options.remove("--disableConstraintValidation")
        self.Terminal.appendPlainText(f"Current options: {self.options}")
    def objectaccessibility(self):
        self.playButton.setIcon(QtGui.QIcon("icons/play.png"))
        if "--allObjectsAccessible" not in self.options:
            self.options.append("--allObjectsAccessible")
        else:
            self.options.remove("--allObjectsAccessible")
        self.Terminal.appendPlainText(f"Current options: {self.options}")
    """
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

# Initialize the App
app = QApplication(sys.argv)
UIWindow = iligui()
app.exec()