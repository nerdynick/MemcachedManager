# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Preferences.ui'
#
# Created: Sun Dec  5 13:55:17 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PrefWindow(object):
    def setupUi(self, PrefWindow):
        PrefWindow.setObjectName("PrefWindow")
        PrefWindow.resize(577, 510)
        self.verticalLayout = QtGui.QVBoxLayout(PrefWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbMain = QtGui.QTabWidget(PrefWindow)
        self.tbMain.setObjectName("tbMain")
        self.StatsTB = QtGui.QWidget()
        self.StatsTB.setObjectName("StatsTB")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.StatsTB)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gbLiveStats = QtGui.QGroupBox(self.StatsTB)
        self.gbLiveStats.setObjectName("gbLiveStats")
        self.gridLayout = QtGui.QGridLayout(self.gbLiveStats)
        self.gridLayout.setObjectName("gridLayout")
        self.lblRefreshLiveInterval = QtGui.QLabel(self.gbLiveStats)
        self.lblRefreshLiveInterval.setObjectName("lblRefreshLiveInterval")
        self.gridLayout.addWidget(self.lblRefreshLiveInterval, 0, 0, 1, 1)
        self.txtRefreshLiveStats = QtGui.QLineEdit(self.gbLiveStats)
        self.txtRefreshLiveStats.setObjectName("txtRefreshLiveStats")
        self.gridLayout.addWidget(self.txtRefreshLiveStats, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.gbLiveStats)
        self.gbServerStats = QtGui.QGroupBox(self.StatsTB)
        self.gbServerStats.setObjectName("gbServerStats")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.gbServerStats)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.gbServerStats)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -222, 493, 498))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbPID = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbPID.setChecked(True)
        self.cbPID.setObjectName("cbPID")
        self.gridLayout_2.addWidget(self.cbPID, 0, 0, 1, 1)
        self.cbStarted = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbStarted.setChecked(True)
        self.cbStarted.setObjectName("cbStarted")
        self.gridLayout_2.addWidget(self.cbStarted, 0, 1, 1, 1)
        self.cbUptime = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbUptime.setChecked(True)
        self.cbUptime.setObjectName("cbUptime")
        self.gridLayout_2.addWidget(self.cbUptime, 0, 2, 1, 1)
        self.cbPointerSize = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbPointerSize.setChecked(True)
        self.cbPointerSize.setObjectName("cbPointerSize")
        self.gridLayout_2.addWidget(self.cbPointerSize, 1, 0, 1, 1)
        self.cbThreads = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbThreads.setChecked(True)
        self.cbThreads.setObjectName("cbThreads")
        self.gridLayout_2.addWidget(self.cbThreads, 1, 1, 1, 1)
        self.cbTotalItems = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbTotalItems.setChecked(True)
        self.cbTotalItems.setObjectName("cbTotalItems")
        self.gridLayout_2.addWidget(self.cbTotalItems, 5, 0, 1, 1)
        self.cbTotalConnections = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbTotalConnections.setChecked(True)
        self.cbTotalConnections.setObjectName("cbTotalConnections")
        self.gridLayout_2.addWidget(self.cbTotalConnections, 6, 0, 1, 1)
        self.cbFlushes = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbFlushes.setChecked(True)
        self.cbFlushes.setObjectName("cbFlushes")
        self.gridLayout_2.addWidget(self.cbFlushes, 7, 0, 1, 1)
        self.cbNetIn = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbNetIn.setChecked(True)
        self.cbNetIn.setObjectName("cbNetIn")
        self.gridLayout_2.addWidget(self.cbNetIn, 8, 0, 1, 1)
        self.cbCurrentItems = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbCurrentItems.setChecked(True)
        self.cbCurrentItems.setObjectName("cbCurrentItems")
        self.gridLayout_2.addWidget(self.cbCurrentItems, 5, 1, 1, 1)
        self.cbEvictions = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbEvictions.setChecked(True)
        self.cbEvictions.setObjectName("cbEvictions")
        self.gridLayout_2.addWidget(self.cbEvictions, 7, 1, 1, 1)
        self.cbNetOut = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbNetOut.setChecked(True)
        self.cbNetOut.setObjectName("cbNetOut")
        self.gridLayout_2.addWidget(self.cbNetOut, 8, 1, 1, 1)
        self.cbTotalSpace = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbTotalSpace.setChecked(True)
        self.cbTotalSpace.setObjectName("cbTotalSpace")
        self.gridLayout_2.addWidget(self.cbTotalSpace, 9, 0, 1, 1)
        self.cbFreeSpace = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbFreeSpace.setChecked(True)
        self.cbFreeSpace.setObjectName("cbFreeSpace")
        self.gridLayout_2.addWidget(self.cbFreeSpace, 9, 1, 1, 1)
        self.cbUsedSpace = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbUsedSpace.setChecked(True)
        self.cbUsedSpace.setObjectName("cbUsedSpace")
        self.gridLayout_2.addWidget(self.cbUsedSpace, 9, 2, 1, 1)
        self.cbRequests = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbRequests.setChecked(True)
        self.cbRequests.setObjectName("cbRequests")
        self.gridLayout_2.addWidget(self.cbRequests, 10, 0, 1, 1)
        self.cbGetHits = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbGetHits.setChecked(True)
        self.cbGetHits.setObjectName("cbGetHits")
        self.gridLayout_2.addWidget(self.cbGetHits, 11, 0, 1, 1)
        self.cbDeleteHits = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbDeleteHits.setChecked(True)
        self.cbDeleteHits.setObjectName("cbDeleteHits")
        self.gridLayout_2.addWidget(self.cbDeleteHits, 12, 0, 1, 1)
        self.cbIncrHits = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbIncrHits.setChecked(True)
        self.cbIncrHits.setObjectName("cbIncrHits")
        self.gridLayout_2.addWidget(self.cbIncrHits, 13, 0, 1, 1)
        self.cbGets = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbGets.setChecked(True)
        self.cbGets.setObjectName("cbGets")
        self.gridLayout_2.addWidget(self.cbGets, 10, 1, 1, 1)
        self.cbSets = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbSets.setChecked(True)
        self.cbSets.setObjectName("cbSets")
        self.gridLayout_2.addWidget(self.cbSets, 10, 2, 1, 1)
        self.cbGetMisses = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbGetMisses.setChecked(True)
        self.cbGetMisses.setObjectName("cbGetMisses")
        self.gridLayout_2.addWidget(self.cbGetMisses, 11, 1, 1, 1)
        self.cbDeleteMisses = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbDeleteMisses.setChecked(True)
        self.cbDeleteMisses.setObjectName("cbDeleteMisses")
        self.gridLayout_2.addWidget(self.cbDeleteMisses, 12, 1, 1, 1)
        self.cbIncrMisses = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbIncrMisses.setChecked(True)
        self.cbIncrMisses.setObjectName("cbIncrMisses")
        self.gridLayout_2.addWidget(self.cbIncrMisses, 13, 1, 1, 1)
        self.cbDecrHits = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbDecrHits.setChecked(True)
        self.cbDecrHits.setObjectName("cbDecrHits")
        self.gridLayout_2.addWidget(self.cbDecrHits, 14, 0, 1, 1)
        self.cbCASHits = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbCASHits.setChecked(True)
        self.cbCASHits.setObjectName("cbCASHits")
        self.gridLayout_2.addWidget(self.cbCASHits, 15, 0, 1, 1)
        self.cbDecrMisses = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbDecrMisses.setChecked(True)
        self.cbDecrMisses.setObjectName("cbDecrMisses")
        self.gridLayout_2.addWidget(self.cbDecrMisses, 14, 1, 1, 1)
        self.cbCASMisses = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbCASMisses.setChecked(True)
        self.cbCASMisses.setObjectName("cbCASMisses")
        self.gridLayout_2.addWidget(self.cbCASMisses, 15, 1, 1, 1)
        self.cbCPUUser = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbCPUUser.setChecked(True)
        self.cbCPUUser.setObjectName("cbCPUUser")
        self.gridLayout_2.addWidget(self.cbCPUUser, 2, 0, 1, 1)
        self.cbCPUSystem = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbCPUSystem.setChecked(True)
        self.cbCPUSystem.setObjectName("cbCPUSystem")
        self.gridLayout_2.addWidget(self.cbCPUSystem, 2, 1, 1, 1)
        self.cbAcceptingConnections = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbAcceptingConnections.setChecked(True)
        self.cbAcceptingConnections.setObjectName("cbAcceptingConnections")
        self.gridLayout_2.addWidget(self.cbAcceptingConnections, 3, 1, 1, 1)
        self.cbConnectionStructs = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbConnectionStructs.setChecked(True)
        self.cbConnectionStructs.setObjectName("cbConnectionStructs")
        self.gridLayout_2.addWidget(self.cbConnectionStructs, 3, 0, 1, 1)
        self.cbListenDisabled = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbListenDisabled.setChecked(True)
        self.cbListenDisabled.setObjectName("cbListenDisabled")
        self.gridLayout_2.addWidget(self.cbListenDisabled, 4, 0, 1, 1)
        self.cbRequestRate = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbRequestRate.setChecked(True)
        self.cbRequestRate.setObjectName("cbRequestRate")
        self.gridLayout_2.addWidget(self.cbRequestRate, 16, 0, 1, 1)
        self.cbGetRate = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbGetRate.setChecked(True)
        self.cbGetRate.setObjectName("cbGetRate")
        self.gridLayout_2.addWidget(self.cbGetRate, 17, 0, 1, 1)
        self.cbHitRate = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbHitRate.setChecked(True)
        self.cbHitRate.setObjectName("cbHitRate")
        self.gridLayout_2.addWidget(self.cbHitRate, 16, 1, 1, 1)
        self.cbMissRate = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbMissRate.setChecked(True)
        self.cbMissRate.setObjectName("cbMissRate")
        self.gridLayout_2.addWidget(self.cbMissRate, 16, 2, 1, 1)
        self.cbSetRate = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbSetRate.setChecked(True)
        self.cbSetRate.setObjectName("cbSetRate")
        self.gridLayout_2.addWidget(self.cbSetRate, 17, 1, 1, 1)
        self.cbEvictionRate = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbEvictionRate.setChecked(True)
        self.cbEvictionRate.setObjectName("cbEvictionRate")
        self.gridLayout_2.addWidget(self.cbEvictionRate, 17, 2, 1, 1)
        self.cbConnections = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbConnections.setChecked(True)
        self.cbConnections.setObjectName("cbConnections")
        self.gridLayout_2.addWidget(self.cbConnections, 6, 1, 1, 1)
        self.cbConnectionYield = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbConnectionYield.setChecked(True)
        self.cbConnectionYield.setObjectName("cbConnectionYield")
        self.gridLayout_2.addWidget(self.cbConnectionYield, 3, 2, 1, 1)
        self.cbCASBadval = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbCASBadval.setChecked(True)
        self.cbCASBadval.setObjectName("cbCASBadval")
        self.gridLayout_2.addWidget(self.cbCASBadval, 15, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_4.addWidget(self.gbServerStats)
        self.cbAutoRefresh = QtGui.QCheckBox(self.StatsTB)
        self.cbAutoRefresh.setObjectName("cbAutoRefresh")
        self.verticalLayout_4.addWidget(self.cbAutoRefresh)
        self.tbMain.addTab(self.StatsTB, "")
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
        self.tbMain.setCurrentIndex(0)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), PrefWindow.close)
        QtCore.QMetaObject.connectSlotsByName(PrefWindow)

    def retranslateUi(self, PrefWindow):
        PrefWindow.setWindowTitle(QtGui.QApplication.translate("PrefWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.gbLiveStats.setTitle(QtGui.QApplication.translate("PrefWindow", "Live Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRefreshLiveInterval.setText(QtGui.QApplication.translate("PrefWindow", "Refresh Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.gbServerStats.setTitle(QtGui.QApplication.translate("PrefWindow", "Server Stats to Show", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPID.setText(QtGui.QApplication.translate("PrefWindow", "PID", None, QtGui.QApplication.UnicodeUTF8))
        self.cbStarted.setText(QtGui.QApplication.translate("PrefWindow", "Date Started", None, QtGui.QApplication.UnicodeUTF8))
        self.cbUptime.setText(QtGui.QApplication.translate("PrefWindow", "Uptime", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPointerSize.setText(QtGui.QApplication.translate("PrefWindow", "Pointer Size", None, QtGui.QApplication.UnicodeUTF8))
        self.cbThreads.setText(QtGui.QApplication.translate("PrefWindow", "Threads", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTotalItems.setText(QtGui.QApplication.translate("PrefWindow", "Total Items", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTotalConnections.setText(QtGui.QApplication.translate("PrefWindow", "Total Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFlushes.setText(QtGui.QApplication.translate("PrefWindow", "Flushes", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNetIn.setText(QtGui.QApplication.translate("PrefWindow", "Net In", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCurrentItems.setText(QtGui.QApplication.translate("PrefWindow", "Current Items", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEvictions.setText(QtGui.QApplication.translate("PrefWindow", "Evictions", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNetOut.setText(QtGui.QApplication.translate("PrefWindow", "Net Out", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTotalSpace.setText(QtGui.QApplication.translate("PrefWindow", "Total Space", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFreeSpace.setText(QtGui.QApplication.translate("PrefWindow", "Free Space", None, QtGui.QApplication.UnicodeUTF8))
        self.cbUsedSpace.setText(QtGui.QApplication.translate("PrefWindow", "Used Space", None, QtGui.QApplication.UnicodeUTF8))
        self.cbRequests.setText(QtGui.QApplication.translate("PrefWindow", "Total Requests", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGetHits.setText(QtGui.QApplication.translate("PrefWindow", "Get Hits", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDeleteHits.setText(QtGui.QApplication.translate("PrefWindow", "Delete Hits", None, QtGui.QApplication.UnicodeUTF8))
        self.cbIncrHits.setText(QtGui.QApplication.translate("PrefWindow", "Incr Hits", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGets.setText(QtGui.QApplication.translate("PrefWindow", "Total Gets", None, QtGui.QApplication.UnicodeUTF8))
        self.cbSets.setText(QtGui.QApplication.translate("PrefWindow", "Total Sets", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGetMisses.setText(QtGui.QApplication.translate("PrefWindow", "Get Misses", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDeleteMisses.setText(QtGui.QApplication.translate("PrefWindow", "Delete Misses", None, QtGui.QApplication.UnicodeUTF8))
        self.cbIncrMisses.setText(QtGui.QApplication.translate("PrefWindow", "Incr Misses", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDecrHits.setText(QtGui.QApplication.translate("PrefWindow", "Decr Hits", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCASHits.setText(QtGui.QApplication.translate("PrefWindow", "CAS Hits", None, QtGui.QApplication.UnicodeUTF8))
        self.cbDecrMisses.setText(QtGui.QApplication.translate("PrefWindow", "Decr Misses", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCASMisses.setText(QtGui.QApplication.translate("PrefWindow", "CAS Misses", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCPUUser.setText(QtGui.QApplication.translate("PrefWindow", "CPU User Time", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCPUSystem.setText(QtGui.QApplication.translate("PrefWindow", "CPU System Time", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAcceptingConnections.setText(QtGui.QApplication.translate("PrefWindow", "Accepting Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.cbConnectionStructs.setText(QtGui.QApplication.translate("PrefWindow", "Connection Structures", None, QtGui.QApplication.UnicodeUTF8))
        self.cbListenDisabled.setText(QtGui.QApplication.translate("PrefWindow", "Listen Disabled Num", None, QtGui.QApplication.UnicodeUTF8))
        self.cbRequestRate.setText(QtGui.QApplication.translate("PrefWindow", "Request Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGetRate.setText(QtGui.QApplication.translate("PrefWindow", "Get Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.cbHitRate.setText(QtGui.QApplication.translate("PrefWindow", "Hit Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMissRate.setText(QtGui.QApplication.translate("PrefWindow", "Miss Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.cbSetRate.setText(QtGui.QApplication.translate("PrefWindow", "Set Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEvictionRate.setText(QtGui.QApplication.translate("PrefWindow", "Eviction Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.cbConnections.setText(QtGui.QApplication.translate("PrefWindow", "Current Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.cbConnectionYield.setText(QtGui.QApplication.translate("PrefWindow", "Connection Yields", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCASBadval.setText(QtGui.QApplication.translate("PrefWindow", "CAS Badval", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoRefresh.setText(QtGui.QApplication.translate("PrefWindow", "Auto Refresh Stats on Tab Change", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMain.setTabText(self.tbMain.indexOf(self.StatsTB), QtGui.QApplication.translate("PrefWindow", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPieGraphColors.setText(QtGui.QApplication.translate("PrefWindow", "Pie Graph Colors:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtPieColors.setHtml(QtGui.QApplication.translate("PrefWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHitMissesColor.setText(QtGui.QApplication.translate("PrefWindow", "Hit & Misses Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGetsSetsColor.setText(QtGui.QApplication.translate("PrefWindow", "Gets & Sets Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMain.setTabText(self.tbMain.indexOf(self.GraphTab), QtGui.QApplication.translate("PrefWindow", "Graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("PrefWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("PrefWindow", "Save Settings", None, QtGui.QApplication.UnicodeUTF8))

