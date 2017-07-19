# -*- coding: utf-8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2017-07-18
'''
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.Qt import Qt, QEvent

from view.main_ui import Ui_MainWindow
from superutils import print_obj

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.init()

    def init(self):
        # 设置窗口标题
        self.setWindowTitle(u"零氏播放器")

        # 设置窗口图标，会在任务栏显示
        icon = QtGui.QIcon("./resource/logo/zero_32x32.png")
        self.setWindowIcon(icon)

        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 增加 widget
        self.wgt = QtGui.QWidget(self)
        self.setCentralWidget(self.wgt)
        
        # 设置背景颜色
        color = QtGui.QColor(0, 0, 0)
        self.wgt.setStyleSheet("QWidget{background-color: %s}" % color.name())
        
        # 添加最大化，最小化，关闭按钮
        self.min_btn = QtGui.QPushButton(u"最小化",self)
        self.min_btn.setStyleSheet("QWidget{background-color: #FF0000}")
        self.min_btn.clicked.connect(self.showMinimized)
        
        self.max_btn = QtGui.QPushButton(u"最大化",self)
        self.max_btn.setStyleSheet("QWidget{background-color: #00FF00}")
        self.max_btn.clicked.connect(self.change_size)
        
        self.close_btn = QtGui.QPushButton(u"关闭",self)
        self.close_btn.setStyleSheet("QWidget{background-color: #0000FF}")
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setObjectName('test')
        
        # 增加布局
        hbox1 = QtGui.QHBoxLayout()   #水平布局
        hbox1.addStretch()
        hbox1.addWidget(self.min_btn, alignment=Qt.AlignRight)
        hbox1.addWidget(self.max_btn, alignment=Qt.AlignRight)
        hbox1.addWidget(self.close_btn, alignment=Qt.AlignRight)
        
        vbox = QtGui.QVBoxLayout()   #垂直布局
        vbox.addLayout(hbox1)
        vbox.addStretch()
        self.wgt.setLayout(vbox)
        self.is_max_size = False
        self.default_size = self.size()
        
#     def change_size(self):
#         print self.is_max_size
#         if self.is_max_size:
#             self.resize(self.default_size)
#             self.is_max_size = False
#         else:
#             self.is_max_size = True
#             self.showMaximized()
#         print "changed", self.is_max_size
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_drag = True
            self.target_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.is_drag:
            self.move(QMouseEvent.globalPos() - self.target_pos)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.is_drag = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def bind(self):
        pass
    
    
    
