# Form implementation generated from reading ui file 'c:\Users\mauri\Repos\GitHub\iligui\iligui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/interlis.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_main = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_main.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_input = QtWidgets.QFrame(parent=self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_input.sizePolicy().hasHeightForWidth())
        self.frame_input.setSizePolicy(sizePolicy)
        self.frame_input.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_input.setObjectName("frame_input")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_input)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Fileselect = QtWidgets.QToolButton(parent=self.frame_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Fileselect.sizePolicy().hasHeightForWidth())
        self.Button_Fileselect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.Button_Fileselect.setFont(font)
        self.Button_Fileselect.setAcceptDrops(True)
        self.Button_Fileselect.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/fileupload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Fileselect.setIcon(icon1)
        self.Button_Fileselect.setIconSize(QtCore.QSize(100, 100))
        self.Button_Fileselect.setAutoRepeat(False)
        self.Button_Fileselect.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Button_Fileselect.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.Button_Fileselect.setAutoRaise(True)
        self.Button_Fileselect.setObjectName("Button_Fileselect")
        self.horizontalLayout.addWidget(self.Button_Fileselect)
        self.Button_Modelselect = QtWidgets.QToolButton(parent=self.frame_input)
        self.Button_Modelselect.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Modelselect.sizePolicy().hasHeightForWidth())
        self.Button_Modelselect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Modelselect.setFont(font)
        self.Button_Modelselect.setAcceptDrops(True)
        self.Button_Modelselect.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/model.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Modelselect.setIcon(icon2)
        self.Button_Modelselect.setIconSize(QtCore.QSize(100, 100))
        self.Button_Modelselect.setCheckable(False)
        self.Button_Modelselect.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.Button_Modelselect.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.Button_Modelselect.setAutoRaise(True)
        self.Button_Modelselect.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.Button_Modelselect.setObjectName("Button_Modelselect")
        self.horizontalLayout.addWidget(self.Button_Modelselect)
        self.gridLayout.addWidget(self.frame_input, 1, 1, 1, 1)
        self.frame_settings = QtWidgets.QFrame(parent=self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_settings.sizePolicy().hasHeightForWidth())
        self.frame_settings.setSizePolicy(sizePolicy)
        self.frame_settings.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings.setObjectName("frame_settings")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_settings)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Button_Menu = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Menu.sizePolicy().hasHeightForWidth())
        self.Button_Menu.setSizePolicy(sizePolicy)
        self.Button_Menu.setMinimumSize(QtCore.QSize(60, 60))
        self.Button_Menu.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Menu.setIcon(icon3)
        self.Button_Menu.setIconSize(QtCore.QSize(60, 60))
        self.Button_Menu.setFlat(True)
        self.Button_Menu.setObjectName("Button_Menu")
        self.verticalLayout_7.addWidget(self.Button_Menu)
        self.Setting01 = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Setting01.sizePolicy().hasHeightForWidth())
        self.Setting01.setSizePolicy(sizePolicy)
        self.Setting01.setMinimumSize(QtCore.QSize(128, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/tool.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Setting01.setIcon(icon4)
        self.Setting01.setFlat(False)
        self.Setting01.setObjectName("Setting01")
        self.verticalLayout_7.addWidget(self.Setting01)
        self.Setting02 = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Setting02.sizePolicy().hasHeightForWidth())
        self.Setting02.setSizePolicy(sizePolicy)
        self.Setting02.setMinimumSize(QtCore.QSize(128, 0))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Setting02.setIcon(icon5)
        self.Setting02.setFlat(False)
        self.Setting02.setObjectName("Setting02")
        self.verticalLayout_7.addWidget(self.Setting02)
        self.Setting03 = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Setting03.sizePolicy().hasHeightForWidth())
        self.Setting03.setSizePolicy(sizePolicy)
        self.Setting03.setMinimumSize(QtCore.QSize(128, 0))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/archive.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Setting03.setIcon(icon6)
        self.Setting03.setFlat(False)
        self.Setting03.setObjectName("Setting03")
        self.verticalLayout_7.addWidget(self.Setting03)
        self.Setting04 = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Setting04.sizePolicy().hasHeightForWidth())
        self.Setting04.setSizePolicy(sizePolicy)
        self.Setting04.setMinimumSize(QtCore.QSize(128, 0))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/loader.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Setting04.setIcon(icon7)
        self.Setting04.setFlat(False)
        self.Setting04.setObjectName("Setting04")
        self.verticalLayout_7.addWidget(self.Setting04)
        self.Setting05 = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Setting05.sizePolicy().hasHeightForWidth())
        self.Setting05.setSizePolicy(sizePolicy)
        self.Setting05.setMinimumSize(QtCore.QSize(128, 0))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/log-in.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Setting05.setIcon(icon8)
        self.Setting05.setFlat(False)
        self.Setting05.setObjectName("Setting05")
        self.verticalLayout_7.addWidget(self.Setting05)
        self.Setting06 = QtWidgets.QPushButton(parent=self.frame_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Setting06.sizePolicy().hasHeightForWidth())
        self.Setting06.setSizePolicy(sizePolicy)
        self.Setting06.setMinimumSize(QtCore.QSize(128, 0))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Setting06.setIcon(icon9)
        self.Setting06.setFlat(False)
        self.Setting06.setObjectName("Setting06")
        self.verticalLayout_7.addWidget(self.Setting06)
        self.gridLayout.addWidget(self.frame_settings, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_terminal = QtWidgets.QFrame(parent=self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_terminal.sizePolicy().hasHeightForWidth())
        self.frame_terminal.setSizePolicy(sizePolicy)
        self.frame_terminal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_terminal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_terminal.setObjectName("frame_terminal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_terminal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title_Terminal = QtWidgets.QLabel(parent=self.frame_terminal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_Terminal.sizePolicy().hasHeightForWidth())
        self.Title_Terminal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Title_Terminal.setFont(font)
        self.Title_Terminal.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Title_Terminal.setObjectName("Title_Terminal")
        self.verticalLayout.addWidget(self.Title_Terminal)
        self.Terminal = QtWidgets.QPlainTextEdit(parent=self.frame_terminal)
        self.Terminal.setObjectName("Terminal")
        self.verticalLayout.addWidget(self.Terminal)
        self.gridLayout.addWidget(self.frame_terminal, 2, 1, 1, 1)
        self.frame_tool = QtWidgets.QFrame(parent=self.frame_main)
        self.frame_tool.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tool.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tool.setObjectName("frame_tool")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_tool)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Title_Version = QtWidgets.QLabel(parent=self.frame_tool)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Title_Version.setFont(font)
        self.Title_Version.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title_Version.setObjectName("Title_Version")
        self.verticalLayout_6.addWidget(self.Title_Version)
        self.frame = QtWidgets.QFrame(parent=self.frame_tool)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Icon_Interlis = QtWidgets.QToolButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Interlis.sizePolicy().hasHeightForWidth())
        self.Icon_Interlis.setSizePolicy(sizePolicy)
        self.Icon_Interlis.setMinimumSize(QtCore.QSize(80, 80))
        self.Icon_Interlis.setIcon(icon)
        self.Icon_Interlis.setIconSize(QtCore.QSize(80, 80))
        self.Icon_Interlis.setAutoRaise(True)
        self.Icon_Interlis.setObjectName("Icon_Interlis")
        self.horizontalLayout_3.addWidget(self.Icon_Interlis)
        self.Tool_Select = QtWidgets.QComboBox(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tool_Select.sizePolicy().hasHeightForWidth())
        self.Tool_Select.setSizePolicy(sizePolicy)
        self.Tool_Select.setMinimumSize(QtCore.QSize(80, 80))
        self.Tool_Select.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Tool_Select.setEditable(False)
        self.Tool_Select.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.Tool_Select.setIconSize(QtCore.QSize(55, 55))
        self.Tool_Select.setObjectName("Tool_Select")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/validator.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Tool_Select.addItem(icon10, "")
        self.Tool_Select.setItemText(0, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/ili2c.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Tool_Select.addItem(icon11, "")
        self.Tool_Select.setItemText(1, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/ili2db.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Tool_Select.addItem(icon12, "")
        self.Tool_Select.setItemText(2, "")
        self.horizontalLayout_3.addWidget(self.Tool_Select)
        self.verticalLayout_6.addWidget(self.frame)
        self.gridLayout.addWidget(self.frame_tool, 1, 0, 1, 1)
        self.frame_play = QtWidgets.QFrame(parent=self.frame_main)
        self.frame_play.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_play.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_play.setObjectName("frame_play")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_play)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_Play = QtWidgets.QToolButton(parent=self.frame_play)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.Button_Play.setFont(font)
        self.Button_Play.setMouseTracking(False)
        self.Button_Play.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Button_Play.setStyleSheet("QToolButton[objectName^=\"Button_Play\"]:hover {\n"
"    background-color : lightgreen;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Button_Play.setIcon(icon13)
        self.Button_Play.setIconSize(QtCore.QSize(100, 100))
        self.Button_Play.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.Button_Play.setAutoRaise(True)
        self.Button_Play.setObjectName("Button_Play")
        self.horizontalLayout_2.addWidget(self.Button_Play)
        self.gridLayout.addWidget(self.frame_play, 2, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout_5.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Tool_Select.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iligui"))
        self.Button_Fileselect.setToolTip(_translate("MainWindow", "Select or Drop an Interlis1/2 Transfer File you want to check."))
        self.Button_Fileselect.setText(_translate("MainWindow", ".itf / .xtf Transfer-File"))
        self.Button_Modelselect.setToolTip(_translate("MainWindow", "Select or Drop an Interlis Model File with which you want to validate your file"))
        self.Button_Modelselect.setText(_translate("MainWindow", ".ili Data-Model"))
        self.Setting01.setToolTip(_translate("MainWindow", "Select configuration files for a preset"))
        self.Setting01.setText(_translate("MainWindow", "Config Files"))
        self.Setting02.setText(_translate("MainWindow", "Validation Settings"))
        self.Setting03.setText(_translate("MainWindow", "Log Settings"))
        self.Setting04.setText(_translate("MainWindow", "Proxy Access"))
        self.Setting05.setText(_translate("MainWindow", "Plugins"))
        self.Setting06.setText(_translate("MainWindow", "About iligui"))
        self.Title_Terminal.setText(_translate("MainWindow", "Terminal Readout"))
        self.Title_Version.setText(_translate("MainWindow", "iligui Version 0.1"))
        self.Icon_Interlis.setText(_translate("MainWindow", "..."))
        self.Button_Play.setText(_translate("MainWindow", "Validate"))