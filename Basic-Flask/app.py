from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask Framework</h1>"

@app.route('/about')
def about():
    return "<h1>Hello About</h1>"

@app.route('/admin')
def profile():
    return "<h1>Hello Admin</h1>"

#Dynamic route
@app.route('/user/<name>/<age>')
def member(name, age):
    return "<h1>Hello : {}, Age : {}</h1>".format(name, age)


if __name__ == "__main__":
    app.run()