import os
import shutil
import time

src = "C:\\Users\\Andreas Graßl\\Desktop\\Programme\\ATLauncher\\"
dest = "F:\\minecraft\\ATLauncher\\"
def saving():
    start = time.time()
    if os.path.isdir(dest):
        print("deleting old folder..")
        shutil.rmtree(dest)
        print("deleting successful")
    print("copying actual folder..")
    shutil.copytree(src, dest, symlinks=False, ignore=None)
    end = time.time()
    print ("copying successful")
    print ("time elapsed was: " + str(end-start))

saving()