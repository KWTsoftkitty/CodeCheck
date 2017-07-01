# -*-coding:utf-8-*
import os,sys
import Dead_Loop

Check_Rule = {
    "Dead_Loop":Dead_Loop.work,
#    "Date_type":"int,long,short,char,uint,uchar,uloong,ushort"
    }

class Check():
    def __init__(self,Rule,File,path):
        self.Rule = Rule
        self.File = File
        self.path = path
        self.info = []

    def Create_txt(self):
        f = open(self.path,'w')
        f.writelines(self.info)
        f.close()
            

    def go_Check(self):
        self.info = Check_Rule[self.Rule](self.File)
        self.Create_txt()

if __name__ ==  "__main__":
    print "Welcome to CodeCheck!"
    print "Let's do a good job!"

    ucRule = sys,argv[1]
    ucFile = sys.argv[2]
    ucPath = sys.argv[3]

    Case = Check(ucRule,ucFile,ucPath)
    Case.go_Check()


    

