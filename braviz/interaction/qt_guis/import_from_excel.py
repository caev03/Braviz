# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\import_from_excel.ui'
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

class Ui_import_from_excel(object):
    def setupUi(self, import_from_excel):
        import_from_excel.setObjectName(_fromUtf8("import_from_excel"))
        import_from_excel.resize(926, 705)
        self.verticalLayout = QtGui.QVBoxLayout(import_from_excel)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(import_from_excel)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.select_file_button = QtGui.QPushButton(self.frame)
        self.select_file_button.setObjectName(_fromUtf8("select_file_button"))
        self.gridLayout_2.addWidget(self.select_file_button, 0, 0, 1, 1)
        self.file_name_label = QtGui.QLineEdit(self.frame)
        self.file_name_label.setReadOnly(True)
        self.file_name_label.setObjectName(_fromUtf8("file_name_label"))
        self.gridLayout_2.addWidget(self.file_name_label, 0, 1, 1, 1)
        self.omitExistent = QtGui.QCheckBox(self.frame)
        self.omitExistent.setObjectName(_fromUtf8("omitExistent"))
        self.gridLayout_2.addWidget(self.omitExistent, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.label = QtGui.QLabel(import_from_excel)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtGui.QTableView(import_from_excel)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.frame_2 = QtGui.QFrame(import_from_excel)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(self.frame_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(self.frame_2)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(import_from_excel)
        QtCore.QMetaObject.connectSlotsByName(import_from_excel)

    def retranslateUi(self, import_from_excel):
        import_from_excel.setWindowTitle(_translate("import_from_excel", "Import from excel", None))
        self.select_file_button.setText(_translate("import_from_excel", "Select File", None))
        self.omitExistent.setToolTip(_translate("import_from_excel", "Omit variables whose name appears already in the database", None))
        self.omitExistent.setText(_translate("import_from_excel", "Omit existent", None))
        self.label.setText(_translate("import_from_excel", "Preview:", None))

