from flask import Flask, jsonify, request
from flask import abort
from engine import Engine
from flask_cors import CORS

engine = []
g_class_sum = []


def assemble_data(class_sum, class_info):
    data = {'classSum': class_sum}
    for c in class_info:
        data[c['courseName']] = c['courseHour']
    return data


app = Flask(__name__)
CORS(app)


@app.route('/api/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    class_table = engine[0].grade[int(course_id) - 1].course_table
    data = {'classNumber': g_class_sum[0], 'classTable': class_table}
    return jsonify(data)


@app.route('/api/course/go', methods=['POST'])
def create_course():
    if not request.json or not 'classNumber' in request.json:
        abort(400)
    class_sum = request.json['classNumber']
    class_info = request.json['courseInfo']

    g_class_sum = []
    engine = []
    g_class_sum.append(int(class_sum))
    engine.append(Engine(assemble_data(class_sum, class_info)))
    engine[0].start_engine()
    return jsonify({'status': 'ok'}), 201


@app.route('/api/course/<int:course_id>/upload', methods=['POST'])
def upload(course_id):
    if not request.json or not 'fileName' in request.json:
        abort(400)
    file_name = request.json['fileName']
    engine[0].grade[int(course_id) - 1].class_data = file_name
    return jsonify({'status': 'ok'}), 201


@app.route('/api/file/<int:course_id>', methods=['GET'])
def get_course_data(course_id):
    file_name = engine[0].grade[int(course_id) - 1].class_data
    return jsonify({'file': file_name})


@app.route('/api/search/<string:file_name>', methods=['GET'])
def search(file_name):
    for i in range(g_class_sum[0]):
        if file_name == engine[0].grade[i].class_data:
            return jsonify({'file': file_name, 'classIndex': i + 1}), 200
    return jsonify({'file': file_name, 'classIndex': -1}), 200

if __name__ == '__main__':
    app.run(debug=True)
