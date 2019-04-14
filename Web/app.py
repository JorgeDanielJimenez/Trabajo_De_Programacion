from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/house')
def house():
    return render_template('house.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route("/pcb")
def pcb():
    return render_template('pcb.html')


if __name__ == '__main__':
    app.run(debug=True)
