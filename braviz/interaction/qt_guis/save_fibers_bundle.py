# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\save_fibers_bundle.ui'
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

class Ui_SaveBundleDialog(object):
    def setupUi(self, SaveBundleDialog):
        SaveBundleDialog.setObjectName(_fromUtf8("SaveBundleDialog"))
        SaveBundleDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(SaveBundleDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(SaveBundleDialog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.error_message = QtGui.QLabel(self.frame)
        self.error_message.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.error_message.setObjectName(_fromUtf8("error_message"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.error_message)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.operation_label = QtGui.QLabel(self.frame)
        self.operation_label.setObjectName(_fromUtf8("operation_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.operation_label)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.structures_list = QtGui.QPlainTextEdit(self.frame)
        self.structures_list.setEnabled(True)
        self.structures_list.setReadOnly(True)
        self.structures_list.setObjectName(_fromUtf8("structures_list"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.structures_list)
        self.save_succesful = QtGui.QLabel(self.frame)
        self.save_succesful.setObjectName(_fromUtf8("save_succesful"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.save_succesful)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(SaveBundleDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(SaveBundleDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveBundleDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveBundleDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(SaveBundleDialog)

    def retranslateUi(self, SaveBundleDialog):
        SaveBundleDialog.setWindowTitle(_translate("SaveBundleDialog", "Save Bundle", None))
        self.label.setText(_translate("SaveBundleDialog", "Bundle Name: ", None))
        self.error_message.setText(_translate("SaveBundleDialog", "Error", None))
        self.label_2.setText(_translate("SaveBundleDialog", "Operation: ", None))
        self.operation_label.setText(_translate("SaveBundleDialog", "<or/and>", None))
        self.label_3.setText(_translate("SaveBundleDialog", "Structures:", None))
        self.save_succesful.setText(_translate("SaveBundleDialog", "Save Succesful", None))

