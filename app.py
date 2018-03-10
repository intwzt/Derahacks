from flask import Flask, jsonify
from flask import abort
from flask import request
from flask_cors import CORS

from engine import Engine

app = Flask(__name__)
CORS(app)

engine = []
g_class_sum = []


def assemble_data(class_sum, class_info):
    data = {'classSum': class_sum}
    for c in class_info:
        data[c['courseName']] = c['courseHour']
    return data


@app.route('/api/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    class_table = engine[0].grade[int(course_id)].course_table
    data = {'classNumber': g_class_sum[0], 'classTable': class_table}
    return jsonify(data)


@app.route('/api/course/go', methods=['POST'])
def create_course():
    if not request.json or not 'classNumber' in request.json:
        abort(400)
    class_sum = request.json['classNumber']
    class_info = request.json['courseInfo']

    g_class_sum.append(class_sum)
    engine.append(Engine(assemble_data(class_sum, class_info)))
    engine[0].start_engine()
    return jsonify({'status': 'ok'}), 201


@app.route('/api/course/<int:course_id>/upload', methods=['POST'])
def upload(course_id):
    if not request.json or not 'fileName' in request.json:
        abort(400)
    file_name = request.json['fileName']
    engine[0].grade[course_id].class_data = file_name
    return jsonify({'status': 'ok'}), 201


@app.route('/api/file/<int:course_id>', methods=['GET'])
def get_course(course_id):
    file_name = engine[0].grade[int(course_id)].class_data
    return jsonify(file_name)


@app.route('/api/search', methods=['POST'])
def search():
    if not request.json or not 'fileName' in request.json:
        abort(400)
    key = request.json['fileName']


if __name__ == '__main__':
    app.run(debug=True)
