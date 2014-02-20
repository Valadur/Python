import os
import shutil

src = "C:\\Users\\Andreas Graßl\\Desktop\\Programme\\ATLauncher\\"
dest = "F:\\minecraft\\ATLauncher\\"

if os.path.isdir(dest):
    shutil.rmtree(dest);

shutil.copytree(src, dest, symlinks=False, ignore=None)