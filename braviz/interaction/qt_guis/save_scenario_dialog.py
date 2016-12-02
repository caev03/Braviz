# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\save_scenario_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SaveScenarioDialog(object):
    def setupUi(self, SaveScenarioDialog):
        SaveScenarioDialog.setObjectName(_fromUtf8("SaveScenarioDialog"))
        SaveScenarioDialog.resize(400, 300)
        SaveScenarioDialog.setSizeGripEnabled(True)
        SaveScenarioDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SaveScenarioDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(SaveScenarioDialog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.scenario_name = QtGui.QLineEdit(self.frame)
        self.scenario_name.setObjectName(_fromUtf8("scenario_name"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.scenario_name)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.scn_description = QtGui.QPlainTextEdit(self.frame)
        self.scn_description.setObjectName(_fromUtf8("scn_description"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.scn_description)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.app_name = QtGui.QLineEdit(self.frame)
        self.app_name.setEnabled(False)
        self.app_name.setObjectName(_fromUtf8("app_name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.app_name)
        self.verticalLayout.addWidget(self.frame)
        self.succesful_message = QtGui.QLabel(SaveScenarioDialog)
        self.succesful_message.setStyleSheet(_fromUtf8("color: rgb(0, 170, 0);"))
        self.succesful_message.setObjectName(_fromUtf8("succesful_message"))
        self.verticalLayout.addWidget(self.succesful_message)
        self.buttonBox = QtGui.QDialogButtonBox(SaveScenarioDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.scenario_name)
        self.label_2.setBuddy(self.scn_description)
        self.label_3.setBuddy(self.app_name)

        self.retranslateUi(SaveScenarioDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveScenarioDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveScenarioDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveScenarioDialog)

    def retranslateUi(self, SaveScenarioDialog):
        SaveScenarioDialog.setWindowTitle(_translate("SaveScenarioDialog", "Save scenario", None))
        self.label.setText(_translate("SaveScenarioDialog", "Scenario Name:", None))
        self.label_2.setText(_translate("SaveScenarioDialog", "Description:", None))
        self.label_3.setText(_translate("SaveScenarioDialog", "Application: ", None))
        self.succesful_message.setText(_translate("SaveScenarioDialog", "Save Succesful", None))

