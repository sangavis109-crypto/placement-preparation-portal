from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/interview')
def interview():
    return render_template('interview.html')


@app.route('/coding')
def coding():
    return render_template('coding.html')


@app.route('/aptitude')
def aptitude():
    return render_template('aptitude.html')

@app.route('/completion')
def completion():
    return render_template('completion.html')   


if __name__ == '__main__':
    app.run(debug=True)