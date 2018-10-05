from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/about")
def index():
    return "We are revamping. Will be back soon!"


if __name__ == "__main__":
    app.run()

