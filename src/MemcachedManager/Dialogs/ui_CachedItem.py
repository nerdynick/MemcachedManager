# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CachedItem.ui'
#
# Created: Wed Sep 22 10:30:31 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CacheItem(object):
    def setupUi(self, CacheItem):
        CacheItem.setObjectName("CacheItem")
        CacheItem.resize(311, 437)
        self.verticalLayout = QtGui.QVBoxLayout(CacheItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbEncodings = QtGui.QComboBox(CacheItem)
        self.cbEncodings.setObjectName("cbEncodings")
        self.cbEncodings.addItem("")
        self.cbEncodings.addItem("")
        self.cbEncodings.addItem("")
        self.cbEncodings.addItem("")
        self.verticalLayout.addWidget(self.cbEncodings)
        self.txtCachedValue = QtGui.QPlainTextEdit(CacheItem)
        self.txtCachedValue.setReadOnly(True)
        self.txtCachedValue.setObjectName("txtCachedValue")
        self.verticalLayout.addWidget(self.txtCachedValue)

        self.retranslateUi(CacheItem)
        QtCore.QMetaObject.connectSlotsByName(CacheItem)

    def retranslateUi(self, CacheItem):
        CacheItem.setWindowTitle(QtGui.QApplication.translate("CacheItem", "Cached Item", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEncodings.setItemText(0, QtGui.QApplication.translate("CacheItem", "Raw", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEncodings.setItemText(1, QtGui.QApplication.translate("CacheItem", "PHP Serialized", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEncodings.setItemText(2, QtGui.QApplication.translate("CacheItem", "Python Pickeled", None, QtGui.QApplication.UnicodeUTF8))
        self.cbEncodings.setItemText(3, QtGui.QApplication.translate("CacheItem", "JSON", None, QtGui.QApplication.UnicodeUTF8))

