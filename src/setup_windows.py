from distutils.core import setup
import py2exe
import glob

# Parts of this setup file where borrowed from
# http://www.py2exe.org/index.cgi/MatPlotLib
# http://www.py2exe.org/index.cgi/Py2exeAndPyQt
opts = {
        'py2exe': { 
                   "includes" : [
                                 "sip", 
                                 "matplotlib.backends",  
                                 "matplotlib.backends.backend_qt4agg",
                                 "matplotlib.figure",
                                 "pylab", 
                                 "numpy", 
                                 "matplotlib.numerix.fft",
                                 "matplotlib.numerix.linear_algebra", 
                                 "matplotlib.numerix.random_array",
                                 "matplotlib.backends.backend_tkagg"
                                 ],
                    'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo', '_cocoaagg', '_fltkagg', '_gtk', '_gtkcairo'],
                    'dll_excludes': ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll']
                    }
        }
data_files = [
              (r'mpl-data', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\*.*')),
              (r'mpl-data', [r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
              (r'mpl-data\images',glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
              (r'mpl-data\fonts',glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\fonts\*.*'))
              ]

setup(name="Memcached Manager",
      version="0.1",
      description="",
      author="Nick Verbeck",
      author_email="nerdynick@gmail.com",
      url="http://code.google.com/p/memcached-manager",
      packages=['memcached','ServerActions'],
      py_modules=['Clusters','MemcachedManager','Servers','Settings','ui_MainWindow'],
      console=['MemcachedManager.py'],
      options=opts,
      data_files=data_files
      )
