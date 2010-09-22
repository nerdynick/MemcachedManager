from PyQt4.QtGui import QTreeWidgetItem
from PyQt4.QtCore import QStringList

class Server:
	def __init__(self, name, ip, port):
		self.name = name
		self.ip = ip
		self.port = port
		self.cluster = None
		self.tree = None
		
	def initTreeView(self):
		self.tree = QTreeWidgetItem(self.cluster.treeItem, 
								QStringList(str(self.name) +" ( "+ str(self.ip) +":"+ str(self.port) +" )"))
		
	def save(self):
		return {'name':self.name, 'ip':self.ip, 'port':self.port}
		
	def setCluster(self, cluster):
		self.cluster = cluster
		
	def delete(self):
		if self.cluster.treeItem is not None and self.tree is not None:
			self.cluster.treeItem.removeChild(self.tree)
			
		self.cluster.deleteServer(self)