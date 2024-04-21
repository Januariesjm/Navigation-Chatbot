from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/execute_task', methods=['POST'])
def execute_task():
    app_name = request.form['app_name']
    task_description = request.form['task_description']

    process = subprocess.Popen(["python", "scripts/task_executor.py", "--app", app_name], stdin=subprocess.PIPE)
    process.communicate(input=task_description.encode())

    return render_template('index.html', message='Task execution initiated successfully!')

if __name__ == '__main__':
    app.run(debug=True)
