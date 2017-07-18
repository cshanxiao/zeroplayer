# -*- coding: utf-8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2017-07-18
'''
import sys
from PyQt4 import QtGui
from control.main import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
