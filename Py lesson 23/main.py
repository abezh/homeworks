from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():

    return render_template("main_page.html")

@app.route("/second_page")
def second_page():

    return render_template("second_page.html")

@app.route("/third_page")
def third_page():

    return render_template("third_page.html")

app.run(debug=True)