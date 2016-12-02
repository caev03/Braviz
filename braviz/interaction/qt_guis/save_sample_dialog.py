# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\save_sample_dialog.ui'
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

class Ui_SaveSample(object):
    def setupUi(self, SaveSample):
        SaveSample.setObjectName(_fromUtf8("SaveSample"))
        SaveSample.setWindowModality(QtCore.Qt.ApplicationModal)
        SaveSample.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(SaveSample)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(SaveSample)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.sample_name = QtGui.QLineEdit(self.frame)
        self.sample_name.setObjectName(_fromUtf8("sample_name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sample_name)
        self.sample_description = QtGui.QPlainTextEdit(self.frame)
        self.sample_description.setObjectName(_fromUtf8("sample_description"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sample_description)
        self.sample_contents = QtGui.QPlainTextEdit(self.frame)
        self.sample_contents.setReadOnly(True)
        self.sample_contents.setObjectName(_fromUtf8("sample_contents"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sample_contents)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(SaveSample)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SaveSample)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveSample.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveSample.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveSample)

    def retranslateUi(self, SaveSample):
        SaveSample.setWindowTitle(_translate("SaveSample", "Save sample", None))
        self.label.setText(_translate("SaveSample", "Sample Name:", None))
        self.label_2.setText(_translate("SaveSample", "Sample Description:", None))
        self.label_3.setText(_translate("SaveSample", "Sample Contents:", None))

