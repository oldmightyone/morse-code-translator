from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("text_to_morse"))


@app.route("/text-morse", methods=["GET", "POST"])
def text_to_morse():
    if request.method == "POST":
        print(request.form.get("input"))
        print(request.form.get("check"))
        return redirect(url_for("morse_to_text"))

    return render_template("text-morse.html")


@app.route("/morse-text", methods=["GET", "POST"])
def morse_to_text():
    if request.method == "POST":
        print(request.form.get("input"))
        return redirect(url_for("text_to_morse"))

    return render_template("morse-text.html")


if __name__ == '__main__':
    app.run(debug=True)