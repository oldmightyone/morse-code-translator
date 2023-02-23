from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("text_to_morse"))


@app.route("/text-morse")
def text_to_morse():
    return render_template("text-morse.html")


@app.route("/morse-text")
def morse_to_text():
    return render_template("morse-text.html")

if __name__ == '__main__':
    app.run(debug=True)