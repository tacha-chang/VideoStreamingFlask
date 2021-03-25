from configparser import ConfigParser
import psycopg2
from config import config
comm = '''
'''
#http://localhost:5050/browser/#
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(**params)
        conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="changeme")
        # create a cursor
        cur = conn.cursor()

	      # execute a statement
        print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # cur.execute('SELECT * FROM "Guest"')
        # cur.execute('Show Tables') //can,t use
        #parameters(office,job,phone,datacard)
        office_name = ""
        job = ""
        id_card = ""
        first_name =""
        last_name = ""
        bd=""
        address=""
        phone=""
        create_date =""
        sqlite_insert_with_param = """INSERT INTO "user"
                              ("office_name","job,id_card","first_name","last_name","bd","address","phone","create_date")
                              VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s);"""
        data_tuple = (office_name,job,id_card,first_name,last_name,bd,address,phone,create_date)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()

        # list_table = cur.fetchall()
        # print(list_table)
        # display the PostgreSQL database server version
        # db_version = cur.fetchone()
        # print(db_version)
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect_LOG():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(**params)
        conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="changeme")
        # create a cursor
        cur = conn.cursor()


        TeamID = 1
        Timelog ='03/22/2021, 06:30:54'
        IDCard = 1234
        IN = True
        # CreateCate = '03/22/2021, 06:30:54'

        sqlite_insert_with_param = """INSERT INTO "log"
                              ("log_in","time_log","id_card", "num_camera")
                              VALUES (%s, %s, %s, %s);"""
        data_tuple = (log_in,time_log,id_card, num_camera) #แก้ in เป็นnumberCamera
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def connect_work_time():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(**params)
        conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="changeme")
        # create a cursor
        cur = conn.cursor()
        # CreateCate = '03/22/2021, 06:30:54'

        sqlite_insert_with_param = """INSERT INTO "babana_work_time"
                              ("id_card","work_date","arrival","depart","status","work_hr","paid")
                              VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        data_tuple = (id_card, work_date, arrival, depart,status,work_hr,paid) #แก้ in เป็นnumberCamera
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect_use_count_number():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="changeme")
        cur = conn.cursor()
        cur.execute('SELECT "TemID","IDCard" FROM "Log" ORDER BY "TemID" DESC')  #
        row = cur.fetchone()
        print(row[0]) #ล่าสุด
        '''
                cur = conn.cursor()
                cur.execute('SELECT "TemID","IDCard" FROM "Log" ORDER BY "TemID" DESC')  #
                row = cur.fetchone()
                print(row[0]) '''
        temID = row[0] +1
        print(temID)
        # while row is not None:
        #     print(row)
        #     print(row[0])
        #     row = cur.fetchone()
        # conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def connect_work_time():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(**params)
        conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="changeme")
        # create a cursor
        cur = conn.cursor()
        # CreateCate = '03/22/2021, 06:30:54'

        sqlite_insert_with_param = """INSERT INTO "babana_work_time"
                              ("id_card","work_date","arrival","depart","status","work_hr","paid")
                              VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        data_tuple = (id_card, work_date, arrival, depart,status,work_hr,paid) #แก้ in เป็นnumberCamera
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def connect_job():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="changeme")
        normal_rate = 70
        overtime_rate = 100
        job = "developer"
        cur = conn.cursor()
        sqlite_insert_with_param = """INSERT INTO "p/hr"
                              ( "normal_rate","overtime_rate","job")
                              VALUES (%s, %s, %s);"""
        data_tuple = (normal_rate,overtime_rate,job) #แก้ in เป็นnumberCamera
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')







if __name__ == '__main__':
    connect_job()
    
