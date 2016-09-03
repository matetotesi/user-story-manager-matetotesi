from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/story")
def story_template():
    return render_template("default.html")


if __name__ == "__main__":
    app.run(debug=True)
