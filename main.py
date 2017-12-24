from flask import Flask

app = Flask(__name__)

@app.route("/Home/")
def hello():
    return "<h1>Hello World!</h1>"


# Launching the application...
if __name__ == '__main__':
    app.run()