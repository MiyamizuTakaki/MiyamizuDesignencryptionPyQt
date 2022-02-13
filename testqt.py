##日后翻译我会单独列写，中文有中文，俄文有俄文，
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QCheckBox,QPushButton,QFileDialog,QTextEdit
from PyQt6.QtWidgets import QLabel,QLineEdit,QGridLayout
from pathlib import Path
from encryption import MKencryption
import json
from unencryption import uMKencryption
from language import*
class PyQtMKencryption(QMainWindow):

    def __init__(self,lm):
        super().__init__()
        self.lm = lm
        self.initUI()


    def initUI(self):
        ln = Language(self.lm)
        c = open("Wxit.txt",'w')
        with c:
            c.write("")
        c = open("Wait.txt",'w')
        with c:
            c.write("")
        self.statusBar().showMessage('加解密程序软件——www.mitsuha.top')

        self.setGeometry(300, 300, 700, 500)
        self.center()
        self.setWindowTitle('加解密程序软件——www.mitsuha.top')
        mkof = QPushButton(ln.lumkof(),self)##定义各类按钮控件，有语言翻译
        mkff = QPushButton(ln.lumkff(),self)
        mkcj = QPushButton(ln.lumkcj(),self)
        mkef = QPushButton(ln.lumkef(),self)
        mkfl = QPushButton(ln.lumkfl(),self)
        mkll = QPushButton(ln.lumkll(),self)
        stjm = QPushButton(ln.lustjm(),self)
        stxm = QPushButton(ln.lustxm(),self)
        mkof.move(10,30)##位置
        mkof.resize(150,30)##大小
        mkff.move(160,30)
        mkff.resize(150,30)
        mkef.move(310,30)
        mkef.resize(200,30)
        mkfl.move(510,30)
        mkfl.resize(170,30)
        stjm.move(10,60)
        stjm.resize(150,30)
        stxm.move(160,60)
        stxm.resize(150,30)
        mkll.move(310,60)
        mkll.resize(170,30)
        mkcj.move(490,60)
        mkcj.resize(210,30)
        self.fmkof = mkof.clicked.connect(self.FileRead)##原始文件
        self.fmkof = mkff.clicked.connect(self.FileOpen)

        self.fmkef = mkef.clicked.connect(self.FileRead)##加密文件
        self.fmkef = mkcj.clicked.connect(self.FileOpen)

        self.fmkfl = mkfl.clicked.connect(self.FileRead)##密钥文件
        self.fmkfl = mkll.clicked.connect(self.FileOpen)

        stjm.clicked.connect(self.startepc)
        stxm.clicked.connect(self.unstartepc)

        self.te = QTextEdit(ln.lute(),self)
        self.te.move(10,130)
        self.te.resize(200,200)
        self.tx = QTextEdit(ln.lutx(),self)
        self.tx.move(230,130)
        self.tx.resize(200,200)
        self.syst = QLabel("系统状态",self)
        self.syst.move(10,350)
        self.ys = QLabel("原始文件路径:",self)
        self.ys.move(10,370)
        self.jm = QLabel("加密文件路径:",self)
        self.jm.move(10,390)
        self.my = QLabel("密钥文件路径:",self)
        self.my.move(10,410)
        self.show()
    
    def center(self):
        ##这个用来把窗口居中用的
        dy = self.frameGeometry()
        dys = self.screen().availableGeometry().center()

        dy.moveCenter(dys)
        self.move(dy.topLeft())
    
    def FileRead(self):
        ln = Language(self.lm)
        dfc = self.sender()
        home_dir = str(Path.home)
        fname = QFileDialog.getOpenFileName(self, ln.lumkcc(), home_dir)
        if fname[0] !='':
            f = open(fname[0], 'r')
            ##self.my.setText(fname[0])
            self.my.resize(300,410)
            with f:
                data = f.read() 
                if dfc.text() == ln.lumkof() or dfc.text() == ln.lumkef():
                    self.te.setText(data)
            c = open("wxit.txt", 'a')
            with c:
                if dfc.text() == ln.lumkof():
                    ts = {"mkof":fname[0]}
                    json.dump(ts,c)
                    c.write('\n')
                elif dfc.text() == ln.lumkef():
                    ts = {"mkef":fname[0]}
                    json.dump(ts,c)
                    c.write('\n')
                elif dfc.text() == ln.lumkfl():
                    ts = {"mkfl":fname[0]}
                    json.dump(ts,c)
                    c.write('\n')
    def FileOpen(self):
        ln = Language(self.lm)
        dfc = self.sender()
        home_dir = str(Path.home)
        fname = QFileDialog.getSaveFileName(self,ln.lumkxc(),home_dir)
        if fname[0] !=' ':
            c = open("Wait.txt", 'a')
            with c:
                if dfc.text() == ln.lumkff():
                    ts = {"mkof":fname[0]}
                    json.dump(ts,c)
                    c.write('\n')
                elif dfc.text() == ln.lumkcj():
                    ts = {"mkef":fname[0]}
                    json.dump(ts,c)
                    c.write('\n')
                elif dfc.text() == ln.lumkll():
                    ts = {"mkfl":fname[0]}
                    json.dump(ts,c)
                    c.write('\n')
    def startepc(self):
        with open("Wxit.txt",'r',encoding="utf-8") as f:
            for c in f.readlines():
                c1 = json.loads(c)
                for cx,cy in c1.items():
                    if cx == 'mkof':##原始文件
                        fmokf = cy
                    elif cx == 'mkef':##加密文件
                        fmkef = cy
                    elif cx == 'mkfl':##密钥文件
                        fmkfl = cy
        with open("Wait.txt",'r',encoding="utf-8") as f:
            for c in f.readlines():
                c1 = json.loads(c)
                for cx,cy in c1.items():
                    if cx == 'mkof':##原始文件
                        fmokf = cy
                    elif cx == 'mkef':##加密文件
                        fmkef = cy
                    elif cx == 'mkfl':##密钥文件
                        fmkfl = cy
        ec = MKencryption(fmkfl,fmkef,fmokf)
        ec.mkfile()
        seok = ec.encryptionst()
        f = open(fmkef,'r')
        with f:
            f1 = f.read()
            self.tx.setText(f1)
    def unstartepc(self):
        with open("Wxit.txt",'r',encoding="utf-8") as f:
            for c in f.readlines():
                c1 = json.loads(c)
                for cx,cy in c1.items():
                    if cx == 'mkof':##原始文件
                        fmokf = cy
                    elif cx == 'mkef':##加密文件
                        fmkef = cy
                    elif cx == 'mkfl':##密钥文件
                        fmkfl = cy
        with open("Wait.txt",'r',encoding="utf-8") as f:
            for c in f.readlines():
                c1 = json.loads(c)
                for cx,cy in c1.items():
                    if cx == 'mkof':##原始文件
                        fmokf = cy
                    elif cx == 'mkef':##加密文件
                        fmkef = cy
                    elif cx == 'mkfl':##密钥文件
                        fmkfl = cy
        ec = uMKencryption(fmkfl,fmkef,fmokf)
        ec.sureency()
        ec.uencryption()
        f = open(fmokf,'r')
        with f:
            f1 = f.read()
            self.tx.setText(f1)


def main():
    lm = False
    app = QApplication(sys.argv)
    ex = PyQtMKencryption(lm)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()