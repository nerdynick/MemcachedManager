'''
Created on Jul 14, 2010

@author: nick
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from MemcachedManager.Dialogs.ui_CachedItem import Ui_CacheItem
import json
from MemcachedManager.PHPUnserialize import PHPUnserialize

class CachedItem(QtGui.QDialog, Ui_CacheItem):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.currentCluster = None
        self.currentKeys = None
        
        self.connect(self, QtCore.SIGNAL('refresh'), self._refresh)
        self.connect(self.cbEncodings, QtCore.SIGNAL('currentIndexChanged(int)'), self._refresh)
        
    def setCluster(self, cluster):
        self.currentCluster = cluster
        self.emit(QtCore.SIGNAL('refresh'), None)
        
    def setKeys(self, keys):
        self.currentKeys = keys
        self.emit(QtCore.SIGNAL('refresh'), None)
        
    def _refresh(self, *args):
        if self.currentCluster is not None and self.currentKeys is not None and self.currentKeys != "":
            encoding = self.cbEncodings.currentText()
            if encoding == 'Python Pickeled':
                unpickel=True
            else:
                unpickel=False
                
            value = self.currentCluster.getKey(self.currentKeys, unpickel=unpickel)
            if encoding == 'PHP Serialized':
                #TODO: PHP Deserialize
                value = ["=== "+ str(k) +" ===\n\n"+ str(PHPUnserialize().unserialize(v)) for k,v in dict(value).iteritems()]
            elif encoding == 'JSON':
                value = ["=== "+ str(k) +" ===\n\n"+ str(json.dumps(json.loads(v), sort_keys=True, indent=4)) for k,v in dict(value).iteritems()]
            else:
                value = ["=== "+ str(k) +" ===\n\n"+ v for k,v in dict(value).iteritems()]
                
            value = "\n\n".join(value)
            self.txtCachedValue.setPlainText(value)
        