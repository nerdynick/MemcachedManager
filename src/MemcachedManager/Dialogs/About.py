'''
Created on Apr 8, 2009

@author: nick
'''
from PyQt4 import QtGui
from MemcachedManager.Dialogs.ui_About import Ui_dialogAbout

class About(QtGui.QDialog, Ui_dialogAbout):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)