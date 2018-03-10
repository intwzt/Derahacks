from flask import Flask, jsonify
from flask import abort
from flask import request

from engine import Engine

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
