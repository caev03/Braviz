# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\extrapolate_spheres.ui'
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

class Ui_ExtrapolateSpheres(object):
    def setupUi(self, ExtrapolateSpheres):
        ExtrapolateSpheres.setObjectName(_fromUtf8("ExtrapolateSpheres"))
        ExtrapolateSpheres.setWindowModality(QtCore.Qt.ApplicationModal)
        ExtrapolateSpheres.resize(633, 574)
        ExtrapolateSpheres.setSizeGripEnabled(True)
        ExtrapolateSpheres.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(ExtrapolateSpheres)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(ExtrapolateSpheres)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.formLayout = QtGui.QFormLayout(self.frame_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.origin_combo = QtGui.QComboBox(self.frame_3)
        self.origin_combo.setObjectName(_fromUtf8("origin_combo"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.origin_combo)
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.link_combo = QtGui.QComboBox(self.frame_3)
        self.link_combo.setObjectName(_fromUtf8("link_combo"))
        self.link_combo.addItem(_fromUtf8(""))
        self.link_combo.addItem(_fromUtf8(""))
        self.link_combo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.link_combo)
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.radio_combo = QtGui.QComboBox(self.frame_3)
        self.radio_combo.setObjectName(_fromUtf8("radio_combo"))
        self.radio_combo.addItem(_fromUtf8(""))
        self.radio_combo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.radio_combo)
        self.optimize_radius = QtGui.QSpinBox(self.frame_3)
        self.optimize_radius.setMaximum(20)
        self.optimize_radius.setObjectName(_fromUtf8("optimize_radius"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.optimize_radius)
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout_2.addWidget(self.frame_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.start_button = QtGui.QPushButton(self.frame)
        self.start_button.setDefault(True)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.verticalLayout_2.addWidget(self.start_button)
        self.quit_button = QtGui.QPushButton(self.frame)
        self.quit_button.setObjectName(_fromUtf8("quit_button"))
        self.verticalLayout_2.addWidget(self.quit_button)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(ExtrapolateSpheres)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.tableView = QtGui.QTableView(self.frame_2)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableView)
        self.select_all_button = QtGui.QPushButton(self.frame_2)
        self.select_all_button.setObjectName(_fromUtf8("select_all_button"))
        self.verticalLayout.addWidget(self.select_all_button)
        self.select_empty = QtGui.QPushButton(self.frame_2)
        self.select_empty.setObjectName(_fromUtf8("select_empty"))
        self.verticalLayout.addWidget(self.select_empty)
        self.clear_button = QtGui.QPushButton(self.frame_2)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.verticalLayout.addWidget(self.clear_button)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(ExtrapolateSpheres)
        QtCore.QMetaObject.connectSlotsByName(ExtrapolateSpheres)

    def retranslateUi(self, ExtrapolateSpheres):
        ExtrapolateSpheres.setWindowTitle(_translate("ExtrapolateSpheres", "Extrapolate spheres", None))
        self.label.setText(_translate("ExtrapolateSpheres", "Origin:", None))
        self.label_3.setText(_translate("ExtrapolateSpheres", "Link Space:", None))
        self.link_combo.setItemText(0, _translate("ExtrapolateSpheres", "None", None))
        self.link_combo.setItemText(1, _translate("ExtrapolateSpheres", "Talairach", None))
        self.link_combo.setItemText(2, _translate("ExtrapolateSpheres", "Dartel", None))
        self.label_4.setText(_translate("ExtrapolateSpheres", "Radius:", None))
        self.radio_combo.setItemText(0, _translate("ExtrapolateSpheres", "Keep Constant", None))
        self.radio_combo.setItemText(1, _translate("ExtrapolateSpheres", "Resize", None))
        self.label_5.setText(_translate("ExtrapolateSpheres", "Max Optimization", None))
        self.start_button.setText(_translate("ExtrapolateSpheres", "Start Extrapolation", None))
        self.quit_button.setText(_translate("ExtrapolateSpheres", "Quit Dialog", None))
        self.label_2.setText(_translate("ExtrapolateSpheres", "Destination", None))
        self.select_all_button.setText(_translate("ExtrapolateSpheres", "Select All", None))
        self.select_empty.setText(_translate("ExtrapolateSpheres", "Select Empty", None))
        self.clear_button.setText(_translate("ExtrapolateSpheres", "Clear Selection", None))

