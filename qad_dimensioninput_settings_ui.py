# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qad_dimensioninput_settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DimInput_Settings_Dialog(object):
    def setupUi(self, DimInput_Settings_Dialog):
        DimInput_Settings_Dialog.setObjectName("DimInput_Settings_Dialog")
        DimInput_Settings_Dialog.resize(363, 346)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DimInput_Settings_Dialog.sizePolicy().hasHeightForWidth())
        DimInput_Settings_Dialog.setSizePolicy(sizePolicy)
        DimInput_Settings_Dialog.setMinimumSize(QtCore.QSize(363, 346))
        DimInput_Settings_Dialog.setMaximumSize(QtCore.QSize(363, 346))
        self.layoutWidget = QtWidgets.QWidget(DimInput_Settings_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 310, 251, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QPushButton(self.layoutWidget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.helpButton = QtWidgets.QPushButton(self.layoutWidget)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout.addWidget(self.helpButton)
        self.groupBox = QtWidgets.QGroupBox(DimInput_Settings_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 291))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.label.setObjectName("label")
        self.radioShow1Dim = QtWidgets.QRadioButton(self.groupBox)
        self.radioShow1Dim.setGeometry(QtCore.QRect(10, 50, 311, 17))
        self.radioShow1Dim.setObjectName("radioShow1Dim")
        self.radioShow2Dim = QtWidgets.QRadioButton(self.groupBox)
        self.radioShow2Dim.setGeometry(QtCore.QRect(10, 80, 311, 17))
        self.radioShow2Dim.setObjectName("radioShow2Dim")
        self.radioShowMoreDim = QtWidgets.QRadioButton(self.groupBox)
        self.radioShowMoreDim.setGeometry(QtCore.QRect(10, 110, 311, 17))
        self.radioShowMoreDim.setObjectName("radioShowMoreDim")
        self.checkAbsoluteAngle = QtWidgets.QCheckBox(self.groupBox)
        self.checkAbsoluteAngle.setGeometry(QtCore.QRect(30, 200, 151, 17))
        self.checkAbsoluteAngle.setObjectName("checkAbsoluteAngle")
        self.checkResultingDim = QtWidgets.QCheckBox(self.groupBox)
        self.checkResultingDim.setGeometry(QtCore.QRect(30, 140, 151, 17))
        self.checkResultingDim.setObjectName("checkResultingDim")
        self.checkLengthChange = QtWidgets.QCheckBox(self.groupBox)
        self.checkLengthChange.setGeometry(QtCore.QRect(30, 170, 151, 17))
        self.checkLengthChange.setObjectName("checkLengthChange")
        self.checkAngleChange = QtWidgets.QCheckBox(self.groupBox)
        self.checkAngleChange.setGeometry(QtCore.QRect(190, 140, 141, 17))
        self.checkAngleChange.setObjectName("checkAngleChange")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 281, 41))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/plugins/qad/icons/lamp_on.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DimInput_Settings_Dialog)
        self.radioShowMoreDim.clicked.connect(DimInput_Settings_Dialog.radioShowMoreDimChecked)
        self.cancelButton.clicked.connect(DimInput_Settings_Dialog.reject)
        self.okButton.clicked.connect(DimInput_Settings_Dialog.ButtonBOX_Accepted)
        self.helpButton.clicked.connect(DimInput_Settings_Dialog.ButtonHELP_Pressed)
        self.radioShow2Dim.clicked.connect(DimInput_Settings_Dialog.radioShow2DimChecked)
        self.radioShow1Dim.clicked.connect(DimInput_Settings_Dialog.radioShow1DimChecked)
        QtCore.QMetaObject.connectSlotsByName(DimInput_Settings_Dialog)

    def retranslateUi(self, DimInput_Settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        DimInput_Settings_Dialog.setWindowTitle(_translate("DimInput_Settings_Dialog", "QAD - Dimension Input Settings"))
        self.okButton.setText(_translate("DimInput_Settings_Dialog", "OK"))
        self.cancelButton.setText(_translate("DimInput_Settings_Dialog", "Cancel"))
        self.helpButton.setText(_translate("DimInput_Settings_Dialog", "?"))
        self.groupBox.setTitle(_translate("DimInput_Settings_Dialog", "Visibility"))
        self.label.setText(_translate("DimInput_Settings_Dialog", "When grip-stretching:"))
        self.radioShow1Dim.setToolTip(_translate("DimInput_Settings_Dialog", "Displays only the length change dimensional input tooltip when you are using grip editing to stretch an object. (DYNDIVIS system variable)"))
        self.radioShow1Dim.setText(_translate("DimInput_Settings_Dialog", "Show only 1 dimension input field at a time"))
        self.radioShow2Dim.setToolTip(_translate("DimInput_Settings_Dialog", "Displays the length change and resulting dimensional input tooltips when you are using grip editing to stretch an object. (DYNDIVIS system variable)"))
        self.radioShow2Dim.setText(_translate("DimInput_Settings_Dialog", "Show 2 dimension input fields at a time"))
        self.radioShowMoreDim.setToolTip(_translate("DimInput_Settings_Dialog", "When you are using grip editing to stretch an object, displays the dimensional input tooltips that are selected below. (DYNDIVIS and DYNDIGRIP system variables)"))
        self.radioShowMoreDim.setText(_translate("DimInput_Settings_Dialog", "Show the following dimension input fields simultaneously:"))
        self.checkAbsoluteAngle.setToolTip(_translate("DimInput_Settings_Dialog", "Displays an angle dimensional tooltip that is updated as you move the grip."))
        self.checkAbsoluteAngle.setText(_translate("DimInput_Settings_Dialog", "Absolute angle"))
        self.checkResultingDim.setToolTip(_translate("DimInput_Settings_Dialog", "Displays a length dimensional tooltip that is updated as you move the grip."))
        self.checkResultingDim.setText(_translate("DimInput_Settings_Dialog", "Resulting dimension"))
        self.checkLengthChange.setToolTip(_translate("DimInput_Settings_Dialog", "Displays the change in length as you move the grip."))
        self.checkLengthChange.setText(_translate("DimInput_Settings_Dialog", "Length change"))
        self.checkAngleChange.setToolTip(_translate("DimInput_Settings_Dialog", "Displays the change in the angle as you move the grip."))
        self.checkAngleChange.setText(_translate("DimInput_Settings_Dialog", "Angle change"))
        self.label_2.setText(_translate("DimInput_Settings_Dialog", "Press TAB to switch to the next dimension input field"))

