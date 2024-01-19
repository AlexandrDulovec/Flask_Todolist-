from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=enumerate(tasks))

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    task_notes = request.form.get('notes')
    if task_description:
        task = {'description': task_description, 'notes': task_notes, 'completed': False}
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_index>')
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
