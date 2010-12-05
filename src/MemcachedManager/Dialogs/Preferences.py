from PyQt4 import QtGui
from PyQt4 import QtCore
from MemcachedManager.Dialogs.ui_Preferences import Ui_PrefWindow
import time
import threading
from MemcachedManager.Settings import Settings

class Preferences(QtGui.QDialog, Ui_PrefWindow):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.settings = Settings()
		
		self.txtHitMissesColor.setText(self.settings.settings.config['Graphs']['HitMiss'])
		self.txtGetsSetsColor.setText(self.settings.settings.config['Graphs']['GetSet'])
		
		tmpText = ''
		for colors in self.settings.settings.config['Graphs']['Pie']:
			tmpText += colors[0] +","+ colors[1] +"\n"
			
		self.txtPieColors.setText(tmpText)
		
		self.txtRefreshLiveStats.setText(str(self.settings.settings.config['Stats']['RefreshInterval']))
		if self.settings.settings.config['Stats']['AutoRefresh'] is True:
			self.cbAutoRefresh.setCheckState(QtCore.Qt.Checked)
		else:
			self.cbAutoRefresh.setCheckState(QtCore.Qt.Unchecked)
			
		
		self.connect(self.btnSave, QtCore.SIGNAL('clicked()'), self.save)
		
		tSettings = self.settings.settings.config['Stats']['ServerStats']
		self.cbPID.setChecked(tSettings['PID'])
		self.cbStarted.setChecked(tSettings['DateStarted'])
		self.cbUptime.setChecked(tSettings['Uptime'])
		self.cbPointerSize.setChecked(tSettings['PointerSize'])
		self.cbThreads.setChecked(tSettings['Threads'])
		self.cbCPUUser.setChecked(tSettings['CPUUserTime'])
		self.cbCPUSystem.setChecked(tSettings['CPUSystemTime'])
		self.cbConnectionStructs.setChecked(tSettings['ConnectionStruct'])
		self.cbAcceptingConnections.setChecked(tSettings['AcceptingConnections'])
		self.cbConnectionYield.setChecked(tSettings['ConnectionYield'])
		self.cbListenDisabled.setChecked(tSettings['ListenDisabled'])
		self.cbTotalItems.setChecked(tSettings['TotalItems'])
		self.cbCurrentItems.setChecked(tSettings['CurrentItems'])
		self.cbTotalConnections.setChecked(tSettings['TotalConnections'])
		self.cbConnections.setChecked(tSettings['CurrentConnections'])
		self.cbFlushes.setChecked(tSettings['Flushes'])
		self.cbEvictions.setChecked(tSettings['Evictions'])
		self.cbNetIn.setChecked(tSettings['NetIn'])
		self.cbNetOut.setChecked(tSettings['NetOut'])
		self.cbTotalSpace.setChecked(tSettings['TotalSpace'])
		self.cbFreeSpace.setChecked(tSettings['FreeSpace'])
		self.cbUsedSpace.setChecked(tSettings['UsedSpace'])
		self.cbRequests.setChecked(tSettings['TotalRequests'])
		self.cbGets.setChecked(tSettings['TotalGets'])
		self.cbSets.setChecked(tSettings['TotalSets'])
		self.cbGetHits.setChecked(tSettings['GetHits'])
		self.cbGetMisses.setChecked(tSettings['GetMisses'])
		self.cbDeleteHits.setChecked(tSettings['DeleteHits'])
		self.cbDeleteMisses.setChecked(tSettings['DeleteMisses'])
		self.cbIncrHits.setChecked(tSettings['IncrHits'])
		self.cbIncrMisses.setChecked(tSettings['IncrMisses'])
		self.cbDecrHits.setChecked(tSettings['DecrHits'])
		self.cbDecrMisses.setChecked(tSettings['DecrMisses'])
		self.cbCASHits.setChecked(tSettings['CASHits'])
		self.cbCASMisses.setChecked(tSettings['CASMisses'])
		self.cbCASBadval.setChecked(tSettings['CASBadval'])
		self.cbRequestRate.setChecked(tSettings['RequestRate'])
		self.cbHitRate.setChecked(tSettings['HitRate'])
		self.cbMissRate.setChecked(tSettings['MissRate'])
		self.cbGetRate.setChecked(tSettings['GetRate'])
		self.cbSetRate.setChecked(tSettings['SetRate'])
		self.cbEvictionRate.setChecked(tSettings['EvictionRate'])
		
	def save(self):
		"""
		Saves all the current preferences to Settings
		"""
		self.settings.settings.config['Graphs']['GetSet'] = str(self.txtGetsSetsColor.text())
		self.settings.settings.config['Graphs']['HitMiss'] = str(self.txtHitMissesColor.text())
		
		tmpColor = []
		for row in str(self.txtPieColors.toPlainText()).split("\n"):
			row_s = str(row).split(',')
			if len(row_s) == 2:
				tmpColor.append((row_s[0], row_s[1]))
			
		self.settings.settings.config['Graphs']['Pie'] = tmpColor
		
		self.settings.settings.config['Stats']['RefreshInterval'] = int(self.txtRefreshLiveStats.text())
		if self.cbAutoRefresh.isChecked():
			self.settings.settings.config['Stats']['AutoRefresh'] = True
		else:
			self.settings.settings.config['Stats']['AutoRefresh'] = False
			
		self.settings.settings.config['Stats']['ServerStats'] = {
			'PID':self.cbPID.isChecked(), 'DateStarted':self.cbStarted.isChecked(), 'Uptime':self.cbUptime.isChecked(),
			'PointerSize':self.cbPointerSize.isChecked(), 'Threads':self.cbThreads.isChecked(),
			'CPUUserTime':self.cbCPUUser.isChecked(), 'CPUSystemTime':self.cbCPUSystem.isChecked(),
			'ConnectionStruct':self.cbConnectionStructs.isChecked(), 'AcceptingConnections':self.cbAcceptingConnections.isChecked(), 
			'ConnectionYield':self.cbConnectionYield.isChecked(), 'ListenDisabled':self.cbListenDisabled.isChecked(),
			'TotalItems':self.cbTotalItems.isChecked(), 'CurrentItems':self.cbCurrentItems.isChecked(),
			'TotalConnections':self.cbTotalConnections.isChecked(), 'CurrentConnections':self.cbConnections.isChecked(),
			'Flushes':self.cbFlushes.isChecked(), 'Evictions':self.cbEvictions.isChecked(),
			'NetIn':self.cbNetIn.isChecked(), 'NetOut':self.cbNetOut.isChecked(),
			'TotalSpace':self.cbTotalSpace.isChecked(), 'FreeSpace':self.cbFreeSpace.isChecked(), 'UsedSpace':self.cbUsedSpace.isChecked(),
			'TotalRequests':self.cbRequests.isChecked(), 'TotalGets':self.cbGets.isChecked(), 'TotalSets':self.cbSets.isChecked(),
			'GetHits':self.cbGetHits.isChecked(), 'GetMisses':self.cbGetMisses.isChecked(),
			'DeleteHits':self.cbDeleteHits.isChecked(), 'DeleteMisses':self.cbDeleteMisses.isChecked(),
			'IncrHits':self.cbIncrHits.isChecked(), 'IncrMisses':self.cbIncrMisses.isChecked(),
			'DecrHits':self.cbDecrHits.isChecked(), 'DecrMisses':self.cbDecrMisses.isChecked(),
			'CASHits':self.cbCASHits.isChecked(), 'CASMisses':self.cbCASMisses.isChecked(), 'CASBadval':self.cbCASBadval.isChecked(),
			'RequestRate':self.cbRequestRate.isChecked(), 'HitRate':self.cbHitRate.isChecked(), 'MissRate':self.cbMissRate.isChecked(),
			'GetRate':self.cbGetRate.isChecked(), 'SetRate':self.cbSetRate.isChecked(), 'EvictionRate':self.cbEvictionRate.isChecked()
		}
		
		self.settings.save()
		self.close()