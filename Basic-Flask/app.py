from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    data = {"Name": "Warisara", "Age" : 30, "Job" : "Student"}
    return render_template("index.html", mydata = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def profile():
    name = "Bhum"
    age = 23
    return render_template("admin.html", username = name)


#debug mode is true, to show error message
if __name__ == "__main__":
    app.run(debug=True)