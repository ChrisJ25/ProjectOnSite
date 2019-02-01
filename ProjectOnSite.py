from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = 'Mr.Frost'
    name = 'Frost Agent'
    return render_template('index.html', author=author, name=name)

@app.route('/zancudo.html')
def job_preview():
    return render_template('zancudo.html')

if __name__ == '__main__':
    app.run()
