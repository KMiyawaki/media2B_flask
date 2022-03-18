# -*- coding: UTF-8 -*-
from flask import Flask

g_app = Flask(__name__)


@g_app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    g_app.run(host="0.0.0.0", port="5000", debug=True)
