# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\AddStructuresDialog.ui'
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

class Ui_AddSegmented(object):
    def setupUi(self, AddSegmented):
        AddSegmented.setObjectName(_fromUtf8("AddSegmented"))
        AddSegmented.setWindowModality(QtCore.Qt.ApplicationModal)
        AddSegmented.resize(400, 300)
        AddSegmented.setSizeGripEnabled(True)
        AddSegmented.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(AddSegmented)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AddSegmented)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.treeView = QtGui.QTreeView(AddSegmented)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeView)
        self.dialogButtonBox = QtGui.QDialogButtonBox(AddSegmented)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName(_fromUtf8("dialogButtonBox"))
        self.verticalLayout.addWidget(self.dialogButtonBox)

        self.retranslateUi(AddSegmented)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddSegmented.accept)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddSegmented.reject)
        QtCore.QMetaObject.connectSlotsByName(AddSegmented)

    def retranslateUi(self, AddSegmented):
        AddSegmented.setWindowTitle(_translate("AddSegmented", "Add structures", None))
        self.label.setText(_translate("AddSegmented", "Select Structures to Add", None))

