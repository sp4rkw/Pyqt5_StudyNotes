# -*- coding:utf-8 -*- 
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2017-11-09 15:12:14
 @Description: Description 
'''



import os
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)
from PyQt5.QtCore import QDateTime,QTimer
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
                


    def initUI(self):
        self.lcd = QLCDNumber(self)#设置数字类
        self.lcd.setDigitCount(25)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet("border: 1px solid green; color: green; background: silver;")#设置显示的颜色样式
        vbox = QVBoxLayout()#设置布局
        vbox.addWidget(self.lcd)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('hello')
        dir_path = os.path.abspath(os.path.dirname(__file__))+'\image\\1.ico'
        self.setWindowIcon(QIcon(dir_path))
        self.show()
        self.timer = QTimer()
        self.timer.start(1)
        self.timer.timeout.connect(self.flush)#使用了计时器
        '''
        创建计时器->设置1ms刷新间隔->每次刷新执行flush函数
        '''
        
        
    def flush(self):
        #获取系统当前时间
        dateTime=QDateTime.currentDateTime()
        #显示的内容
        self.lcd.display(dateTime.toString("yyyy-MM-dd HH:mm:ss.zzz"))

 
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






