# Form implementation generated from reading ui file 'c:\Users\mauri\Repos\GitHub\iligui\dialog_modelselect_old.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_modelselectDialog(object):
    def setupUi(self, modelselectDialog):
        modelselectDialog.setObjectName("modelselectDialog")
        modelselectDialog.resize(455, 359)
        modelselectDialog.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"QRadioButton::indicator:checked, QCheckBox::indicator:checked {\n"
"    image: url(icons/check-circle-green.svg);\n"
"}\n"
"QRadioButton::indicator:unchecked, QCheckBox::indicator:unchecked {\n"
"    image: url(icons/circle.svg);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(modelselectDialog)
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QLabel(parent=modelselectDialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_2.addWidget(self.Title)
        self.transferfileSourceFrame = QtWidgets.QFrame(parent=modelselectDialog)
        self.transferfileSourceFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.transferfileSourceFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.transferfileSourceFrame.setObjectName("transferfileSourceFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.transferfileSourceFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.transferfileRadiobutton = QtWidgets.QRadioButton(parent=self.transferfileSourceFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transferfileRadiobutton.sizePolicy().hasHeightForWidth())
        self.transferfileRadiobutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.transferfileRadiobutton.setFont(font)
        self.transferfileRadiobutton.setStyleSheet("")
        self.transferfileRadiobutton.setCheckable(True)
        self.transferfileRadiobutton.setChecked(True)
        self.transferfileRadiobutton.setObjectName("transferfileRadiobutton")
        self.radioButtonGroup = QtWidgets.QButtonGroup(modelselectDialog)
        self.radioButtonGroup.setObjectName("radioButtonGroup")
        self.radioButtonGroup.addButton(self.transferfileRadiobutton)
        self.verticalLayout_3.addWidget(self.transferfileRadiobutton)
        self.transferfileButtonFrame = QtWidgets.QFrame(parent=self.transferfileSourceFrame)
        self.transferfileButtonFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.transferfileButtonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.transferfileButtonFrame.setObjectName("transferfileButtonFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.transferfileButtonFrame)
        self.horizontalLayout_10.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.transferfileButton = QtWidgets.QPushButton(parent=self.transferfileButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.transferfileButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.transferfileButton.setIcon(icon)
        self.transferfileButton.setObjectName("transferfileButton")
        self.horizontalLayout_10.addWidget(self.transferfileButton)
        self.verticalLayout_3.addWidget(self.transferfileButtonFrame)
        self.verticalLayout_2.addWidget(self.transferfileSourceFrame)
        self.onlineSourceFrame = QtWidgets.QFrame(parent=modelselectDialog)
        self.onlineSourceFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.onlineSourceFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.onlineSourceFrame.setObjectName("onlineSourceFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.onlineSourceFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.onlinesearchRadiobutton = QtWidgets.QRadioButton(parent=self.onlineSourceFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onlinesearchRadiobutton.sizePolicy().hasHeightForWidth())
        self.onlinesearchRadiobutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.onlinesearchRadiobutton.setFont(font)
        self.onlinesearchRadiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}")
        self.onlinesearchRadiobutton.setIconSize(QtCore.QSize(20, 20))
        self.onlinesearchRadiobutton.setChecked(False)
        self.onlinesearchRadiobutton.setObjectName("onlinesearchRadiobutton")
        self.radioButtonGroup.addButton(self.onlinesearchRadiobutton)
        self.verticalLayout.addWidget(self.onlinesearchRadiobutton)
        self.onlinesearchButtonFrame = QtWidgets.QFrame(parent=self.onlineSourceFrame)
        self.onlinesearchButtonFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.onlinesearchButtonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.onlinesearchButtonFrame.setObjectName("onlinesearchButtonFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.onlinesearchButtonFrame)
        self.horizontalLayout_11.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.onlinesearchButton = QtWidgets.QPushButton(parent=self.onlinesearchButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.onlinesearchButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.onlinesearchButton.setIcon(icon1)
        self.onlinesearchButton.setObjectName("onlinesearchButton")
        self.horizontalLayout_11.addWidget(self.onlinesearchButton)
        self.verticalLayout.addWidget(self.onlinesearchButtonFrame)
        self.verticalLayout_2.addWidget(self.onlineSourceFrame)
        self.localSourceFrame = QtWidgets.QFrame(parent=modelselectDialog)
        self.localSourceFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.localSourceFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.localSourceFrame.setObjectName("localSourceFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.localSourceFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.localsearchRadiobutton = QtWidgets.QRadioButton(parent=self.localSourceFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.localsearchRadiobutton.setFont(font)
        self.localsearchRadiobutton.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}")
        self.localsearchRadiobutton.setObjectName("localsearchRadiobutton")
        self.radioButtonGroup.addButton(self.localsearchRadiobutton)
        self.verticalLayout_4.addWidget(self.localsearchRadiobutton)
        self.localsearchButtonFrame = QtWidgets.QFrame(parent=self.localSourceFrame)
        self.localsearchButtonFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.localsearchButtonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.localsearchButtonFrame.setObjectName("localsearchButtonFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.localsearchButtonFrame)
        self.horizontalLayout_12.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.localsearchButton = QtWidgets.QPushButton(parent=self.localsearchButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.localsearchButton.setFont(font)
        self.localsearchButton.setIcon(icon1)
        self.localsearchButton.setObjectName("localsearchButton")
        self.horizontalLayout_12.addWidget(self.localsearchButton)
        self.verticalLayout_4.addWidget(self.localsearchButtonFrame)
        self.verticalLayout_2.addWidget(self.localSourceFrame)
        self.line = QtWidgets.QFrame(parent=modelselectDialog)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.subtitleFrame = QtWidgets.QFrame(parent=modelselectDialog)
        self.subtitleFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.subtitleFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.subtitleFrame.setObjectName("subtitleFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.subtitleFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.subtitle = QtWidgets.QLabel(parent=self.subtitleFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.horizontalLayout_4.addWidget(self.subtitle)
        self.verticalLayout_2.addWidget(self.subtitleFrame)
        self.modelNameFrame = QtWidgets.QFrame(parent=modelselectDialog)
        font = QtGui.QFont()
        font.setItalic(False)
        self.modelNameFrame.setFont(font)
        self.modelNameFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.modelNameFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.modelNameFrame.setObjectName("modelNameFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.modelNameFrame)
        self.horizontalLayout.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.modelName_title = QtWidgets.QLabel(parent=self.modelNameFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.modelName_title.setFont(font)
        self.modelName_title.setObjectName("modelName_title")
        self.horizontalLayout.addWidget(self.modelName_title)
        self.modelName_icon = QtWidgets.QLabel(parent=self.modelNameFrame)
        self.modelName_icon.setText("")
        self.modelName_icon.setPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/chevron-right.svg"))
        self.modelName_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.modelName_icon.setObjectName("modelName_icon")
        self.horizontalLayout.addWidget(self.modelName_icon)
        self.modelName_text = QtWidgets.QLabel(parent=self.modelNameFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelName_text.sizePolicy().hasHeightForWidth())
        self.modelName_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.modelName_text.setFont(font)
        self.modelName_text.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.modelName_text.setScaledContents(False)
        self.modelName_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modelName_text.setWordWrap(True)
        self.modelName_text.setIndent(0)
        self.modelName_text.setOpenExternalLinks(True)
        self.modelName_text.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.modelName_text.setObjectName("modelName_text")
        self.horizontalLayout.addWidget(self.modelName_text)
        self.verticalLayout_2.addWidget(self.modelNameFrame)
        self.modelParthFrame = QtWidgets.QFrame(parent=modelselectDialog)
        self.modelParthFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.modelParthFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.modelParthFrame.setObjectName("modelParthFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.modelParthFrame)
        self.horizontalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.modelPath_title = QtWidgets.QLabel(parent=self.modelParthFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.modelPath_title.setFont(font)
        self.modelPath_title.setObjectName("modelPath_title")
        self.horizontalLayout_2.addWidget(self.modelPath_title)
        self.modelPath_icon = QtWidgets.QLabel(parent=self.modelParthFrame)
        self.modelPath_icon.setText("")
        self.modelPath_icon.setPixmap(QtGui.QPixmap("c:\\Users\\mauri\\Repos\\GitHub\\iligui\\icons/chevron-right.svg"))
        self.modelPath_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.modelPath_icon.setObjectName("modelPath_icon")
        self.horizontalLayout_2.addWidget(self.modelPath_icon)
        self.modelPath_text = QtWidgets.QLabel(parent=self.modelParthFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelPath_text.sizePolicy().hasHeightForWidth())
        self.modelPath_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.modelPath_text.setFont(font)
        self.modelPath_text.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.modelPath_text.setScaledContents(False)
        self.modelPath_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modelPath_text.setWordWrap(True)
        self.modelPath_text.setIndent(0)
        self.modelPath_text.setOpenExternalLinks(True)
        self.modelPath_text.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.modelPath_text.setObjectName("modelPath_text")
        self.horizontalLayout_2.addWidget(self.modelPath_text)
        self.verticalLayout_2.addWidget(self.modelParthFrame)
        self.okButton = QtWidgets.QPushButton(parent=modelselectDialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.verticalLayout_2.addWidget(self.okButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(modelselectDialog)
        QtCore.QMetaObject.connectSlotsByName(modelselectDialog)

    def retranslateUi(self, modelselectDialog):
        _translate = QtCore.QCoreApplication.translate
        modelselectDialog.setWindowTitle(_translate("modelselectDialog", "Dialog"))
        self.Title.setText(_translate("modelselectDialog", "Choose Search Type and Select a Model"))
        self.transferfileRadiobutton.setText(_translate("modelselectDialog", "Automatically search for Model"))
        self.transferfileButton.setText(_translate("modelselectDialog", "Edit Model Declaration in Transfer-File"))
        self.onlinesearchRadiobutton.setText(_translate("modelselectDialog", "from Online Source"))
        self.onlinesearchButton.setText(_translate("modelselectDialog", "Select Models with INTERLIS Model Browser Tool"))
        self.localsearchRadiobutton.setText(_translate("modelselectDialog", "from Local Source"))
        self.localsearchButton.setText(_translate("modelselectDialog", "Select Models on Local Disk"))
        self.subtitle.setText(_translate("modelselectDialog", "Currently Selected Model"))
        self.modelName_title.setText(_translate("modelselectDialog", "Selected Model Name"))
        self.modelName_text.setToolTip(_translate("modelselectDialog", "<html><head/><body><p>The Error returned by the Validator. The direct Position will be delivered if possible.</p><p>Click on the Error to open your INTERLIS Transfer-File with your preferred editor for XML Files. </p></body></html>"))
        self.modelName_text.setText(_translate("modelselectDialog", "Not found or selected"))
        self.modelPath_title.setText(_translate("modelselectDialog", "Selected Model URL/Path"))
        self.modelPath_text.setToolTip(_translate("modelselectDialog", "<html><head/><body><p>The Error returned by the Validator. The direct Position will be delivered if possible.</p><p>Click on the Error to open your INTERLIS Transfer-File with your preferred editor for XML Files. </p></body></html>"))
        self.modelPath_text.setText(_translate("modelselectDialog", "Not found or selected"))
        self.okButton.setText(_translate("modelselectDialog", "OK"))
