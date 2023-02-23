from flask import Flask, render_template, redirect, url_for, request
from morse_code_convertor import MorseCodeConverter

app = Flask(__name__)
converter = MorseCodeConverter()

@app.route("/")
def home():
    return redirect(url_for("text_to_morse"))


@app.route("/text-morse", methods=["GET", "POST"])
def text_to_morse():
    if request.method == "POST":
        to_real_char = None
        if request.form.get("check") == "on":
            to_real_char = True

        code = converter.string_to_code(string=request.form.get("input"), to_real_char=to_real_char)

        return redirect(url_for("morse_to_text", code=code))

    text = None
    try:
        text = request.args['text']
    except:
        pass

    return render_template("text-morse.html", text=text)


@app.route("/morse-text", methods=["GET", "POST"])
def morse_to_text():
    if request.method == "POST":
        text = converter.code_to_string(code=request.form.get("input"))
        return redirect(url_for("text_to_morse", text=text))
    code = None
    try:
        code = request.args['code']
    except:
        pass

    return render_template("morse-text.html", code=code)


if __name__ == '__main__':
    app.run(debug=True)