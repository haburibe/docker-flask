# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'


def main():
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    main()
