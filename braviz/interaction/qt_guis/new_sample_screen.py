# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\new_sample_screen.ui'
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

class Ui_NewSampleWindow(object):
    def setupUi(self, NewSampleWindow):
        NewSampleWindow.setObjectName(_fromUtf8("NewSampleWindow"))
        NewSampleWindow.resize(921, 600)
        self.centralwidget = QtGui.QWidget(NewSampleWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_5 = QtGui.QFrame(self.frame)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.formLayout = QtGui.QFormLayout(self.frame_5)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.frame_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBox = QtGui.QComboBox(self.frame_5)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout.addWidget(self.frame_5)
        self.add_filter_button = QtGui.QPushButton(self.frame)
        self.add_filter_button.setObjectName(_fromUtf8("add_filter_button"))
        self.verticalLayout.addWidget(self.add_filter_button)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.filters = QtGui.QListView(self.frame)
        self.filters.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.filters.setObjectName(_fromUtf8("filters"))
        self.verticalLayout.addWidget(self.filters)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.working_set_view = QtGui.QListView(self.frame)
        self.working_set_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.working_set_view.setObjectName(_fromUtf8("working_set_view"))
        self.verticalLayout.addWidget(self.working_set_view)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.undo_button = QtGui.QPushButton(self.frame_2)
        self.undo_button.setEnabled(False)
        self.undo_button.setObjectName(_fromUtf8("undo_button"))
        self.verticalLayout_3.addWidget(self.undo_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.add_all_button = QtGui.QPushButton(self.frame_2)
        self.add_all_button.setObjectName(_fromUtf8("add_all_button"))
        self.verticalLayout_3.addWidget(self.add_all_button)
        self.add_subset_button = QtGui.QPushButton(self.frame_2)
        self.add_subset_button.setObjectName(_fromUtf8("add_subset_button"))
        self.verticalLayout_3.addWidget(self.add_subset_button)
        self.remove_button = QtGui.QPushButton(self.frame_2)
        self.remove_button.setObjectName(_fromUtf8("remove_button"))
        self.verticalLayout_3.addWidget(self.remove_button)
        self.intersect_button = QtGui.QPushButton(self.frame_2)
        self.intersect_button.setObjectName(_fromUtf8("intersect_button"))
        self.verticalLayout_3.addWidget(self.intersect_button)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.clear_button = QtGui.QPushButton(self.frame_2)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.verticalLayout_3.addWidget(self.clear_button)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.setStretch(0, 9)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(7, 1)
        self.verticalLayout_3.setStretch(9, 9)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.current_view = QtGui.QListView(self.frame_3)
        self.current_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.current_view.setObjectName(_fromUtf8("current_view"))
        self.verticalLayout_2.addWidget(self.current_view)
        self.size_label = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.size_label.setFont(font)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setObjectName(_fromUtf8("size_label"))
        self.verticalLayout_2.addWidget(self.size_label)
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.description = QtGui.QPlainTextEdit(self.frame_3)
        self.description.setObjectName(_fromUtf8("description"))
        self.verticalLayout_2.addWidget(self.description)
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout = QtGui.QGridLayout(self.frame_4)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.save_button = QtGui.QPushButton(self.frame_4)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.gridLayout.addWidget(self.save_button, 1, 0, 1, 1)
        self.load_button = QtGui.QPushButton(self.frame_4)
        self.load_button.setObjectName(_fromUtf8("load_button"))
        self.gridLayout.addWidget(self.load_button, 2, 0, 1, 1)
        self.create_ind_variable = QtGui.QPushButton(self.frame_4)
        self.create_ind_variable.setObjectName(_fromUtf8("create_ind_variable"))
        self.gridLayout.addWidget(self.create_ind_variable, 1, 5, 1, 1)
        self.cancel_button = QtGui.QPushButton(self.frame_4)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.gridLayout.addWidget(self.cancel_button, 2, 5, 1, 1)
        self.send_to_all = QtGui.QPushButton(self.frame_4)
        self.send_to_all.setObjectName(_fromUtf8("send_to_all"))
        self.gridLayout.addWidget(self.send_to_all, 2, 1, 1, 1)
        self.set_in_parent = QtGui.QPushButton(self.frame_4)
        self.set_in_parent.setObjectName(_fromUtf8("set_in_parent"))
        self.gridLayout.addWidget(self.set_in_parent, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(4, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 4)
        NewSampleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(NewSampleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        NewSampleWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(NewSampleWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        NewSampleWindow.setStatusBar(self.statusbar)
        self.label_5.setBuddy(self.comboBox)

        self.retranslateUi(NewSampleWindow)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), NewSampleWindow.close)
        QtCore.QMetaObject.connectSlotsByName(NewSampleWindow)

    def retranslateUi(self, NewSampleWindow):
        NewSampleWindow.setWindowTitle(_translate("NewSampleWindow", "Create Sample", None))
        self.label_5.setText(_translate("NewSampleWindow", "Base Sample:", None))
        self.comboBox.setItemText(0, _translate("NewSampleWindow", "<All>", None))
        self.add_filter_button.setText(_translate("NewSampleWindow", "Add Filter", None))
        self.label_4.setText(_translate("NewSampleWindow", "Filters:", None))
        self.filters.setToolTip(_translate("NewSampleWindow", "Right click to remove filters", None))
        self.label.setText(_translate("NewSampleWindow", "Working Set:", None))
        self.working_set_view.setToolTip(_translate("NewSampleWindow", "Right click to add subjects to current sample", None))
        self.undo_button.setToolTip(_translate("NewSampleWindow", "Undo last operation", None))
        self.undo_button.setText(_translate("NewSampleWindow", "Undo", None))
        self.add_all_button.setToolTip(_translate("NewSampleWindow", "Add subjects in workingset to sample", None))
        self.add_all_button.setText(_translate("NewSampleWindow", "Add All", None))
        self.add_subset_button.setToolTip(_translate("NewSampleWindow", "Add a random subset of the working set to the current sample", None))
        self.add_subset_button.setText(_translate("NewSampleWindow", "Add Subset", None))
        self.remove_button.setToolTip(_translate("NewSampleWindow", "Remove subject in working set from sample", None))
        self.remove_button.setText(_translate("NewSampleWindow", "Subtract", None))
        self.intersect_button.setToolTip(_translate("NewSampleWindow", "Keep in sample ONLY subject which are also in the working set", None))
        self.intersect_button.setText(_translate("NewSampleWindow", "Intersect", None))
        self.clear_button.setText(_translate("NewSampleWindow", "Clear", None))
        self.label_2.setText(_translate("NewSampleWindow", "Current Sample:", None))
        self.current_view.setToolTip(_translate("NewSampleWindow", "Right click to remove subjects", None))
        self.size_label.setText(_translate("NewSampleWindow", "Size : ", None))
        self.label_3.setText(_translate("NewSampleWindow", "Sample Description:", None))
        self.save_button.setText(_translate("NewSampleWindow", "Save", None))
        self.load_button.setText(_translate("NewSampleWindow", "Load", None))
        self.create_ind_variable.setText(_translate("NewSampleWindow", "Create indicator variable", None))
        self.cancel_button.setText(_translate("NewSampleWindow", "Cancel", None))
        self.send_to_all.setToolTip(_translate("NewSampleWindow", "Send the current sample to all opened applications", None))
        self.send_to_all.setText(_translate("NewSampleWindow", "Send to All", None))
        self.set_in_parent.setToolTip(_translate("NewSampleWindow", "Set the current sample in the application", None))
        self.set_in_parent.setText(_translate("NewSampleWindow", "Set in application", None))
