import os
import shutil
import sys
from types import coroutine
src=r'C:\Users\e32lsm\F'    #src資料夾
dest=r'C:\Users\e32lsm\D'   #dest資料夾

if not os.path.isdir(src):
    print('src is not a dir')
    sys.exit(2)

if not os.path.isdir(dest):
    print('dest is not a dir')
    sys.exit(2)

for dir_path, dir_names, file_names in os.walk(src):

    folder = dir_path.replace(src+'\\', '') #若不在SCR，取出資料夾名稱

    dest_path=dest    
    # print('目前路徑:', dir_path)
    # print('資料夾:', folder)    
    if folder == src:
        coroutine
    else:        
        dest_path = os.path.join(dest, folder)        
        if not os.path.isdir(dest_path): #沒有資料夾路徑
            os.makedirs(dest_path)       #就建立
    
    for f in file_names:        
        src_path = os.path.join(dir_path, f)
        save_path = os.path.join(dest_path, f) 

        if not os.path.isfile(save_path):
            shutil.copy2(src_path, save_path)
        else:
            src_time = int(os.path.getmtime(src_path))
            dest_time = int(os.path.getmtime(save_path))
            if src_time> dest_time:
                shutil.copy2(src_path, save_path)

