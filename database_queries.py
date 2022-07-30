from flask import jsonify, request
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'darshan'
app.config['MYSQL_DATABASE_DB'] = 'rest_api'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
def welcome():
    return "welcome"
def courses1():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM courses"
        cursor.execute(query)
        result = cursor.fetchall()
        op = []
        conn.commit()
        for data in range(len(result)):
            co = {
                'name': result[data][0],
                'id': result[data][1],
                'desc': result[data][2]
            }
            op.append(co)
        return jsonify({"courses": op})
    except:
        return "not available"

def course_id(iid):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM courses"
        cursor.execute(query)
        result = cursor.fetchall()
        op = []
        conn.commit()
        for data in range(len(result)):
            co = {
                'name': result[data][0],
                'id': result[data][1],
                'desc': result[data][2]
            }
            op.append(co)
        return jsonify({"course": op[iid-1]})
    except:
        return "not available"

def add_data1():
    try:
        json = request.get_json()
        name = json['name']
        id = json['id']
        desc = json['descp']
        if name and id and desc and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            query = "INSERT INTO COURSES(name, id, descp) values(%s, %s, %s)"
            binddata = (name, id, desc)
            cursor.execute(query, binddata)
            conn.commit()
            responce = jsonify('Course added successfully')
            responce.status_code = 200
            return responce
        else:
            return "course not added"
    except:
        return "not available"
