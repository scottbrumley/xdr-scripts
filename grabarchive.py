import shutil
import os
import socket
import time

def getAndCompress(folder):
    myhost = socket.gethostname()
    mytime = time.time()
    zip = "grab-" + myhost + "-" + str(mytime) + ".zip"
    
    try:
        zipRet = shutil.make_archive(zip, 'zip', folder)
    except:
        pass
    return zipRet

