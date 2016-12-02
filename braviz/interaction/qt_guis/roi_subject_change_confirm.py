# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\roi_subject_change_confirm.ui'
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

class Ui_RoiConfirmChangeSubject(object):
    def setupUi(self, RoiConfirmChangeSubject):
        RoiConfirmChangeSubject.setObjectName(_fromUtf8("RoiConfirmChangeSubject"))
        RoiConfirmChangeSubject.setWindowModality(QtCore.Qt.ApplicationModal)
        RoiConfirmChangeSubject.resize(400, 300)
        RoiConfirmChangeSubject.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(RoiConfirmChangeSubject)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(RoiConfirmChangeSubject)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(RoiConfirmChangeSubject)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Discard|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(RoiConfirmChangeSubject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RoiConfirmChangeSubject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RoiConfirmChangeSubject.reject)
        QtCore.QMetaObject.connectSlotsByName(RoiConfirmChangeSubject)

    def retranslateUi(self, RoiConfirmChangeSubject):
        RoiConfirmChangeSubject.setWindowTitle(_translate("RoiConfirmChangeSubject", "Sphere Modified", None))
        self.label.setText(_translate("RoiConfirmChangeSubject", "Save changes to the current sphere?", None))

