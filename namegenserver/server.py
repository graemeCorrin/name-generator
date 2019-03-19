from flask import render_template, jsonify, request
from namegenserver.app import *
import datetime
import json
from namegenserver.generator import namegenerator


@app.route('/', methods=['GET', 'POST'])
def index():
    print(os.environ['APP_SETTINGS'])
    return render_template('index.html')


@app.route("/name", methods=['POST'])
def get_name():

    data: dict = json.loads(request.data.decode())

    seed = data.get('seed', '')

    name = namegenerator.generate_name(seed)
    return jsonify({str(datetime.datetime.now()): name})


if __name__ == '__main__':
    app.run()
