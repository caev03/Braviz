# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\interactions_dialog.ui'
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

class Ui_InteractionsDiealog(object):
    def setupUi(self, InteractionsDiealog):
        InteractionsDiealog.setObjectName(_fromUtf8("InteractionsDiealog"))
        InteractionsDiealog.resize(756, 643)
        self.verticalLayout = QtGui.QVBoxLayout(InteractionsDiealog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(InteractionsDiealog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.reg_view = QtGui.QTableView(InteractionsDiealog)
        self.reg_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.reg_view.setObjectName(_fromUtf8("reg_view"))
        self.reg_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.reg_view)
        self.frame = QtGui.QFrame(InteractionsDiealog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_single_button = QtGui.QPushButton(self.frame)
        self.add_single_button.setObjectName(_fromUtf8("add_single_button"))
        self.horizontalLayout.addWidget(self.add_single_button)
        self.add_all_button = QtGui.QPushButton(self.frame)
        self.add_all_button.setObjectName(_fromUtf8("add_all_button"))
        self.horizontalLayout.addWidget(self.add_all_button)
        self.verticalLayout.addWidget(self.frame)
        self.label_2 = QtGui.QLabel(InteractionsDiealog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.full_view = QtGui.QTableView(InteractionsDiealog)
        self.full_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.full_view.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.full_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.full_view.setObjectName(_fromUtf8("full_view"))
        self.full_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.full_view)

        self.retranslateUi(InteractionsDiealog)
        QtCore.QMetaObject.connectSlotsByName(InteractionsDiealog)

    def retranslateUi(self, InteractionsDiealog):
        InteractionsDiealog.setWindowTitle(_translate("InteractionsDiealog", "Dialog", None))
        self.label.setText(_translate("InteractionsDiealog", "Regressors", None))
        self.add_single_button.setText(_translate("InteractionsDiealog", "Add Single Term", None))
        self.add_all_button.setText(_translate("InteractionsDiealog", "Add all combinations", None))
        self.label_2.setText(_translate("InteractionsDiealog", "Interactions", None))

