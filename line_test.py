from parinya import LINE
import time
import datetime
import psycopg2
conn = psycopg2.connect(
host="localhost",
database="postgres",
user="postgres",
password="changeme")
token_kmitl = 'SuWZzmcKMMH5RvFaglsCT8jWlIDEBltqjEwhNR7aepd'
x = datetime.datetime.now()
print(x.strftime("%x"))   #ex. 	12/31/18
print(x.strftime("%A"))  #Weekday, full version	Wednesday
line = LINE(token_kmitl)
msg ='''Morning report 3/19/2021
Name    Arrival Status
Tachrat 9.00    on time
Kree    9.45    late
'''
line.sendtext(msg)
def line_guest(data): #มีรูปมีข้อความรับ 3 ค่า
    return


def Morning_report(): #รับค่าดาต้าbaseรายวัน
    txt = "Morning report"+ x.strftime("%x") +"\n" +"Name  Arrival Status" +"\n"
    # if Arrival > 9.30:
    #     txt += " late"
    # elif Arrival < 9.30:
    #     txt += " on time"
    # elif Arrival == null:
    #     txt += " absent"
    # txt += "tacharat"
    line.sendtext(txt)

Morning_report()
