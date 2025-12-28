from flask import Flask, render_template, request, jsonify
import json
import datetime
from pathlib import Path

app = Flask(__name__)

class ToDoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if Path(self.filename).exists():
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title, description='', reminder_date=None):
        task = {
            'id': max([t['id'] for t in self.tasks], default=0) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'reminder_date': reminder_date,
            'notified': False
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_all_tasks(self):
        return sorted(self.tasks, key=lambda x: x['id'], reverse=True)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        return True

    def update_task(self, task_id, title, description, reminder_date):
        for task in self.tasks:
            if task['id'] == task_id:
                task['title'] = title
                task['description'] = description
                task['reminder_date'] = reminder_date
                task['notified'] = False  # Reset notification flag when reminder changes
                self.save_tasks()
                return task
        return None

    def mark_notified(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['notified'] = True
                self.save_tasks()
                return task
        return None

todo_app = ToDoApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todo_app.get_all_tasks())

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = todo_app.add_task(
        data.get('title'),
        data.get('description', ''),
        data.get('reminder_date')
    )
    return jsonify(task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = todo_app.update_task(
        task_id,
        data.get('title'),
        data.get('description', ''),
        data.get('reminder_date')
    )
    return jsonify(task) if task else ('', 404)

@app.route('/api/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = todo_app.complete_task(task_id)
    return jsonify(task) if task else ('', 404)

@app.route('/api/tasks/<int:task_id>/notified', methods=['POST'])
def mark_notified(task_id):
    task = todo_app.mark_notified(task_id)
    return jsonify(task) if task else ('', 404)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    todo_app.delete_task(task_id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
