from flask import Flask, jsonify, request

app = Flask(__name__)

courses = [{'name': 'python programming',
            'id': 1,
            'desc': 'valuable course'},
           {'name': 'java programming',
            'id': 2,
            'desc': 'impressive course'},
           {'name': 'c programming',
            'id': 3,
            'desc': 'aggressive course'},
           {'name': 'c++ programming',
            'id': 4,
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

@app.route("/courses", methods=['POST'])
#except get method, other http methods should runned in 2 terminals
#the command used in 2nd terminal is "curl -i -H "Content-type:Application/json" -X POST http://localhost:5000/courses"
#where -i => status code, -H => header format, "Content-type:Application/json" => return type format, -X POST => http method and thn url
def post_course():
    course = request.get_json()
    data = {
        'name': course['name'],
        'id': course['id'],
        'desc': course['desc']
    }
    courses.append(data)
    return jsonify({'Created': data})

@app.route("/courses/<int:id>", methods=["PUT"])
#here when you specifiy "id" you should provide it in form of index number
#the command used in 2nd terminal is "curl -i -H "Content-type:Application/json" -X PUT http://localhost:5000/courses/"id_number(index number)""
#where -i => status code, -H => header format, "Content-type:Application/json" => return type format, -X POST => http method and thn url
def put_value(id):
    id = request.get_json()
    try:
        courses[(id["id"])-1]['desc'] = id["desc"]
        courses[(id["id"])-1]['name'] = id["name"]
        courses[(id["id"])-1]['id'] = id["id"]
        return jsonify({'Courses': courses[(id["id"])-1]})
    except:
        return "course not found"

@app.route("/courses/<int:id>", methods=["DELETE"])
def delete_course(id):
    id = request.get_json()
    try:
        courses.remove(courses[(id['id'])-1])
        return jsonify({"result": True})
    except:
        return "course id not found"

if __name__ == "__main__":
    app.run(debug=True)