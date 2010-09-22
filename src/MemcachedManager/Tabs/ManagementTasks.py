from PyQt4 import QtCore
from PyQt4 import QtGui

class ManagementTasks:
	def __init__(self):
		self.connect(self.btnDelCacheKeys, QtCore.SIGNAL("clicked()"), self.deleteKeys)
		self.connect(self.btnGetCacheKeys, QtCore.SIGNAL("clicked()"), self.getKeys)
		self.connect(self.btnFlushCache, QtCore.SIGNAL("clicked()"), self.flushServers)
		self.connect(self.btnKeySearch, QtCore.SIGNAL("clicked()"), self.keySearch)
		
	def onFocus(self):
		"""
		Event called by MemcachedManager when this tab gains focus
		"""
		pass
	
	def closeEvent(self):
		pass
	
	def getKeys(self):
		value = self.txtCacheKeys.text()
		if self.currentCluster is not None:
			self.cachedItemDialog.hide()
			self.cachedItemDialog.show()
			self.cachedItemDialog.setCluster(self.currentCluster)
			self.cachedItemDialog.setKeys(value)
		else:
			QtGui.QMessageBox.critical(self, "Not Cluster Selected", "You do not have an Active Cluster")
		
	def deleteKeys(self):
		"""
		Deletes a key(s) from the Current Active Cluster 
		"""
		value = self.txtCacheKeys.text()
		if self.currentCluster is not None:
			self.currentCluster.deleteKey(value)
			QtGui.QMessageBox.information(self, "Key(s) Deleted", "Your key(s) have been deleted")
		else:
			QtGui.QMessageBox.critical(self, "Not Cluster Selected", "You do not have an Active Cluster")
	
	def flushServers(self):
		"""
		Flush all Keys from the Current Active Cluster
		"""
		if self.currentCluster is not None:
			self.currentCluster.flushKeys()
			QtGui.QMessageBox.information(self, "Cache Keys Flushed", "Your keys have been flushed")
		else:
			QtGui.QMessageBox.critical(self, "Not Cluster Selected", "You do not have an Active Cluster")
	
	def keySearch(self):
		"""
		Preform a Key Search
		
		This is still under development
		"""
		#pBar = pbKeySearch
		#RegEx = cbRegEx
		#Text = txtSearchKey
		QtGui.QMessageBox.information(self, "Key Search", "Key Search is currently under development. It is planned for the 0.2 release.")