import glob
import os
import time
import subprocess
from PIL import Image
import shutil
'''
path = './facedata/'
list_of_files = glob.glob('facedata/*')
c_time = os.path.getctime(path)
local_time = time.ctime(c_time)
print("ctime (Local time):", local_time) #แปลงไฟล์เป็นเวลาloal
latest_file = max(list_of_files , key=os.path.getctime)
print(latest_file)  #หาไฟล์ล่าสุด ต้องหาtxtไฟล์
im = Image.open(latest_file) #หารูปล่าสุด ไฟล์รูปล่าสุด
im.show()
'''
path_source = 'C:/Users/Tacha/VideoStreamingFlask/Photo/tacharat/tacharat1.png'
path_dest ='C:/Users/Tacha/VideoStreamingFlask/'
dest = shutil.copy(path_source, path_dest) #copyไฟล์
dest = shutil.move(path_source, path_dest) #moveไฟล์

with open("./CARD_READER/SIAM-ID/Data.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
    last_line = lines[-1] #บรรทัดสุดท้าย
x  = last_line.split(",")
print(x)
print(x[0]) #date
print(x[1]) #time
print(x[2]) #idcard
# print(x[3]) gender
print(x[7]) #name
print(x[8]) #lastname
print(x[9]) #birthday
print(x[31]) #photo
print('Number' +x[14] +' ' + x[15]+' ' + x[16]+' ' + x[17]+' ' + x[18]+' ' + x[19]+' ' + x[20]+' ' + x[21]) #address
#


now = time.time()
folder = '<folder_path>'
files = [os.path.join(folder, filename) for filename in os.listdir(folder)]  #ลบข้อมูลfile ใน 90วัน
for filename in files:
    if (now - os.stat(filename).st_mtime) > 7776000:
        command = "rm {0}".format(filename)
        subprocess.call(command, shell=True)
''' ลบข้อมูล90วัน
import os
import datetime
import glob
path = 'enter_path_here'

today = datetime.datetime.today()#gets current time
os.chdir(path) #changing path to current path(same as cd command)

#we are taking current folder, directory and files
#separetly using os.walk function
for root,directories,files in os.walk(path,topdown=False):
    for name in files:
        #this is the last modified time
        t = os.stat(os.path.join(root, name))[8]
        filetime = datetime.datetime.fromtimestamp(t) - today

        #checking if file is more than 7 days old
        #or not if yes then remove them
        if filetime.days <= -7:
            print(os.path.join(root, name), filetime.days)
            os.remove(os.path.join(root, name))
'''
'''
def link(path_file):
    path_file = 'C:/Users/Tacha/VideoStreamingFlask/CARD_READER/SIAM-ID/' + path_file + '.jpg'
    print(path_file)
    c_time = os.path.getctime(path_file)
    local_time = time.ctime(c_time)
    print("ctime (Local time):", local_time) หาเวลาไฟล์ภาพ
link("1101801037083")
'''
