import os,sys
import jpype

JAR_PATH = ''

def work(file_name):

    jvmPath = jpype.getDefaultJVMPath()
    jvmArg = “ -Djava.class.path = ” + JAR_PATH
    if not jpype.isJVMStarted():
        jpype.startJVM(jvmPath, jvmArg)

    PClass = jpype.JClass('Demo')
    
    f = open(filename,'r')   
    PCheck = PClass(f.read()) 
    Result = PCheck.run()
    f.close()
    jpype.shutdownJVM() 
    return Result