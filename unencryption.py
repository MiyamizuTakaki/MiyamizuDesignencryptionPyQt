import json
import re


class uMKencryption():
    def __init__(self, mkfl, mkjm, mkse):
        self.mkfl = mkfl
        self.mkjm = mkjm
        self.mkse = mkse

    def sureency(self):
        sr1 = False
        sr2 = False
        with open(self.mkfl, 'r') as dlfile:
            for dlfiles in dlfile:  ##抬头文件验证
                if dlfiles == "__MiyamizuDesign__encryption__1__\n":
                    sr1 = True
                break
        with open(self.mkjm, 'r') as dlfile:
            for dlfiles in dlfile:
                if dlfiles == "__MiyamizuDesign__encryptionFile__\n":
                    sr2 = True
                break
        if sr1 == True and sr2 == True:
            return True
        else:
            return False

    def uencryption(self):
        jms = []
        jma = []
        u = 0
        with open(self.mkfl, 'r',encoding='utf-8') as dlfile:
            for dlfiles in dlfile:
                if dlfiles == "__MiyamizuDesign__encryption__1__\n":
                    continue
                jms.append(json.loads(dlfiles))
        for jmss in jms:
            u = u+1
        p =0
        with open(self.mkjm, 'r') as dlfile:
            for dlfiles in dlfile:
                if dlfiles == "__MiyamizuDesign__encryptionFile__\n":
                    continue
                for dlfilex in dlfiles:
                    if jms[p][3] == 0:
                        jm = (jms[p][0] * jms[p][1]) - ord(dlfilex)
                    elif jms[p][3] != 0:
                        jm = ord(dlfilex) + jms[p][3]
                    with open(self.mkse, 'a',encoding='utf-8') as dlfiles:
                        dlfiles.write(chr(jm))
                    p = p + 1

