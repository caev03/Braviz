# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\load_logic_bundle.ui'
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

class Ui_LoadLogicDialog(object):
    def setupUi(self, LoadLogicDialog):
        LoadLogicDialog.setObjectName(_fromUtf8("LoadLogicDialog"))
        LoadLogicDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        LoadLogicDialog.resize(611, 443)
        LoadLogicDialog.setSizeGripEnabled(True)
        LoadLogicDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(LoadLogicDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(LoadLogicDialog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listView = QtGui.QListView(self.frame)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionRectVisible(True)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.treeView = QtGui.QTreeView(self.frame)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.header().setVisible(False)
        self.gridLayout.addWidget(self.treeView, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(LoadLogicDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadLogicDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoadLogicDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoadLogicDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadLogicDialog)

    def retranslateUi(self, LoadLogicDialog):
        LoadLogicDialog.setWindowTitle(_translate("LoadLogicDialog", "Load Logic Bundle", None))
        self.label.setText(_translate("LoadLogicDialog", "Select Bundle:", None))
        self.label_2.setText(_translate("LoadLogicDialog", "Preview", None))

