from flask import Flask, jsonify

app = Flask(__name__)

courses = [{'name': 'python programming',
            'id': '1',
            'desc': 'valuable course'},
           {'name': 'java programming',
            'id': '2',
            'desc': 'impressive course'},
           {'name': 'c programming',
            'id': '3',
            'desc': 'aggressive course'},
           {'name': 'c++ programming',
            'id': '4',
            'desc': 'awesome course'}
           ]

@app.route('/')
def index():
    return "Welcome"

@app.route("/courses", methods=['GET'])
def get_courses():
    return jsonify({"Courses":courses})

@app.route(f"/courses/<int:id>", methods=['GET'])
def get_by_id(id):
    try:
        return jsonify({"Courses": courses[id-1]})
    except:
        return "Course Not Found"

@app.route("/courses/<string:name>")
def get_by_course_name(name):
    try:
        if name == "pythonprogramming" or name == "Pythonprogramming" or name == "python programming" or name == "Python programming" or name == "python" or name == "Python" or name == "Py":
            return jsonify({'Course': courses[0]})
        elif name == "javaprogramming" or name == "JavaProgramming" or name == "java programming" or name == "Java Programming" or name == "java" or name == "Java":
            return jsonify({'Course': courses[1]})
        elif name == "cprogramming" or name == "CProgramming" or name == "c programming" or name == "C Programming" or name == "c" or name == "C":
            return jsonify({'Course': courses[2]})
        elif name == "c++programming" or name == "C++Programming" or name == "c++ programming" or name == "C++ Programming" or name == "C++" or name == "c++":
            return jsonify({'Course': courses[4]})
        elif name == "programming" or name == "Programming":
            return jsonify({'Courses': courses})
        else:
            return "Course Not Found"
    except:
        return "course not found"

@app.route("/courses", methods= ['POST'])
def post_course():
    course = {'name': 'java script programming',
            'id': '5',
            'desc': 'awesome course'}
    courses.append(course)
    return jsonify({'created': course})

if __name__ == "__main__":
    app.run(debug=True)