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
                
            compressed = False
            if encoding[-12:] == "(Compressed)":
                compressed = True
                encoding = encoding[0:-13]
                
            values = ActiveCluster().getActive().getKeys(self.currentKeys, unpickel=unpickel, compressed=compressed)
            text = ""
            for server, keys in dict(values).items():
                if encoding == 'PHP Serialized':
                    tvalue = []
                    for k,v in dict(keys).iteritems():
                        if v is not None:
                            try:
                                v = str(PHPUnserialize().unserialize(v))
                            except Exception:
                                v = 'Error'
                        else:
                            v = "(None)"
                            
                        tvalue.append(self._formatKeyValue(k, v))
                    value = tvalue
                elif encoding == 'JSON':
                    tvalue = []
                    for k,v in dict(keys).iteritems():
                        if v is not None:
                            try:
                                v = str(json.dumps(json.loads(v), sort_keys=True, indent=4))
                            except Exception:
                                v = 'Error'
                        else:
                            v = "(None)"
                            
                        tvalue.append(self._formatKeyValue(k, v))
                    value = tvalue
                else:
                    tvalue = []
                    for k,v in dict(keys).iteritems():
                        if v is None:
                            v = "(None)"
                            
                        tvalue.append(self._formatKeyValue(k, v))
                    value = tvalue
                    
                if text != "":
                    text += "\n\n"
                    
                text += str(server)+"\n"
                text += "="*len(str(server))
                text += "\n\n"
                text += "\n\n".join(value)
                text = QtCore.QString(text)
                
            self.txtCachedValue.setPlainText(text)
            
    def _formatKeyValue(self, key, value):
        text = str(key)+"\n"
        text += "-"*len(str(key))
        text += "\n"+ str(value)
        return text
        