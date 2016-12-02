# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\load_scenario_dialog.ui'
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

class Ui_LoadScenarioDialog(object):
    def setupUi(self, LoadScenarioDialog):
        LoadScenarioDialog.setObjectName(_fromUtf8("LoadScenarioDialog"))
        LoadScenarioDialog.resize(836, 479)
        LoadScenarioDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(LoadScenarioDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(LoadScenarioDialog)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scenarios_table = QtGui.QTableView(self.frame)
        self.scenarios_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.scenarios_table.setAlternatingRowColors(True)
        self.scenarios_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.scenarios_table.setSortingEnabled(True)
        self.scenarios_table.setObjectName(_fromUtf8("scenarios_table"))
        self.scenarios_table.horizontalHeader().setStretchLastSection(True)
        self.scenarios_table.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.scenarios_table)
        self.screen_shot_label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen_shot_label.sizePolicy().hasHeightForWidth())
        self.screen_shot_label.setSizePolicy(sizePolicy)
        self.screen_shot_label.setMinimumSize(QtCore.QSize(300, 0))
        self.screen_shot_label.setMaximumSize(QtCore.QSize(300, 16777215))
        self.screen_shot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_shot_label.setObjectName(_fromUtf8("screen_shot_label"))
        self.horizontalLayout.addWidget(self.screen_shot_label)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(LoadScenarioDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadScenarioDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoadScenarioDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoadScenarioDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadScenarioDialog)

    def retranslateUi(self, LoadScenarioDialog):
        LoadScenarioDialog.setWindowTitle(_translate("LoadScenarioDialog", "Load Scenario", None))
        self.screen_shot_label.setText(_translate("LoadScenarioDialog", "Screenshot", None))

