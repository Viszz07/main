from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Example data structure to store tasks
tasks = {
    "todo": ["Task 1", "Task 2"],
    "in_progress": ["Task 3"],
    "done": ["Task 4"]
}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    status = request.form.get('status')
    
    if task_name and status:
        tasks[status].append(task_name)
    
    return redirect('/')

@app.route('/move_task', methods=['POST'])
def move_task():
    task_name = request.form.get('task_name')
    current_status = request.form.get('current_status')
    new_status = request.form.get('new_status')
    
    if task_name and current_status and new_status:
        tasks[current_status].remove(task_name)
        tasks[new_status].append(task_name)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)
