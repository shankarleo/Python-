import os
import shutil
import datetime
import schedule
import time

source = "D:\Source"
dest = "D:\Backups"

def c(s,d):
    today=datetime.date.today()
    dd = os.path.join(d,str(today))

    try:
        shutil.copytree(s,dd)
        print(f"Folder Copied:{dd}")

    except Exception as e:
        print(f"Folder alreday exists in:{dd}")


c(source,dest)