from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# إعداد الاتصال بقاعدة البيانات
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # ضع كلمة مرورك هنا
        database="quran_center"
    )

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM quran_students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    juz = request.form['juz']
    course = request.form['course'] # (تحفيظ أو دروس تقوية)
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quran_students (name, juz, course) VALUES (%s, %s, %s)", (name, juz, course))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
