from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form["search"]

        result = wikipedia.summary(search, sentences=5)
        return f"<h1>{result}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
