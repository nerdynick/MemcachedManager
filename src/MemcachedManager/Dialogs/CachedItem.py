'''
Created on Jul 14, 2010

@author: nick
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from MemcachedManager.Dialogs.ui_CachedItem import Ui_CacheItem
import json
from MemcachedManager.PHPUnserialize import PHPUnserialize
from MemcachedManager.Clusters import ActiveCluster

class CachedItem(QtGui.QDialog, Ui_CacheItem):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.currentKeys = None
        
        self.connect(self, QtCore.SIGNAL('refresh'), self._refresh)
        self.connect(self.cbEncodings, QtCore.SIGNAL('currentIndexChanged(int)'), self._refresh)
        
    def refresh(self, keys):
        self.currentKeys = keys
        self.emit(QtCore.SIGNAL('refresh'), None)
        
    def _refresh(self, *args):
        if ActiveCluster().getActive() is not None and self.currentKeys is not None and self.currentKeys != "":
            encoding = self.cbEncodings.currentText()
            if encoding == 'Python Pickeled':
                unpickel=True
            else:
                unpickel=False
                
            values = ActiveCluster().getActive().getKeys(self.currentKeys, unpickel=unpickel)
            text = ""
            for server, value in dict(values).items():
                if encoding == 'PHP Serialized':
                    tvalue = []
                    for k,v in dict(value).iteritems():
                        try:
                            v = str(PHPUnserialize().unserialize(v))
                        except Exception:
                            v = 'Error'
                        tvalue.append("--- "+ str(k) +" ---\n\n"+v)
                    value = tvalue
                elif encoding == 'JSON':
                    tvalue = []
                    for k,v in dict(value).iteritems():
                        try:
                            v = str(json.dumps(json.loads(v), sort_keys=True, indent=4))
                        except Exception:
                            v = 'Error'
                        tvalue.append("--- "+ str(k) +" ---\n\n"+v)
                    value = tvalue
                else:
                    value = ["--- "+ str(k) +" ---\n\n"+ v for k,v in dict(value).iteritems()]
                    
                value = "\n\n".join(value)
                text += "\n\n==="+ str(server) +"===\n"+value
                text = QtCore.QString(text)
                
            self.txtCachedValue.setPlainText(text)
        