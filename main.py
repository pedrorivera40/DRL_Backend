from flask import Flask, request, jsonify
from handler.person_handler import PersonHandler

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/Person")
def get_persons():
    if (not request.args): return PersonHandler().getAllAccounts()
    return jsonify(ERROR="Malformed URL"), 404


# Launching the application...
if __name__ == '__main__':
    app.run()
