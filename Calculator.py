# -*- coding:utf-8 -*- 
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2017-11-20 16:08:54
 @Description: Description 
'''


import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QIcon
import os

class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.string = ''#作为容器去计算
        self.number = '0'#初始值
        self.setWindowTitle('简单计算器')#设置标题
        grid = QtWidgets.QGridLayout()#网格型布局 
        self.display = QtWidgets.QLineEdit('0')#QLineEdit是一个单行文本编辑控件。
        '''
        QLineEdit是一个单行文本编辑控件。
        使用者可以通过很多函数，输入和编辑单行文本，比如撤销、恢复、剪切、粘贴以及拖放等。
        通过改变QLineEdit的 echoMode() ，可以设置其属性，比如以密码的形式输入。
        文本的长度可以由 maxLength() 限制，可以通过使用 validator() 或者 inputMask() 可以限制它只能输入数字。在对同一个QLineEdit的validator或者input mask进行转换时，最好先将它的validator或者input mask清除，以避免错误发生。
        与QLineEdit相关的一个类是QTextEdit，它允许多行文字以及富文本编辑。
        我们可以使用 setText() 或者 insert() 改变其中的文本，通过 text() 获得文本，通过 displayText() 获得显示的文本，使用 setSelection() 或者 selectAll() 选中文本，选中的文本可以通过cut()、copy()、paste()进行剪切、复制和粘贴，使用 setAlignment() 设置文本的位置。
        文本改变时会发出 textChanged() 信号；如果不是由setText()造成文本的改变，那么会发出textEdit()信号；鼠标光标改变时会发出cursorPostionChanged()信号；当返回键或者回车键按下时，会发出returnPressed()信号。
        当编辑结束，或者LineEdit失去了焦点，或者当返回/回车键按下时，editFinished()信号将会发出。
        '''
        self.display.setFont(QtGui.QFont("Times", 20))#设置字体
        self.display.setReadOnly(True)#设置可编辑
        self.display.setAlignment(QtCore.Qt.AlignRight)#设置文本位置，这里设置为右边开始
        self.display.setMaxLength(15)#设置最大的长度  
        grid.addWidget(self.display,0,0,1,4)
        '''
        void QGridLayout::addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)
        6个参数表示控件名，行，列，占用行数，占用列数，对齐方式
        '''
        names = ['Clear', 'Back', '', 'Close', 
                '7', '8', '9', '/',
                '4', '5', '6', '*', 
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]
        c = 0
        for name in names:
            button = QtWidgets.QPushButton(name)
            button.setFixedSize(QtCore.QSize(60,30))
            button.clicked.connect(self.buttonClicked) # 给每个按钮设置信号/槽
            if c == 2:
                pass
                #grid.addWidget(QtWidgets.QLabel(''), 0, 2) #替换 第三个按钮 为 文本标签！
            else: 
                grid.addWidget(button, pos[c][0]+1, pos[c][1])
            c = c + 1      
        self.setLayout(grid)
        
        
        
        
    def buttonClicked(self): 
        #sender = self.sender();  # 确定信号发送者
        #self.display.setText(sender.text())#确定text为name
        text = self.sender().text()
        if text == "=":
            self.string = self.string+self.number
            self.number = str(eval(self.string)) # 简单计算,这里使用eval直接计算字符串
            self.string=''
        elif text in '+-*/':
            self.string = self.string+self.number+text
            self.number='0'#清空数字
        elif text == "Back":
            self.string = self.string.Substring(0,self.string.Length - 1)#删去最后一位
        elif text == "Clear":
            self.number = "0"
        elif text == "Close":
            self.close()
        else:
            if(self.number == '0'):
                self.number=''
            self.number = self.number+text

        self.display.setText(self.number)


app = QtWidgets.QApplication(sys.argv)
ex = Example()
dir_path = os.path.abspath(os.path.dirname(__file__))+'\image\\1.ico'
ex.setWindowIcon(QIcon(dir_path))
ex.show()
sys.exit(app.exec_())