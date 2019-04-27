
#!/usr/bin/python
#
# this script moves log files that are more than 24hrs old 
#

import glob
import os, time, sys

temppath = "/var/www/html/temps/"
tempext = "*.json"
tempdest = "/var/greenhouse/temps/"

picpath = "/var/www/html/pictures/"
picext = "*.jpg"
picdest = "/var/greenhouse/pictures/"

now = time.time()
oneday = 86400

def movefiles(path, ext, dest):
    for thefile in glob.glob(path + ext):
        if os.stat(os.path.join(path, thefile)).st_mtime < now - oneday:
            print("moving " + thefile + " to " + dest + os.path.basename(thefile))
            os.rename(thefile, dest + os.path.basename(thefile))

movefiles(temppath, tempext, tempdest)
movefiles(picpath, picext, picdest)
