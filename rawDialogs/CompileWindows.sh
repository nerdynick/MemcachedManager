#Main Window
echo "Compiling MainWindow.ui"
pyuic4 -o ../src/MemcachedManager/ui_MainWindow.py MainWindow.ui

#Live Stats Dialog
echo "Compiling LiveStats.ui"
pyuic4 -o ../src/MemcachedManager/Dialogs/ui_LiveStats.py LiveStats.ui

#Preferences Dialog
echo "Compiling Preferences.ui"
pyuic4 -o ../src/MemcachedManager/Dialogs/ui_Preferences.py Preferences.ui

#Cluster/Server Add Dialog
echo "Compiling Add.ui"
pyuic4 -o ../src/MemcachedManager/Dialogs/ui_Add.py Add.ui

#About Dialog
echo "Compiling About.ui"
pyuic4 -o ../src/MemcachedManager/Dialogs/ui_About.py About.ui

#Cached Item Dialog
echo "Compiling About.ui"
pyuic4 -o ../src/MemcachedManager/Dialogs/ui_CachedItem.py CachedItem.ui

echo "Done"
