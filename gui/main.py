import threading
from clientgui import ClientForm
from PyQt4 import QtCore, QtGui
import sys

if __name__ == '__main__':
    try:
      app = QtGui.QApplication(sys.argv)
      gui = ClientForm('41.191.124.10', 9119)
      gui.show()
      sys.exit(app.exec_())
    except IndexError:
      print 'Usage: python main.py <server> <port>'

