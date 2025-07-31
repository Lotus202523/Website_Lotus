from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/committees")
def committees():
    return render_template("committees.html")

@app.route("/proceedings")
def proceedings():
    return render_template("proceedings.html")

@app.route("/base")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)