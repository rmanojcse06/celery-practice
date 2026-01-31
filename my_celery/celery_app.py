from flask import Flask, jsonify
from my_celery.celery_tasks import add
app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>')
def trigger_task(a, b):
    result = add.delay(a, b)
    return jsonify({"task_id": result.id, "status": "Task Scheduled!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
