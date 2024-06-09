from flask import Flask, request
from main import RequestPilot

app = Flask(__name__)


@app.route("/authenticate-token", methods=['POST'])
def authenticate_token():
    return RequestPilot(request).authenticate_token()


@app.route("/authenticate-login", methods=['POST'])
def authenticate_login():
    return RequestPilot(request).authenticate_login()


@app.route("/get-user-data", methods=['GET', 'POST'])
def get_user_data():
    return RequestPilot(request).get_user_data()


@app.route("/register-user", methods=['POST'])
def register_user():
    return RequestPilot(request).register_user()


@app.route("/register-group", methods=['POST'])
def register_group():
    return RequestPilot(request).register_group()


@app.route("/register-task", methods=['GET', 'POST'])
def register_task():
    return RequestPilot(request).register_task()


@app.route("/delete-user", methods=['GET', 'POST'])
def delete_user():
    return RequestPilot(request).delete_user()


@app.route("/delete-group", methods=['GET', 'POST'])
def delete_group():
    return RequestPilot(request).delete_group()


@app.route("/delete-task", methods=['GET', 'POST'])
def delete_task():
    return RequestPilot(request).delete_task()


@app.route("/logout-user", methods=['POST'])
def logout_user():
    print("/logout-user")
    return RequestPilot(request).logout_user()


app.run(host="0.0.0.0", port=5000, debug=True)
