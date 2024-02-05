from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    data = {"Name": "Warisara", "Age" : 30, "Job" : "Student", "Gender" : "Female"}
    return render_template("index.html", mydata = data)

@app.route('/about')
def about():
    product =["Apple", "Banana", "Orange", "Grape"]
    return render_template("about.html", myproduct = product)

@app.route('/admin')
def profile():
    name = "Bhum"
    age = 23
    return render_template("admin.html", username = name)

@app.route('/sendData')
def signupform():
    fname = request.args.get("fname")
    description = request.args.get("description")
    return render_template("thankyou.html", data = {"fname": fname, "description": description})

#debug mode is true, to show error message
if __name__ == "__main__":
    app.run(debug=True)