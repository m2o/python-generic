#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

tasks = []

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/todo/api/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/todo/api/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    matchedtasks = filter(lambda t: t['id']==task_id,tasks)
    taskcnt = len(matchedtasks)
    if taskcnt == 0:
        abort(404)
    elif taskcnt == 1:
        return jsonify({'task':matchedtasks[0]})
    else:
        raise AssertionError("tasks with duplicate ids")

@app.route('/todo/api/tasks',methods=['POST'])
def create_task():
    if request.json and request.json.get('name') is not None:
        task = {'id': tasks[-1]['id']+1 if len(tasks) else 1,
                'name':request.json['name']}
        tasks.append(task)
    else:
        abort(404)

    return jsonify({'task':task}),201

if __name__ == '__main__':
    app.run(debug = True)
