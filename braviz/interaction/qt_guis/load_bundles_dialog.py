# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\load_bundles_dialog.ui'
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

class Ui_LoadBundles(object):
    def setupUi(self, LoadBundles):
        LoadBundles.setObjectName(_fromUtf8("LoadBundles"))
        LoadBundles.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(LoadBundles)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.all_bundles_list_view = QtGui.QListView(LoadBundles)
        self.all_bundles_list_view.setObjectName(_fromUtf8("all_bundles_list_view"))
        self.verticalLayout.addWidget(self.all_bundles_list_view)
        self.buttonBox = QtGui.QDialogButtonBox(LoadBundles)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadBundles)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoadBundles.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoadBundles.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadBundles)

    def retranslateUi(self, LoadBundles):
        LoadBundles.setWindowTitle(_translate("LoadBundles", "Select bundles to add", None))

