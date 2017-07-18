# -*- coding: utf-8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2017-07-18
'''
from PyQt4.Qt import Qt, QEvent

from PyQt4 import QtCore
from PyQt4 import QtGui
from view.main_ui import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.init()

    def init(self):
        # 设置窗口标题
        self.setWindowTitle(u"零氏播放器")

        # 设置窗口图标，会在任务栏显示
        icon = QtGui.QIcon("./resource/logo/zero_32x32.ico")
        self.setWindowIcon(icon)

        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 设备窗口背景


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QtGui.QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def bind(self):
        pass
