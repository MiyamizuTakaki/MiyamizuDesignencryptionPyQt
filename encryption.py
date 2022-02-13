import random
import json
from re import M
from pathlib import Path
from PyQt6.QtCore import *
def zis(k):##检查i是否为质数
    for q in range(2,k):
        if k%q == 0:
            return True
        return False
def hzjc(k1, n):##检查是否互质
    if k1>n:
        if k1%n == 0:
            return False
        else:
            return True
    elif k1<n:
        if n%k1 == 0:
            return False
        else:
            return True
    elif k1==n:
        return False

class MKencryption():
    def __init__(self,mkfl,mkjm,mkse):
        self.mkstr = ""##字符串
        self.mkfl = mkfl##密钥文件
        self.mkjm = mkjm##加密/解密文件
        self.mkea = 1##初始化##加密代数
        self.mkse = mkse##加密文件存放路径
    def mkfile(self):##创建文件
        with open(self.mkfl,'w')as dlfile:##密钥文件
            dlfile.write("__MiyamizuDesign__encryption__1__\n")##没这个不给解密
        with open(self.mkjm,'w')as dlfile:##加密文件
            dlfile.write("__MiyamizuDesign__encryptionFile__\n")##没这个不给解密
    ##告诉大家，这个我不核对文件一致性，一定程度保证安全
    ##还有，先创建文件，后加密
    ##还有中文的问题以后解决，目前有中文加密后解密后必有乱码
    ##Русский язывк Готов! Не вопрос!
    def encryptionst(self):
        with open(self.mkse, 'r',encoding='utf-8') as dlfile:
            i = 0
            for dlfilex in dlfile:
                i = i +len(dlfilex)
        ok = True
        while ok==True:
            with open(self.mkse,'r',encoding='utf-8')as dlfile:
                for dlfiles in dlfile:
                    self.mkstr = dlfiles
                    jl=[0,i,0,0]##左边为随机数右边长度
                    k = 0##随机数初始化
                    for mkstrx in self.mkstr:
                        n = ord(mkstrx)##utf8推算，类型转换
                        pd = True
                        pd1 = False
                        while pd==True or pd1 == False:
                            k1 = random.randint(1,i)##咱这个随机数按照未加密字符长度确定
                            pd = zis(k1)
                            pd1 = hzjc(k1,n)
                            if pd==False and pd1 == True:
                                k = k1
                                jl[0]=k##随机数
                                jl[2] = int((i*k)/n)##求商，相当于校验码
                                if (i*k)<n:
                                    jl[3]= n-(i*k)
                                with open(self.mkfl,'a')as dlfile:
                                    json.dump(jl,dlfile)
                                    dlfile.write("\n")
                                ei = (i*k)%n##加密推算
                                jl[3]=0
                                with open(self.mkjm,'a',encoding='utf-8')as dlfile:
                                    dlfile.write(chr(ei))##文件写入
            ##由于生成的文件经常出现缺斤少两，必须验证，不合格重新处理，不然解密后的文件不完整
            ##完整性验证
            m= 0
            with open(self.mkfl,'r')as dlfile:
                for dlfiles in dlfile:
                    m = m+1
            m = m+1
            p=i
            p = p+2
            if p !=m:
                with open(self.mkfl,'w')as dlfile:
                    dlfile.write("__MiyamizuDesign__encryption__1__\n")
                with open(self.mkjm,'w')as dlfile:
                    dlfile.write("__MiyamizuDesign__encryptionFile__\n")
            else:
                ok=False
                senx = True
                return senx