# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\braviz\braviz\interaction\qt_guis\menu2_light_mac.ui'
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

class Ui_BavizMenu(object):
    def setupUi(self, BavizMenu):
        BavizMenu.setObjectName(_fromUtf8("BavizMenu"))
        BavizMenu.resize(771, 567)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BavizMenu.sizePolicy().hasHeightForWidth())
        BavizMenu.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gridLayout_aligntop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        BavizMenu.setWindowIcon(icon)
        BavizMenu.setStyleSheet(_fromUtf8("QWidget#centralwidget{\n"
"background-image: url(:/icons/imagine2.svg);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom right;\n"
"background-origin: content;\n"
"}\n"
"QToolButton:hover{\n"
" font: bold;\n"
"}"))
        BavizMenu.setIconSize(QtCore.QSize(100, 100))
        BavizMenu.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(BavizMenu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(51, 0, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.help_button = QtGui.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/help-browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.help_button.setIcon(icon1)
        self.help_button.setIconSize(QtCore.QSize(40, 25))
        self.help_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.help_button.setObjectName(_fromUtf8("help_button"))
        self.horizontalLayout.addWidget(self.help_button)
        self.verticalLayout.addWidget(self.frame)
        self.groupBox_2 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.subject_overview = QtGui.QToolButton(self.groupBox_2)
        self.subject_overview.setMinimumSize(QtCore.QSize(90, 90))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/some_fibers.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.subject_overview.setIcon(icon2)
        self.subject_overview.setIconSize(QtCore.QSize(60, 60))
        self.subject_overview.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.subject_overview.setAutoRaise(False)
        self.subject_overview.setObjectName(_fromUtf8("subject_overview"))
        self.horizontalLayout_5.addWidget(self.subject_overview)
        self.sample_overview = QtGui.QToolButton(self.groupBox_2)
        self.sample_overview.setMinimumSize(QtCore.QSize(90, 90))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sample_overview.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.sample_overview.setIcon(icon3)
        self.sample_overview.setIconSize(QtCore.QSize(60, 60))
        self.sample_overview.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.sample_overview.setAutoRaise(False)
        self.sample_overview.setObjectName(_fromUtf8("sample_overview"))
        self.horizontalLayout_5.addWidget(self.sample_overview)
        self.fmri_explorer = QtGui.QToolButton(self.groupBox_2)
        self.fmri_explorer.setMinimumSize(QtCore.QSize(90, 90))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/fmri_explore_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fmri_explorer.setIcon(icon4)
        self.fmri_explorer.setIconSize(QtCore.QSize(60, 60))
        self.fmri_explorer.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fmri_explorer.setAutoRaise(False)
        self.fmri_explorer.setObjectName(_fromUtf8("fmri_explorer"))
        self.horizontalLayout_5.addWidget(self.fmri_explorer)
        self.check_reg = QtGui.QToolButton(self.groupBox_2)
        self.check_reg.setMinimumSize(QtCore.QSize(90, 90))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/check_reg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_reg.setIcon(icon5)
        self.check_reg.setIconSize(QtCore.QSize(60, 60))
        self.check_reg.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.check_reg.setAutoRaise(False)
        self.check_reg.setObjectName(_fromUtf8("check_reg"))
        self.horizontalLayout_5.addWidget(self.check_reg)
        self.roi_builder = QtGui.QToolButton(self.groupBox_2)
        self.roi_builder.setMinimumSize(QtCore.QSize(90, 90))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/roi_builder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roi_builder.setIcon(icon6)
        self.roi_builder.setIconSize(QtCore.QSize(60, 60))
        self.roi_builder.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.roi_builder.setObjectName(_fromUtf8("roi_builder"))
        self.horizontalLayout_5.addWidget(self.roi_builder)
        self.logic_bundles = QtGui.QToolButton(self.groupBox_2)
        self.logic_bundles.setMinimumSize(QtCore.QSize(90, 90))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/logic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logic_bundles.setIcon(icon7)
        self.logic_bundles.setIconSize(QtCore.QSize(60, 60))
        self.logic_bundles.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logic_bundles.setObjectName(_fromUtf8("logic_bundles"))
        self.horizontalLayout_5.addWidget(self.logic_bundles)
        self.measure_app = QtGui.QToolButton(self.groupBox_2)
        self.measure_app.setMinimumSize(QtCore.QSize(90, 90))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/measure.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.measure_app.setIcon(icon8)
        self.measure_app.setIconSize(QtCore.QSize(60, 60))
        self.measure_app.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.measure_app.setObjectName(_fromUtf8("measure_app"))
        self.horizontalLayout_5.addWidget(self.measure_app)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.anova = QtGui.QToolButton(self.groupBox_3)
        self.anova.setMinimumSize(QtCore.QSize(90, 90))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/baviz_anova.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.anova.setIcon(icon9)
        self.anova.setIconSize(QtCore.QSize(60, 60))
        self.anova.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.anova.setObjectName(_fromUtf8("anova"))
        self.horizontalLayout_2.addWidget(self.anova)
        self.linear_model = QtGui.QToolButton(self.groupBox_3)
        self.linear_model.setEnabled(True)
        self.linear_model.setMinimumSize(QtCore.QSize(90, 90))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/linear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linear_model.setIcon(icon10)
        self.linear_model.setIconSize(QtCore.QSize(60, 60))
        self.linear_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.linear_model.setObjectName(_fromUtf8("linear_model"))
        self.horizontalLayout_2.addWidget(self.linear_model)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.correlations = QtGui.QToolButton(self.groupBox_3)
        self.correlations.setEnabled(True)
        self.correlations.setMinimumSize(QtCore.QSize(90, 90))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/correlations_app.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.correlations.setIcon(icon11)
        self.correlations.setIconSize(QtCore.QSize(60, 60))
        self.correlations.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.correlations.setObjectName(_fromUtf8("correlations"))
        self.horizontalLayout_2.addWidget(self.correlations)
        self.parallel_coordinates = QtGui.QToolButton(self.groupBox_3)
        self.parallel_coordinates.setEnabled(True)
        self.parallel_coordinates.setMinimumSize(QtCore.QSize(90, 90))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/parallel_coords_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.parallel_coordinates.setIcon(icon12)
        self.parallel_coordinates.setIconSize(QtCore.QSize(60, 60))
        self.parallel_coordinates.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.parallel_coordinates.setObjectName(_fromUtf8("parallel_coordinates"))
        self.horizontalLayout_2.addWidget(self.parallel_coordinates)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.variables = QtGui.QToolButton(self.groupBox_4)
        self.variables.setEnabled(True)
        self.variables.setMinimumSize(QtCore.QSize(0, 50))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/listview-highlight.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.variables.setIcon(icon13)
        self.variables.setIconSize(QtCore.QSize(50, 30))
        self.variables.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.variables.setObjectName(_fromUtf8("variables"))
        self.horizontalLayout_4.addWidget(self.variables)
        self.scenarios = QtGui.QToolButton(self.groupBox_4)
        self.scenarios.setEnabled(True)
        self.scenarios.setMinimumSize(QtCore.QSize(0, 50))
        self.scenarios.setIcon(icon)
        self.scenarios.setIconSize(QtCore.QSize(50, 30))
        self.scenarios.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.scenarios.setObjectName(_fromUtf8("scenarios"))
        self.horizontalLayout_4.addWidget(self.scenarios)
        self.samples = QtGui.QToolButton(self.groupBox_4)
        self.samples.setEnabled(True)
        self.samples.setMinimumSize(QtCore.QSize(0, 50))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/kontact_contacts.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.samples.setIcon(icon14)
        self.samples.setIconSize(QtCore.QSize(50, 30))
        self.samples.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.samples.setObjectName(_fromUtf8("samples"))
        self.horizontalLayout_4.addWidget(self.samples)
        self.excel = QtGui.QToolButton(self.groupBox_4)
        self.excel.setEnabled(True)
        self.excel.setMinimumSize(QtCore.QSize(0, 50))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/database_in.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.excel.setIcon(icon15)
        self.excel.setIconSize(QtCore.QSize(50, 30))
        self.excel.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.excel.setObjectName(_fromUtf8("excel"))
        self.horizontalLayout_4.addWidget(self.excel)
        self.export_2 = QtGui.QToolButton(self.groupBox_4)
        self.export_2.setEnabled(True)
        self.export_2.setMinimumSize(QtCore.QSize(0, 50))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/database_out.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.export_2.setIcon(icon16)
        self.export_2.setIconSize(QtCore.QSize(50, 30))
        self.export_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.export_2.setObjectName(_fromUtf8("export_2"))
        self.horizontalLayout_4.addWidget(self.export_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.network_button = QtGui.QToolButton(self.frame_3)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/internet-web-browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.network_button.setIcon(icon17)
        self.network_button.setCheckable(True)
        self.network_button.setChecked(True)
        self.network_button.setObjectName(_fromUtf8("network_button"))
        self.horizontalLayout_3.addWidget(self.network_button)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_2.setStretch(0, 1)
        BavizMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BavizMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BavizMenu.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BavizMenu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BavizMenu.setStatusBar(self.statusbar)

        self.retranslateUi(BavizMenu)
        QtCore.QMetaObject.connectSlotsByName(BavizMenu)

    def retranslateUi(self, BavizMenu):
        BavizMenu.setWindowTitle(_translate("BavizMenu", "Braviz Menu", None))
        self.label.setText(_translate("BavizMenu", "<html><head/><body><p>Welcome to Braviz<br/>Project</p></body></html>", None))
        self.help_button.setToolTip(_translate("BavizMenu", "Display help in a web browser", None))
        self.help_button.setText(_translate("BavizMenu", "Help", None))
        self.groupBox_2.setTitle(_translate("BavizMenu", "Explore Visual Data", None))
        self.subject_overview.setToolTip(_translate("BavizMenu", "See images, segmentation, tractography and cortex of a given subject. \n"
"Export variables to the database", None))
        self.subject_overview.setText(_translate("BavizMenu", "Subject Overview", None))
        self.sample_overview.setToolTip(_translate("BavizMenu", "Compare geometric structures across multiple subjects", None))
        self.sample_overview.setText(_translate("BavizMenu", "Sample Overview", None))
        self.fmri_explorer.setToolTip(_translate("BavizMenu", "Visualize fMRI series", None))
        self.fmri_explorer.setText(_translate("BavizMenu", "Explore fMRI", None))
        self.check_reg.setToolTip(_translate("BavizMenu", "Compare two images", None))
        self.check_reg.setText(_translate("BavizMenu", "Check Registration", None))
        self.roi_builder.setToolTip(_translate("BavizMenu", "Use spheres to select regions of interest", None))
        self.roi_builder.setText(_translate("BavizMenu", "ROI Builder", None))
        self.logic_bundles.setToolTip(_translate("BavizMenu", "Create bundles by combining ROIs and Structures", None))
        self.logic_bundles.setText(_translate("BavizMenu", "Logic Bundles", None))
        self.measure_app.setToolTip(_translate("BavizMenu", "Measure distances in orthogonal planes", None))
        self.measure_app.setText(_translate("BavizMenu", "Measure", None))
        self.groupBox_3.setTitle(_translate("BavizMenu", "Analysis", None))
        self.anova.setToolTip(_translate("BavizMenu", "Perform an Anova statistical analysis using the variables in the database", None))
        self.anova.setText(_translate("BavizMenu", "Anova", None))
        self.linear_model.setToolTip(_translate("BavizMenu", "Fit a linear model with the variables in the database", None))
        self.linear_model.setText(_translate("BavizMenu", "Linear Model", None))
        self.correlations.setToolTip(_translate("BavizMenu", "Find correlations among pairs of variables in the database", None))
        self.correlations.setText(_translate("BavizMenu", "Correlations", None))
        self.parallel_coordinates.setToolTip(_translate("BavizMenu", "Look at several variables in a parallel coordinates display", None))
        self.parallel_coordinates.setText(_translate("BavizMenu", "Parallel Coords", None))
        self.groupBox_4.setTitle(_translate("BavizMenu", "Manage Data", None))
        self.variables.setToolTip(_translate("BavizMenu", "Review the variables in the database", None))
        self.variables.setText(_translate("BavizMenu", "Variables", None))
        self.scenarios.setToolTip(_translate("BavizMenu", "Review the saved scenarios, and load them", None))
        self.scenarios.setText(_translate("BavizMenu", "Scenarios", None))
        self.samples.setToolTip(_translate("BavizMenu", "Review current subsamples and create new subsamples", None))
        self.samples.setText(_translate("BavizMenu", "Subsamples", None))
        self.excel.setToolTip(_translate("BavizMenu", "Import variables from excel", None))
        self.excel.setText(_translate("BavizMenu", "Import", None))
        self.export_2.setToolTip(_translate("BavizMenu", "Export variables to a file", None))
        self.export_2.setText(_translate("BavizMenu", "Export", None))
        self.network_button.setStatusTip(_translate("BavizMenu", "Untoggle to disconnect applications syncrhonization", None))
        self.network_button.setText(_translate("BavizMenu", "...", None))

import resources_rc
