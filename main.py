import database_queries
from app import app
from flask import jsonify, request
from flaskext.mysql import MySQL
from database_queries import courses1
from database_queries import course_id
from database_queries import add_data1
from config import mysql


@app.route("/")
def welcome():
    res = database_queries.welcome()
    return res

@app.route("/courses", methods=['GET'])
def courses():
    res = courses1()
    return res

@app.route("/courses/<int:iid>", methods=['GET'])
def courses_id(iid):
    res = course_id(iid)
    return res

@app.route("/courses/add_data", methods=['POST'])
def add_data():
    return add_data1()

if __name__ == "__main__":
    app.run()
