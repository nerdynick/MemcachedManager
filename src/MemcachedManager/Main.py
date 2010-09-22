#!/usr/bin/env python
"""
Memcached Server Manager

Overview
========

Memcached Manager is a very simple yet powerful memcached server/cluster manager. 
It allows you to delete & flush keys, view stats, see the raw data on the server, and more. 

Author
======

U{Nick "NerdyNick" Verbeck   <nerdynick@gmail.com>}

Version
=======

0.1

Detailed Documentation
======================

You can read more documentation at U{http://code.google.com/p/memcached-manager/}

Copyright
=========

Copyright (C) 2008,2009  Nick Verbeck <nerdynick@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import os
import MainWindow

__version__ = "0.1a1.5"

def launch():
	app = QtGui.QApplication(sys.argv)
	window = MainWindow.MainWindow()
	window.show()
	app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))
	sys.exit(app.exec_())
	
def getIconPath(icon):
	basePath = os.path.dirname(os.path.realpath(__file__))
	return os.path.join(basePath, "Icons", icon)

if __name__ == '__main__':
	launch()
	
