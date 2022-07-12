from flask import Flask, request, jsonify, make_response, send_from_directory
import json

app = Flask(__name__)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


if __name__ == '__main__':
    app.run()
