# -*- coding:utf-8 -*- 
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2017-11-24 00:38:36
 @Description: 注意，这里只是用了eric6构建了一个图形页面，实际功能(信号传输机制并没有设置)
'''


# Form implementation generated from reading ui file 'F:\pythonexe\notepad\notepad.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__))+'\image\\1.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)#这里自己手动改了地址
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(-7, -4, 621, 501))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 606, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu1 = QtWidgets.QMenu(self.menuBar)
        self.menu1.setObjectName("menu1")
        self.menu2 = QtWidgets.QMenu(self.menuBar)
        self.menu2.setObjectName("menu2")
        self.menu3 = QtWidgets.QMenu(self.menuBar)
        self.menu3.setObjectName("menu3")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setAcceptDrops(False)
        self.statusBar.setAutoFillBackground(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action2_2 = QtWidgets.QAction(MainWindow)
        self.action2_2.setObjectName("action2_2")
        self.action3_2 = QtWidgets.QAction(MainWindow)
        self.action3_2.setObjectName("action3_2")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setCheckable(False)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_sa = QtWidgets.QAction(MainWindow)
        self.actionSave_sa.setObjectName("actionSave_sa")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSetup = QtWidgets.QAction(MainWindow)
        self.actionSetup.setObjectName("actionSetup")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSave_as)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSetup)
        self.menu.addAction(self.actionPrint)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu1.menuAction())
        self.menuBar.addAction(self.menu2.menuAction())
        self.menuBar.addAction(self.menu3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "记事本 BY GETF"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这是一个伪装notepad</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.menu1.setTitle(_translate("MainWindow", "格式(&O)"))
        self.menu2.setTitle(_translate("MainWindow", "查看(&V)"))
        self.menu3.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
        self.action4.setText(_translate("MainWindow", "4"))
        self.action1_2.setText(_translate("MainWindow", "1"))
        self.action2_2.setText(_translate("MainWindow", "2"))
        self.action3_2.setText(_translate("MainWindow", "3"))
        self.actionNew.setText(_translate("MainWindow", "新建(&N)"))
        self.actionNew.setToolTip(_translate("MainWindow", "新建一个文件"))
        self.actionOpen.setText(_translate("MainWindow", "打开(&O)..."))
        self.actionSave.setText(_translate("MainWindow", "保存(&S)"))
        self.actionSave_sa.setText(_translate("MainWindow", "save sa"))
        self.actionSave_as.setText(_translate("MainWindow", "另存为(&A)..."))
        self.actionSetup.setText(_translate("MainWindow", "页面设置(&U)..."))
        self.actionPrint.setText(_translate("MainWindow", "打印(&P)..."))
        self.actionExit.setText(_translate("MainWindow", "退出(&X)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

