import xlsxwriter
import time
import shutil
import os
import datetime
import psycopg2
conn = psycopg2.connect(
host="localhost",
database="postgres",
user="postgres",
password="changeme")
a_list = [1, 2, 3, 4]


def writer_report():  #officer
    workbook = xlsxwriter.Workbook('name_file.xlsx')
    worksheet = workbook.add_worksheet()

    my_list = [ID_card, Name ,Day, Date, Time,Arrival,Status]  #writehead
    for col_num, data in enumerate(my_list):
        worksheet.write(0, col_num, data,bold)
    #ลูปลงข้อมูล


    #ลูปคำนวนStatus


def writer_daily():

    workbook = xlsxwriter.Workbook('name_file.xlsx')
    worksheet = workbook.add_worksheet()

    my_list = [ID_card, Name ,Day, Date, Time,Arrival,Depart,Office]  #writehead
    for col_num, data in enumerate(my_list):
        worksheet.write(0, col_num, data)



    workbook.close()
def writer_month():
    return

def test():
    workbook = xlsxwriter.Workbook('name_file.xlsx')
    worksheet = workbook.add_worksheet()

    my_list = [ID_card, Name ,Day, Date,Arrival,Depart,Status,Late]  #writehead
    for col_num, data in enumerate(my_list):
        worksheet.write(0, col_num, data,bold)
    # x = datetime.datetime.now()
    # print(x.strftime("%x"))   #ex. 	12/31/18
    # print(x.strftime("%A"))  #Weekday, full version	Wednesda
    expenses = (
     ['Rent', 1000],
     ['Gas',   100],
     ['Food',  300],
     ['Gym',    50],)
    expenses = (
      [600100376,'Rent',day,date,9.00 ],
      ['Gas',   100],
      ['Food',  300],
      ['Gym',    50],)
    row = 1
    col = 0

    #
    for item, cost in (expenses):
        worksheet.write(row, col,     id) #id
        worksheet.write(row, col + 1, name) #name
        worksheet.write(row, col + 2, day) #day
        worksheet.write(row, col + 3, date) #date
        worksheet.write(row, col + 4, Arrival) #Arrival
        worksheet.write(row, col + 5, Depart) #depart
        worksheet.write(row, col + 6, Status) #Late on time absent
        worksheet.write(row, col + 7, Late) #Status fulltime parttime late absent  no checkin no checkout
        # worksheet.write(row, col + 8, ) #Late on time absent

        row += 1
    worksheet.write(0, 8, 'Total',       bold)
    worksheet.write(0, 8 , '=SUM(B2:B5)')
    workbook.close()
test()


''''
def Excel_Daily(x ,camera_out):
    file_name = x + 'xlsx' #date
    workbook = xlsxwriter.Workbook('file_name')
    worksheet = workbook.add_worksheet()
    my_list = [[1, 1, 1, 1, 1],
           [2, 2, 2, 2, 1],
           [3, 3, 3, 3, 1],
           [4, 4, 4, 4, 1],
           [5, 5, 5, 5, 1]]
    for row_num, row_data in enumerate(my_list):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(row_num, col_num, col_data)
    workbook.close()
    return 0
def Excel_month():
    return 0
'''
