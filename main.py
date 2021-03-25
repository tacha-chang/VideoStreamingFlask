from flask import Flask, render_template,request,redirect, Response,url_for
from camera import VideoCamera
from Card_reading import reader_card
from recognition import verify_photo
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from pop_up_NO_USE import popupmsg
import os
import schedule
import psycopg2
#icon = os.path.join('static', 'icon') #connect FOLDER Photo
Photo_card_read = os.path.join('static', 'Photo_card_read')
ver = []
app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = icon
app.config['UPLOAD_FOLDER'] = Photo_card_read
#app.use("/static", express.static('./static/')); js
conn = psycopg2.connect(
host="localhost",
database="postgres",
user="postgres",
password="changeme")
@app.after_request
def after_request(response):
    if response == "run" :
        try:
             verify_photo()
        except Exception as e:
             print("hello")

        app.logger.info("after_request")
        return response
    else :
        return response
@app.route('/home')
def home():

    return render_template('home.html')

@app.route('/')
def index():
    after_request("run")
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/verify')
def verify():
     # print("1")
     # check = verify_photo()
     # print(check)
     return 'hello'


@app.route('/Role')
def Role():

    return render_template('role.html')

@app.route('/Admin')
def Admin():
    return render_template('login.html')

@app.route('/admin_regis',methods=['POST'])
def admin_regis():
    data=[]
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']  #เก็บดาต้าจากตรงนี้
        data.append(username)
        data.append(password)
        if username == "addmin" and password == "admin123":
            print("Welcome Admin")
            return redirect(url_for('Cardreading_OFFICE'))##อ่านการ์ดของ อ่านการ์ด


@app.route('/register_office')
def register_office():
    data_profile = reader_card()
    file_img = data_profile[31]
    print(file_img)
    #img_profile = os.path.join(app.config['UPLOAD_FOLDER'], file_img)#รูปจากบัตร
    img_profile = os.listdir('static/img/temp_img/')
    return render_template('register.html',img_profile = img_profile, data_profile = data_profile)

@app.route('/register')
def register():
    data_profile = reader_card()
    file_img = data_profile[31]
    print(file_img)
    #img_profile = os.path.join(app.config['UPLOAD_FOLDER'], file_img)#รูปจากบัตร
    img_profile = os.listdir('static/img/temp_img/')
    return render_template('register.html',img_profile = img_profile, data_profile = data_profile)



@app.route('/Cardreading')
def Cardreading():
    # popupmsg()
    return render_template('Cardreading.html') #แก้ให้route ไป Guest

@app.route('/Cardreading_office')
def Cardreading_office():
    # popupmsg()
    return render_template('Cardreading.html') #แก้ให้route ไป user


@app.route('/information')
def information():
    return render_template('fill_in.html')

@app.route('/fill_in',methods = ['POST'])
def fill_in():
    data = []
    if request.method == "POST":
        PHONE_NUMBER = request.form['PHONE_NUMBER']
        explain = request.form['explain']
        Office = request.form['Office']  #เก็บดาต้าจากตรงนี้
        data.append(PHONE_NUMBER)
        data.append(explain)
        data.append(Office)
        #input เข้าdatabase สร้าง2 ตัว
        if Office == "duck":
            print("Welcome duck")
            return redirect(url_for('success_KMITL')) #function
        if Office == "banana":
            print("Welcome banana")
            return redirect(url_for('success_KMUTMD')) #function

        #return redirect(url_for('success_KMITL'))
@app.route('/success_KMITL')
def success_KMITL():
    data_profile = reader_card()
    #delete temp_img SIAM-ID txt.file  บรรทัดสุดท้าย
    return render_template('success_banana.html', data_profile = data_profile)


@app.route('/success_KMUTMD')
def success_KMUTMD():
    data_profile = reader_card()
    return render_template('success_duck.html', data_profile = data_profile)



@app.route('/show_duck')
def show_duck():
    with conn:
        cur =conn.cursor()
        cur.execute('SELECT * FROM "user"')
        rows =cur.fetchall()

        return render_template('show_duck.html', datas = rows)

@app.route('/show_banana')
def show_banana():
    with conn:
        cur =conn.cursor()
        cur.execute('SELECT * FROM "user"')
        rows =cur.fetchall()
        return render_template('show_banana.html', datas = rows)








if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
