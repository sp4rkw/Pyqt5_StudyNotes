# -*-coding:utf-8-*-
# @Author : "GETF"
# @Time : 2018/3/1 13:12 
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import os,webbrowser,sys,base64,rsa
from PyQt5.QtWidgets import QFileDialog,QInputDialog,QLineEdit,QMessageBox,QApplication, QMainWindow  
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from PyQt5.QtCore import QCoreApplication 


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
     
    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        text = text.encode("utf-8")
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext).decode("ASCII")
     
    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0').decode("utf-8")



class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 599)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1800, 1200))
        self.textEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.textEdit.setToolTipDuration(-1)
        self.textEdit.setObjectName("textEdit")
        font = self.textEdit.font()
        font.setPointSize(font.pointSize() + 3)  
        self.textEdit.setFont(font)  
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 833, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu1 = QtWidgets.QMenu(self.menuBar)
        self.menu1.setObjectName("menu1")
        self.menu2 = QtWidgets.QMenu(self.menuBar)
        self.menu2.setObjectName("menu2")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(False)  
        self.action.setObjectName("action")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setCheckable(False)
        self.actionSave.setObjectName("actionSave")
        self.actionOtherSave = QtWidgets.QAction(MainWindow)
        self.actionOtherSave.setCheckable(False)
        self.actionOtherSave.setObjectName("actionOtherSave")
        self.actionDecrypt = QtWidgets.QAction(MainWindow)
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.actionEncrypt = QtWidgets.QAction(MainWindow)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setCheckable(False)
        self.actionabout.setObjectName("actionabout")
        self.menuAbout.addAction(self.actionabout)
        self.menu1.addAction(self.action)
        self.menu1.addAction(self.actionSave)
        self.menu1.addAction(self.actionOtherSave)
        self.menu2.addAction(self.actionDecrypt)
        self.menu2.addAction(self.actionEncrypt)
        self.menuBar.addAction(self.menu1.menuAction())
        self.menuBar.addAction(self.menu2.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
  
    def retranslateUi(self, MainWindow):  
        _translate = QtCore.QCoreApplication.translate  
        MainWindow.setWindowTitle(_translate("MainWindow", "密文阅读器"))
        self.textEdit.setStatusTip(_translate("MainWindow", "文件区"))
        self.menuBar.setStatusTip(_translate("MainWindow", "文件操作"))
        self.menu1.setStatusTip(_translate("MainWindow", "文件操作"))
        self.menu1.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu2.setTitle(_translate("MainWindow", "操作(O)"))
        self.menuAbout.setStatusTip(_translate("MainWindow", "关于我们"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于(A)"))
        self.action.setText(_translate("MainWindow", "打开"))
        self.action.setStatusTip(_translate("MainWindow", "打开文件"))
        self.actionSave.setText(_translate("MainWindow", "存储"))
        self.actionSave.setStatusTip(_translate("MainWindow", "存储文件"))
        self.actionOtherSave.setText(_translate("MainWindow", "另存为"))
        self.actionOtherSave.setStatusTip(_translate("MainWindow", "另存为xx文件"))
        self.actionDecrypt.setText(_translate("MainWindow", "解密"))
        self.actionDecrypt.setStatusTip(_translate("MainWindow", "解密文档"))
        self.actionEncrypt.setText(_translate("MainWindow", "加密"))
        self.actionEncrypt.setStatusTip(_translate("MainWindow", "加密文档"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionabout.setStatusTip(_translate("MainWindow", "了解我们"))  
  
  
class Window(QMainWindow, Ui_MainWindow):  
    def __init__(self, *args, **kwargs):  
        super(Window, self).__init__(*args, **kwargs)  
        self.setupUi(self)
        self.dir_name = os.path.abspath(os.path.dirname(__file__)).replace('\\','/')
        self.pwd = 0
        if(self.pwd == 0):
            self.Entercrypt()
        if(os.path.exists(self.dir_name+'/pub.txt')):
            des_encrypt = prpcrypt(self.pwd)
            f3 = open(self.dir_name+'/ip.txt','r',encoding='utf-8')
            des_test = f3.read()
            f3.close()
            try:
                AES_judge = des_encrypt.decrypt(des_test)
            except:
                AES_judge = 123
            if(AES_judge != 'qweasdzxcqwer'):
                self.EnterWarning2()
            else:
                f1 = open(self.dir_name+'/pub.txt','r')
                self.pubkey = rsa.PublicKey.load_pkcs1(f1.read().encode())
                f1.close()
                f2 = open(self.dir_name+'/priv.txt','r')
                priv_data = des_encrypt.decrypt(f2.read()).encode()
                self.privkey = rsa.PrivateKey.load_pkcs1(priv_data)
                f2.close()
        else:
            (self.pubkey, self.privkey) = rsa.newkeys(512)
            des_encrypt = prpcrypt(self.pwd)
            ipip = des_encrypt.encrypt("qweasdzxcqwer")
            f3 = open(self.dir_name+'/ip.txt','w+',encoding='utf-8')
            f3.write(ipip)
            f3.close()
            f1 = open(self.dir_name+'/pub.txt','w+')
            f1.write(self.pubkey.save_pkcs1().decode())
            f1.close()
            priv_deta = des_encrypt.encrypt(self.privkey.save_pkcs1().decode())
            f2 = open(self.dir_name+'/priv.txt','w+')
            f2.write(priv_deta)
            f2.close()

        #关于我们
        self.actionabout.triggered.connect(self.About_webbrowser_Clicked) 
        self.actionabout.setShortcut('Ctrl+A')  
        
        #打开文件
        self.action.triggered.connect(self.openFile)  
        self.action.setShortcut('Ctrl+O')

        #保存文件
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave.setShortcut('Ctrl+S')

        #另存为文件
        self.actionOtherSave.triggered.connect(self.saveOtherFile)
        self.actionOtherSave.setShortcut('Alt+S')
        
        #加密文件
        self.actionEncrypt.triggered.connect(self.EncryptFile)
        self.actionEncrypt.setShortcut('Ctrl+E')

        #解密文件
        self.actionDecrypt.triggered.connect(self.DecryptFile)
        self.actionDecrypt.setShortcut('Ctrl+D')


    def Entercrypt(self):
        value,ok = QInputDialog.getText(self, "密码输入框", "注意：密码必须为6位字母加数字！！！\n\n请在这里输入密码：", QLineEdit.Password, "密码请设置为6位字母")
        if(len(value) == 6 and value.isalnum() == True):
            self.pwd = 'qwlpS'+value+'123qq'
        else:
            self.EnterWarning()


    def EnterWarning(self):
        reply = QMessageBox.warning(self,"警告!", "密码格式或位数不符合要求", QMessageBox.Yes)
        if reply == QMessageBox.Yes:#这里对接收到的结果进行处理  
            sys.exit()

    def EnterWarning2(self):
        reply = QMessageBox.warning(self,"警告!", "密码错误，请重新输入", QMessageBox.Yes)
        if reply == QMessageBox.Yes:#这里对接收到的结果进行处理  
            sys.exit()


    def EncryptFile(self):
        try:
            data = self.textEdit.toPlainText().encode('utf-8')
            crypto = rsa.encrypt(data, self.pubkey)
            demo = base64.b64encode(crypto)
            self.textEdit.setText(str(demo,'utf-8'))
        except:
            pass

    def DecryptFile(self):
        try:
            data = self.textEdit.toPlainText().encode('utf-8')
            demo = base64.b64decode(data)
            message = rsa.decrypt(demo, self.privkey).decode('utf-8')
            self.textEdit.setText(message)
        except:
            pass

    def saveOtherFile(self):
        try:
            fileName2, filetype2 = QFileDialog.getSaveFileName(self,  "文件保存",  "C://Users/Administrator/Desktop",  "All Files (*);;Text Files (*.txt)")
            data = self.textEdit.toPlainText()
            file = open(fileName2,'w+')
            file.write(data)
            file.close()
        except:
            pass

    def About_webbrowser_Clicked(self):
        webbrowser.open('http://blog.csdn.net/wy_97/article/details/79434269')


    def openFile(self):  
        try:
            fileName1, filetype1 = QFileDialog.getOpenFileName(self,  "选取文件",  self.dir_name,  "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔  
            if(fileName1 != self.dir_name+'/Crypt/crypt.txt'):
                file = open(fileName1,'r')
                data = file.read()
                file.close()
                if not(os.path.exists(self.dir_name+'/Backup')):
                    os.mkdir(self.dir_name+'/Backup')
                file = open(self.dir_name+"/Backup/backup.txt",'w+')
                file.write(data)
                file.close()
            else:
                file = open(fileName1,'r',encoding='ISO-8859-15')
                data = file.read()
                file.close()
                if not(os.path.exists(self.dir_name+'/Backup')):
                    os.mkdir(self.dir_name+'/Backup')
                file = open(self.dir_name+"/Backup/backup.txt",'w+',encoding='ISO-8859-15')
                file.write(data)
                file.close()
            
            self.textEdit.setText(data)
        except:
            pass

    def saveFile(self):
        try:
            if not(os.path.exists(self.dir_name+'\Crypt')):
                os.mkdir(self.dir_name+'\Crypt')
            data = self.textEdit.toPlainText()
            file = open(self.dir_name+'\Crypt\crypt.txt','w+',encoding='ISO-8859-15')
            file.write(data)
            file.close()
        except:
            pass

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    w = Window()  
    dir_path = os.path.abspath(os.path.dirname(__file__))+'\image\\1.ico'
    w.setWindowIcon(QIcon(dir_path))
    w.show()  
    sys.exit(app.exec_())  