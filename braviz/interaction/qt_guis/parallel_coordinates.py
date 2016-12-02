# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\parallel_coordinates.ui'
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

class Ui_parallel_coordinates(object):
    def setupUi(self, parallel_coordinates):
        parallel_coordinates.setObjectName(_fromUtf8("parallel_coordinates"))
        parallel_coordinates.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/parallel_coords_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        parallel_coordinates.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(parallel_coordinates)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.cathegory_combo = QtGui.QComboBox(self.frame)
        self.cathegory_combo.setObjectName(_fromUtf8("cathegory_combo"))
        self.verticalLayout.addWidget(self.cathegory_combo)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.search_box = QtGui.QLineEdit(self.frame)
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.verticalLayout.addWidget(self.search_box)
        self.vars_list = QtGui.QListView(self.frame)
        self.vars_list.setObjectName(_fromUtf8("vars_list"))
        self.verticalLayout.addWidget(self.vars_list)
        self.clear_button = QtGui.QPushButton(self.frame)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.verticalLayout.addWidget(self.clear_button)
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.url_label = QtGui.QLabel(self.frame_2)
        self.url_label.setTextFormat(QtCore.Qt.RichText)
        self.url_label.setOpenExternalLinks(True)
        self.url_label.setObjectName(_fromUtf8("url_label"))
        self.verticalLayout_2.addWidget(self.url_label)
        self.webView = QtWebKit.QWebView(self.frame_2)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.splitter)
        parallel_coordinates.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(parallel_coordinates)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        parallel_coordinates.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(parallel_coordinates)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        parallel_coordinates.setStatusBar(self.statusbar)
        self.actionSelect_Sample = QtGui.QAction(parallel_coordinates)
        self.actionSelect_Sample.setObjectName(_fromUtf8("actionSelect_Sample"))
        self.menuFile.addAction(self.actionSelect_Sample)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(parallel_coordinates)
        QtCore.QMetaObject.connectSlotsByName(parallel_coordinates)

    def retranslateUi(self, parallel_coordinates):
        parallel_coordinates.setWindowTitle(_translate("parallel_coordinates", "Braviz - Parallel Coordinates", None))
        self.label.setText(_translate("parallel_coordinates", "Cathegories:", None))
        self.label_2.setText(_translate("parallel_coordinates", "Variables:", None))
        self.search_box.setPlaceholderText(_translate("parallel_coordinates", "Search", None))
        self.clear_button.setText(_translate("parallel_coordinates", "Clear", None))
        self.url_label.setText(_translate("parallel_coordinates", "<a href=\"http://127.0.0.1:8100\">click</a>", None))
        self.menuFile.setTitle(_translate("parallel_coordinates", "File", None))
        self.actionSelect_Sample.setText(_translate("parallel_coordinates", "Select Sample", None))

from PyQt4 import QtWebKit
import resources_rc
