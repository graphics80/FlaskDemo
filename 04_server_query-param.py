from flask import Flask, jsonify, make_response, request
import json

app = Flask(__name__)





@app.route('/api/students', methods = ['GET'])
def get_students():
    f = open('data/students.json')
    data = json.load(f)
    response = make_response(
        jsonify(
                data
            ),
            401,
            )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/students/<id>', methods = ['GET'])
def get_students_by_id(id):
    f = open('data/students.json')
    data = json.load(f)

    # Filter python objects with list comprehensions
    filtered_data = [x for x in data if x['student_id'] == int(id)]

    response = make_response(
        jsonify(
                filtered_data
            ),
            401,
            )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/api/students', methods = ['POST'])
def postStudents():
    return request.method + " students not yet implemented!"


if __name__ == '__main__':
    app.run()
