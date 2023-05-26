# Form implementation generated from reading ui file 'c:\Users\mauri\Repos\GitHub\iligui\dialog_modelselectonline.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_modelselectDialog(object):
    def setupUi(self, modelselectDialog):
        modelselectDialog.setObjectName("modelselectDialog")
        modelselectDialog.resize(318, 190)
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
        self.verticalLayout_2.addWidget(self.Title, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame = QtWidgets.QFrame(parent=modelselectDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.transferfileRadiobutton = QtWidgets.QRadioButton(parent=self.frame)
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
        self.verticalLayout.addWidget(self.transferfileRadiobutton)
        self.localsearchRadiobutton = QtWidgets.QRadioButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localsearchRadiobutton.sizePolicy().hasHeightForWidth())
        self.localsearchRadiobutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.localsearchRadiobutton.setFont(font)
        self.localsearchRadiobutton.setObjectName("localsearchRadiobutton")
        self.radioButtonGroup.addButton(self.localsearchRadiobutton)
        self.verticalLayout.addWidget(self.localsearchRadiobutton)
        self.onlinesearchRadiobutton = QtWidgets.QRadioButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onlinesearchRadiobutton.sizePolicy().hasHeightForWidth())
        self.onlinesearchRadiobutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.onlinesearchRadiobutton.setFont(font)
        self.onlinesearchRadiobutton.setIconSize(QtCore.QSize(20, 20))
        self.onlinesearchRadiobutton.setChecked(False)
        self.onlinesearchRadiobutton.setObjectName("onlinesearchRadiobutton")
        self.radioButtonGroup.addButton(self.onlinesearchRadiobutton)
        self.verticalLayout.addWidget(self.onlinesearchRadiobutton)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
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
        self.Title.setText(_translate("modelselectDialog", "Select a Model"))
        self.transferfileRadiobutton.setText(_translate("modelselectDialog", "Automatically from Transfer-File"))
        self.localsearchRadiobutton.setText(_translate("modelselectDialog", "Manually from Local Source"))
        self.onlinesearchRadiobutton.setText(_translate("modelselectDialog", "Manually from Online Source"))
        self.okButton.setText(_translate("modelselectDialog", "OK"))
