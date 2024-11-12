from flask import Flask, request
from flask_cors import CORS
from receiver import wait_for_new_messages
from html_sender import send_html


app = Flask(__name__)

CORS(app)


@app.get("/")
def home():
    return "this is the home page"


@app.get("/check")
def check_unread():
    emails = wait_for_new_messages()

    for email in emails:
        send_html(email)

    return "success"


if __name__ == '__main__':
    app.run()
