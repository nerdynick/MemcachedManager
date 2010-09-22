# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Preferences.ui'
#
# Created: Wed Sep 22 10:30:31 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PrefWindow(object):
    def setupUi(self, PrefWindow):
        PrefWindow.setObjectName("PrefWindow")
        PrefWindow.resize(422, 300)
        self.verticalLayout = QtGui.QVBoxLayout(PrefWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbMain = QtGui.QTabWidget(PrefWindow)
        self.tbMain.setObjectName("tbMain")
        self.GraphTab = QtGui.QWidget()
        self.GraphTab.setObjectName("GraphTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.GraphTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblPieGraphColors = QtGui.QLabel(self.GraphTab)
        self.lblPieGraphColors.setObjectName("lblPieGraphColors")
        self.verticalLayout_2.addWidget(self.lblPieGraphColors)
        self.txtPieColors = QtGui.QTextEdit(self.GraphTab)
        self.txtPieColors.setObjectName("txtPieColors")
        self.verticalLayout_2.addWidget(self.txtPieColors)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblHitMissesColor = QtGui.QLabel(self.GraphTab)
        self.lblHitMissesColor.setObjectName("lblHitMissesColor")
        self.verticalLayout_3.addWidget(self.lblHitMissesColor)
        self.txtHitMissesColor = QtGui.QLineEdit(self.GraphTab)
        self.txtHitMissesColor.setMinimumSize(QtCore.QSize(100, 0))
        self.txtHitMissesColor.setObjectName("txtHitMissesColor")
        self.verticalLayout_3.addWidget(self.txtHitMissesColor)
        self.lblGetsSetsColor = QtGui.QLabel(self.GraphTab)
        self.lblGetsSetsColor.setObjectName("lblGetsSetsColor")
        self.verticalLayout_3.addWidget(self.lblGetsSetsColor)
        self.txtGetsSetsColor = QtGui.QLineEdit(self.GraphTab)
        self.txtGetsSetsColor.setMinimumSize(QtCore.QSize(100, 0))
        self.txtGetsSetsColor.setObjectName("txtGetsSetsColor")
        self.verticalLayout_3.addWidget(self.txtGetsSetsColor)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tbMain.addTab(self.GraphTab, "")
        self.StatsTB = QtGui.QWidget()
        self.StatsTB.setObjectName("StatsTB")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.StatsTB)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblRefreshLiveInterval = QtGui.QLabel(self.StatsTB)
        self.lblRefreshLiveInterval.setObjectName("lblRefreshLiveInterval")
        self.gridLayout.addWidget(self.lblRefreshLiveInterval, 0, 0, 1, 1)
        self.txtRefreshLiveStats = QtGui.QLineEdit(self.StatsTB)
        self.txtRefreshLiveStats.setObjectName("txtRefreshLiveStats")
        self.gridLayout.addWidget(self.txtRefreshLiveStats, 0, 1, 1, 1)
        self.cbAutoRefresh = QtGui.QCheckBox(self.StatsTB)
        self.cbAutoRefresh.setObjectName("cbAutoRefresh")
        self.gridLayout.addWidget(self.cbAutoRefresh, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tbMain.addTab(self.StatsTB, "")
        self.verticalLayout.addWidget(self.tbMain)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnCancel = QtGui.QPushButton(PrefWindow)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_2.addWidget(self.btnCancel)
        self.btnSave = QtGui.QPushButton(PrefWindow)
        self.btnSave.setDefault(True)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PrefWindow)
        self.tbMain.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), PrefWindow.close)
        QtCore.QMetaObject.connectSlotsByName(PrefWindow)

    def retranslateUi(self, PrefWindow):
        PrefWindow.setWindowTitle(QtGui.QApplication.translate("PrefWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPieGraphColors.setText(QtGui.QApplication.translate("PrefWindow", "Pie Graph Colors:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtPieColors.setHtml(QtGui.QApplication.translate("PrefWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHitMissesColor.setText(QtGui.QApplication.translate("PrefWindow", "Hit & Misses Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGetsSetsColor.setText(QtGui.QApplication.translate("PrefWindow", "Gets & Sets Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMain.setTabText(self.tbMain.indexOf(self.GraphTab), QtGui.QApplication.translate("PrefWindow", "Graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRefreshLiveInterval.setText(QtGui.QApplication.translate("PrefWindow", "Refresh Live Stats Interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoRefresh.setText(QtGui.QApplication.translate("PrefWindow", "Auto Refresh on Tab Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMain.setTabText(self.tbMain.indexOf(self.StatsTB), QtGui.QApplication.translate("PrefWindow", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("PrefWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("PrefWindow", "Save Settings", None, QtGui.QApplication.UnicodeUTF8))

