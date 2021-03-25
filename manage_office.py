#####จัดการเรื่องการเก็บไฟล์แต่ละoffice
import os
import requests
import shutil
from parinya import LINE
from Card_reading import reader_card
import datetime
url = 'https://notify-api.line.me/api/notify'
token_kmitl = 'SuWZzmcKMMH5RvFaglsCT8jWlIDEBltqjEwhNR7aepd'
token_kmutnb = ''
token_kmutt = ''

path_Office_kmitl = 'C:/Users/Tacha/VideoStreamingFlask/Office/kmitl'
path_Office_kmutnb = ''
path_Office_kmutt = ''

path_Excel_kmitl = 'C:/Users/Tacha/VideoStreamingFlask/Excel/kmitl'
path_Excel_kmutnb = ''
path_Excel_kmutt = ''
'''
token = 'Hkf9EI7Ilafe4uinK9Iibud1p8OJVMBz8hOLHTCL0gs'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token_kmitl}
msg = 'Hello LINE Notify'
r = requests.post(url, headers=headers, data = {'message':msg})

print (r.text)
'''
test =  reader_card()
x = ["Ford", "Volvo", "BMW","Ford", "Volvo", "BMW", "Volvo", "BMW", "Volvo", "BMW"] #ตัวแปรอ่านค่า
def insert_guest(data,Office,explain):
    path_file = 'C:/Users/Tacha/VideoStreamingFlask/CARD_READER/SIAM-ID/1101801037083.jpg'    #data[31] #file_phot form CARD_READER
    Office = Office
    if Office == 'kmitl':
        files=[
          ('imageFile',('1101801037083.jpg',open('C:/Users/Tacha/VideoStreamingFlask/CARD_READER/SIAM-ID/1101801037083.jpg','rb'),'image/jpeg'))
        ]

        headers = {'Authorization': 'Bearer '+token_kmitl}
        msg = 'accestime :'+ data[1] +' ' +data[0]+ "              " + data[6]+' ' + data[7] +' '+ data[8] +' detail: '+explain
        print(path_file)
        r = requests.request("POST",url, headers=headers,files = files,data = {'message':msg})
        path_dest ='C:/Users/Tacha/VideoStreamingFlask/kmitl/Guest'
    #    dest = shutil.move(path_source, path_dest) # ยังไม่ได้ใว่ source_file
        print("send file to line" + Office)
    elif Office == 'kmutnb':
        return 0
    elif Office == 'kmutt':
        return 0
insert_guest(data =test ,Office = "kmitl" ,explain = "I am here to meet Ms.Kree")


def remove_data_guest(folder_path):
    now = time.time()
    folder = folder_path
    files = [os.path.join(folder, filename) for filename in os.listdir(folder)]  #ลบข้อมูลfile ใน 90วัน
    for filename in files:
        if (now - os.stat(filename).st_mtime) > 7776000:
            command = "rm {0}".format(filename)
            subprocess.call(command, shell=True)
