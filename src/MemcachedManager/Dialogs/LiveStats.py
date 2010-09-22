from PyQt4 import QtGui
from PyQt4 import QtCore
from MemcachedManager.Dialogs.ui_LiveStats import Ui_liveStatsDialog
import time
import MemcachedManager.Settings

class Dialog(QtGui.QDialog, Ui_liveStatsDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.currentCluster = None
		self.monitor = False
		self.thread = None
		self.threadInterupt = False
		self.stats = []
		self.TableViewModel = MonitorTableModel()
		self.tbvLiveStats.setModel(self.TableViewModel)
		
		self.settings = MemcachedManager.Settings.Settings()
		
		self.connect(self, QtCore.SIGNAL('finished(int)'), self.stopMonitor)
		
	def show(self):
		QtGui.QDialog.show(self)
		self.startMonitor()
		self.stats = []
		self.tbvLiveStats.clearSpans()
		
	def setCluster(self, cluster):
		self.currentCluster = cluster
		
	def startMonitor(self):
		self.monitor = True
		self.threadInterupt = False
		if self.thread is None:
			self.thread = Monitor(self)
			self.connect(self.thread, QtCore.SIGNAL('refreshing'), self.statsRefreshing)
			self.connect(self.thread, QtCore.SIGNAL('refreshed'), self.statsRefreshed)
			self.thread.start()
	
	def stopMonitor(self):
		self.monitor = False
		self.threadInterupt = True
		self.stats = []
		
	def toggleMonitor(self):
		if self.monitor:
			self.stopMonitor()
		else:
			self.startMonitor()
			
	def statsRefreshing(self):
		self.setWindowTitle("Live Stats - Refreshing")
			
	def statsRefreshed(self):
		self.tbvLiveStats.resizeColumnsToContents()
		self.setWindowTitle("Live Stats")
	
	def updateStats(self, stats):
		self.stats = stats
		self.TableViewModel.updateStats(stats)
		
class MonitorTableModel(QtCore.QAbstractTableModel):
	def __init__(self, parent=None):
		QtCore.QAbstractTableModel.__init__(self, parent)
		self.stats = None
		self.headerdata = ["Server", 
						'No. Items', 
						'No. Connections', 
						'Hits', 
						'% Hits',
						'Misses', 
						'% Misses',
						'Gets', 
						'Sets', 
						'Evictions',
						'Free Space', 
						'Used Space']
		
	def updateStats(self, stats):
		self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
		self.stats = stats
		self.emit(QtCore.SIGNAL("layoutChanged()"))
		
	def headerData(self, col, orientation, role):
		if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
			return QtCore.QVariant(self.headerdata[col])
		return QtCore.QVariant()
		
	def rowCount(self, parent):
		if self.stats is not None:
			return len(self.stats.getServers())
		else: 
			return 0
	
	def columnCount(self, parent):
		return len(self.headerdata)
	
	def data(self, index, role):
		if not index.isValid():
			return QtCore.QVariant()
		elif role != QtCore.Qt.DisplayRole:
			return QtCore.QVariant()
		server = self.stats.getServers()[index.row()]
		if index.column() == 0:
			value = server.Name
		elif index.column() == 1:
			value =  "{0:n}".format(server.CurrItems)
		elif index.column() == 2:
			value = "{0:n}".format(server.CurrConnections)
		elif index.column() == 3:
			value = "{0:n}".format(server.GetHits)
		elif index.column() == 4:
			value = "{0:.2%}".format(server.getHitPerc())
		elif index.column() == 5:
			value = "{0:n}".format(server.GetMisses)
		elif index.column() == 6:
			value = "{0:.2%}".format(server.getMissPerc())
		elif index.column() == 7:
			value = "{0:n}".format(server.CMDGet)
		elif index.column() == 8:
			value = "{0:n}".format(server.CMDSet)
		elif index.column() == 9:
			value = "{0:n}".format(server.Evictions)
		elif index.column() == 10:
			value = server.getFormatedFreeSpace()
		elif index.column() == 11:
			value = server.getFormatedUsedSpace()
		else:	
			value = ''
			
		return QtCore.QVariant(value)
		

class Monitor(QtCore.QThread):
	def __init__(self, dialog):
		#threading.Thread.__init__(self)
		QtCore.QThread.__init__(self)
		self.dialog = dialog
		
	def run(self):
		while not self.dialog.threadInterupt:
			self.emit(QtCore.SIGNAL('refreshing'), None)
			try:
				stats = self.dialog.currentCluster.getStats()
			except Exception:
				try:
					stats = self.dialog.currentCluster.getStats()
				except Exception:
					stats = None
					
			if stats is not None:
				self.dialog.updateStats(stats)
				self.emit(QtCore.SIGNAL('refreshed'), None)
				time.sleep(int(self.dialog.settings.settings.config['Stats']['RefreshInterval']))
