import os

from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return request.data


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

