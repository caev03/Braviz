# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\add_filter_dialog.ui'
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

class Ui_AddFilterDialog(object):
    def setupUi(self, AddFilterDialog):
        AddFilterDialog.setObjectName(_fromUtf8("AddFilterDialog"))
        AddFilterDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddFilterDialog.resize(1086, 606)
        AddFilterDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        AddFilterDialog.setSizeGripEnabled(True)
        AddFilterDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(AddFilterDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_3 = QtGui.QFrame(AddFilterDialog)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.search_box = QtGui.QLineEdit(self.frame_3)
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.verticalLayout_2.addWidget(self.search_box)
        self.tableView = QtGui.QTableView(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.tableView.verticalHeader().setSortIndicatorShown(False)
        self.tableView.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame = QtGui.QFrame(AddFilterDialog)
        self.frame.setMinimumSize(QtCore.QSize(340, 0))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.var_name = QtGui.QLabel(self.frame)
        self.var_name.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.var_name.setFont(font)
        self.var_name.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.var_name.setObjectName(_fromUtf8("var_name"))
        self.verticalLayout.addWidget(self.var_name)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.var_type_combo = QtGui.QComboBox(self.frame_2)
        self.var_type_combo.setEnabled(False)
        self.var_type_combo.setObjectName(_fromUtf8("var_type_combo"))
        self.var_type_combo.addItem(_fromUtf8(""))
        self.var_type_combo.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.var_type_combo)
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.var_description = QtGui.QPlainTextEdit(self.frame_2)
        self.var_description.setEnabled(False)
        self.var_description.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.var_description.setObjectName(_fromUtf8("var_description"))
        self.verticalLayout_3.addWidget(self.var_description)
        self.details_frame = QtGui.QStackedWidget(self.frame_2)
        self.details_frame.setObjectName(_fromUtf8("details_frame"))
        self.nominal_page = QtGui.QWidget()
        self.nominal_page.setObjectName(_fromUtf8("nominal_page"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.nominal_page)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labels_names_table = QtGui.QTableView(self.nominal_page)
        self.labels_names_table.setObjectName(_fromUtf8("labels_names_table"))
        self.labels_names_table.horizontalHeader().setStretchLastSection(True)
        self.labels_names_table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_3.addWidget(self.labels_names_table)
        self.details_frame.addWidget(self.nominal_page)
        self.real_page = QtGui.QWidget()
        self.real_page.setObjectName(_fromUtf8("real_page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.real_page)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_8 = QtGui.QLabel(self.real_page)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)
        self.operation_combo = QtGui.QComboBox(self.real_page)
        self.operation_combo.setObjectName(_fromUtf8("operation_combo"))
        self.operation_combo.addItem(_fromUtf8(""))
        self.operation_combo.addItem(_fromUtf8(""))
        self.operation_combo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.operation_combo, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.real_page)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.th_spin = QtGui.QDoubleSpinBox(self.real_page)
        self.th_spin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.th_spin.setObjectName(_fromUtf8("th_spin"))
        self.gridLayout_3.addWidget(self.th_spin, 5, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        self.minimum_val = QtGui.QDoubleSpinBox(self.real_page)
        self.minimum_val.setMaximum(9999.0)
        self.minimum_val.setObjectName(_fromUtf8("minimum_val"))
        self.gridLayout_3.addWidget(self.minimum_val, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.real_page)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_6 = QtGui.QLabel(self.real_page)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.maximum_val = QtGui.QDoubleSpinBox(self.real_page)
        self.maximum_val.setMaximum(9999999.0)
        self.maximum_val.setObjectName(_fromUtf8("maximum_val"))
        self.gridLayout_3.addWidget(self.maximum_val, 0, 5, 1, 1)
        self.optimum_val = QtGui.QSpinBox(self.real_page)
        self.optimum_val.setMaximum(100)
        self.optimum_val.setObjectName(_fromUtf8("optimum_val"))
        self.gridLayout_3.addWidget(self.optimum_val, 1, 1, 1, 1)
        self.optimum_real_value = QtGui.QLabel(self.real_page)
        self.optimum_real_value.setObjectName(_fromUtf8("optimum_real_value"))
        self.gridLayout_3.addWidget(self.optimum_real_value, 1, 3, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.real_page)
        self.horizontalSlider.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout_3.addWidget(self.horizontalSlider, 2, 0, 1, 6)
        self.label_7 = QtGui.QLabel(self.real_page)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 91, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.real_page)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 5, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 6, 0, 1, 1)
        self.reset_real_meta = QtGui.QPushButton(self.real_page)
        self.reset_real_meta.setObjectName(_fromUtf8("reset_real_meta"))
        self.gridLayout_3.addWidget(self.reset_real_meta, 3, 0, 1, 6)
        self.details_frame.addWidget(self.real_page)
        self.verticalLayout_3.addWidget(self.details_frame)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.save_button = QtGui.QPushButton(self.frame_4)
        self.save_button.setEnabled(False)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout_2.addWidget(self.save_button)
        self.select_button = QtGui.QPushButton(self.frame_4)
        self.select_button.setEnabled(False)
        self.select_button.setObjectName(_fromUtf8("select_button"))
        self.horizontalLayout_2.addWidget(self.select_button)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        self.plot_frame = QtGui.QFrame(AddFilterDialog)
        self.plot_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.plot_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.plot_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.plot_frame.setObjectName(_fromUtf8("plot_frame"))
        self.horizontalLayout.addWidget(self.plot_frame)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.label_2.setBuddy(self.var_type_combo)
        self.label.setBuddy(self.var_description)
        self.label_4.setBuddy(self.minimum_val)
        self.label_5.setBuddy(self.maximum_val)

        self.retranslateUi(AddFilterDialog)
        self.details_frame.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddFilterDialog)

    def retranslateUi(self, AddFilterDialog):
        AddFilterDialog.setWindowTitle(_translate("AddFilterDialog", "Add Filter", None))
        self.search_box.setPlaceholderText(_translate("AddFilterDialog", "Search", None))
        self.var_name.setText(_translate("AddFilterDialog", "Select Filter Variable", None))
        self.label_2.setText(_translate("AddFilterDialog", "Type :", None))
        self.var_type_combo.setItemText(0, _translate("AddFilterDialog", "Real", None))
        self.var_type_combo.setItemText(1, _translate("AddFilterDialog", "Nominal", None))
        self.label.setText(_translate("AddFilterDialog", "Description :", None))
        self.label_8.setText(_translate("AddFilterDialog", "Operation:", None))
        self.operation_combo.setItemText(0, _translate("AddFilterDialog", ">", None))
        self.operation_combo.setItemText(1, _translate("AddFilterDialog", "<", None))
        self.operation_combo.setItemText(2, _translate("AddFilterDialog", "=", None))
        self.label_4.setToolTip(_translate("AddFilterDialog", "Select the expected minimum value for this variable", None))
        self.label_4.setText(_translate("AddFilterDialog", "Minimum", None))
        self.label_5.setToolTip(_translate("AddFilterDialog", "Select the expected maximum value for this variable", None))
        self.label_5.setText(_translate("AddFilterDialog", "Maximum", None))
        self.label_6.setToolTip(_translate("AddFilterDialog", "Select the optimal value for this value, the value that would be considered \"good\"", None))
        self.label_6.setText(_translate("AddFilterDialog", "Optimum", None))
        self.optimum_val.setSuffix(_translate("AddFilterDialog", "%", None))
        self.optimum_real_value.setText(_translate("AddFilterDialog", "0", None))
        self.label_7.setText(_translate("AddFilterDialog", " = ", None))
        self.label_9.setText(_translate("AddFilterDialog", "Threshold:", None))
        self.reset_real_meta.setText(_translate("AddFilterDialog", "Reset Minimum, Maximum and Optimum", None))
        self.save_button.setText(_translate("AddFilterDialog", "Save", None))
        self.select_button.setText(_translate("AddFilterDialog", "Save and Add Filter", None))

