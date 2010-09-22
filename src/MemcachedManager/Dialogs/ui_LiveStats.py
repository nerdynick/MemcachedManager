# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LiveStats.ui'
#
# Created: Wed Sep 22 10:30:31 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_liveStatsDialog(object):
    def setupUi(self, liveStatsDialog):
        liveStatsDialog.setObjectName("liveStatsDialog")
        liveStatsDialog.resize(640, 379)
        self.verticalLayout = QtGui.QVBoxLayout(liveStatsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbvLiveStats = QtGui.QTableView(liveStatsDialog)
        self.tbvLiveStats.setShowGrid(False)
        self.tbvLiveStats.setSortingEnabled(False)
        self.tbvLiveStats.setWordWrap(False)
        self.tbvLiveStats.setObjectName("tbvLiveStats")
        self.tbvLiveStats.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tbvLiveStats)

        self.retranslateUi(liveStatsDialog)
        QtCore.QMetaObject.connectSlotsByName(liveStatsDialog)

    def retranslateUi(self, liveStatsDialog):
        liveStatsDialog.setWindowTitle(QtGui.QApplication.translate("liveStatsDialog", "Live Stats", None, QtGui.QApplication.UnicodeUTF8))

