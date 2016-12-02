# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\export_logic_scalar_into_db.ui'
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

class Ui_ExportScalar(object):
    def setupUi(self, ExportScalar):
        ExportScalar.setObjectName(_fromUtf8("ExportScalar"))
        ExportScalar.setWindowModality(QtCore.Qt.ApplicationModal)
        ExportScalar.resize(430, 381)
        ExportScalar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        ExportScalar.setSizeGripEnabled(True)
        ExportScalar.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(ExportScalar)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(ExportScalar)
        self.frame.setMinimumSize(QtCore.QSize(340, 0))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout = QtGui.QFormLayout(self.frame_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.var_name = QtGui.QLabel(self.frame_2)
        self.var_name.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.var_name.setFont(font)
        self.var_name.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.var_name.setObjectName(_fromUtf8("var_name"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.var_name)
        self.var_name_input = QtGui.QLineEdit(self.frame_2)
        self.var_name_input.setObjectName(_fromUtf8("var_name_input"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.var_name_input)
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label)
        self.var_description = QtGui.QPlainTextEdit(self.frame_2)
        self.var_description.setObjectName(_fromUtf8("var_description"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.var_description)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.metric_label = QtGui.QLineEdit(self.frame_2)
        self.metric_label.setEnabled(False)
        self.metric_label.setReadOnly(True)
        self.metric_label.setObjectName(_fromUtf8("metric_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.metric_label)
        self.error_str = QtGui.QLabel(self.frame_2)
        self.error_str.setStyleSheet(_fromUtf8("\n"
"color: rgb(255, 0, 0);"))
        self.error_str.setObjectName(_fromUtf8("error_str"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.error_str)
        self.verticalLayout.addWidget(self.frame_2)
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.start_button = QtGui.QPushButton(self.frame_4)
        self.start_button.setEnabled(False)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout_2.addWidget(self.start_button)
        self.cancel_button = QtGui.QPushButton(self.frame_4)
        self.cancel_button.setEnabled(True)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        self.var_name.setBuddy(self.var_name_input)
        self.label.setBuddy(self.var_description)
        self.label_2.setBuddy(self.metric_label)

        self.retranslateUi(ExportScalar)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), ExportScalar.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportScalar)

    def retranslateUi(self, ExportScalar):
        ExportScalar.setWindowTitle(_translate("ExportScalar", "Export Scalar into DB", None))
        self.var_name.setText(_translate("ExportScalar", "Variable Name: ", None))
        self.label.setText(_translate("ExportScalar", "Description :", None))
        self.label_2.setText(_translate("ExportScalar", "Scalar:", None))
        self.error_str.setText(_translate("ExportScalar", "Error: Variable name exists", None))
        self.start_button.setText(_translate("ExportScalar", "Start", None))
        self.cancel_button.setText(_translate("ExportScalar", "Cancel", None))

