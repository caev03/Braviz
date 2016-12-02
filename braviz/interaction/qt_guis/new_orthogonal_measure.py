# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\new_orthogonal_measure.ui'
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

class Ui_NewRoi(object):
    def setupUi(self, NewRoi):
        NewRoi.setObjectName(_fromUtf8("NewRoi"))
        NewRoi.setWindowModality(QtCore.Qt.ApplicationModal)
        NewRoi.resize(400, 300)
        NewRoi.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(NewRoi)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(NewRoi)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
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
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.roi_name = QtGui.QLineEdit(self.frame)
        self.roi_name.setObjectName(_fromUtf8("roi_name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.roi_name)
        self.roi_desc = QtGui.QPlainTextEdit(self.frame)
        self.roi_desc.setObjectName(_fromUtf8("roi_desc"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.roi_desc)
        self.roi_space = QtGui.QComboBox(self.frame)
        self.roi_space.setEnabled(False)
        self.roi_space.setObjectName(_fromUtf8("roi_space"))
        self.roi_space.addItem(_fromUtf8(""))
        self.roi_space.addItem(_fromUtf8(""))
        self.roi_space.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.roi_space)
        self.error_msg = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.error_msg.setFont(font)
        self.error_msg.setStyleSheet(_fromUtf8("#error_msg{color: rgb(255, 0, 0);}"))
        self.error_msg.setObjectName(_fromUtf8("error_msg"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.error_msg)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.plane_combo = QtGui.QComboBox(self.frame)
        self.plane_combo.setObjectName(_fromUtf8("plane_combo"))
        self.plane_combo.addItem(_fromUtf8(""))
        self.plane_combo.addItem(_fromUtf8(""))
        self.plane_combo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.plane_combo)
        self.verticalLayout.addWidget(self.frame)
        self.dialogButtonBox = QtGui.QDialogButtonBox(NewRoi)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.dialogButtonBox.setObjectName(_fromUtf8("dialogButtonBox"))
        self.verticalLayout.addWidget(self.dialogButtonBox)
        self.label.setBuddy(self.roi_name)
        self.label_2.setBuddy(self.roi_space)
        self.label_3.setBuddy(self.roi_desc)

        self.retranslateUi(NewRoi)
        self.roi_space.setCurrentIndex(1)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewRoi.accept)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewRoi.reject)
        QtCore.QMetaObject.connectSlotsByName(NewRoi)
        NewRoi.setTabOrder(self.roi_name, self.roi_space)
        NewRoi.setTabOrder(self.roi_space, self.roi_desc)
        NewRoi.setTabOrder(self.roi_desc, self.dialogButtonBox)

    def retranslateUi(self, NewRoi):
        NewRoi.setWindowTitle(_translate("NewRoi", "Create New Orthogonal Measurement", None))
        self.label.setText(_translate("NewRoi", "Measure Name:", None))
        self.label_2.setText(_translate("NewRoi", "Coordinate Space:", None))
        self.label_3.setText(_translate("NewRoi", "Description:", None))
        self.roi_space.setItemText(0, _translate("NewRoi", "Subject", None))
        self.roi_space.setItemText(1, _translate("NewRoi", "Talairach", None))
        self.roi_space.setItemText(2, _translate("NewRoi", "Dartel", None))
        self.error_msg.setText(_translate("NewRoi", "Invalid Name", None))
        self.label_4.setText(_translate("NewRoi", "Plane:", None))
        self.plane_combo.setItemText(0, _translate("NewRoi", "Axial", None))
        self.plane_combo.setItemText(1, _translate("NewRoi", "Coronal", None))
        self.plane_combo.setItemText(2, _translate("NewRoi", "Sagital", None))

