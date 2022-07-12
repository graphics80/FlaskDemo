from flask import Flask, request

app = Flask(__name__)


@app.route('/api/students', methods = ['POST'])
def postStudents():
    return request.method + " students not yet implemented!"

@app.route('/api/students', methods = ['GET'])
def getStudents():
    return request.method + " students not yet implemented!"


if __name__ == '__main__':
    app.run()
