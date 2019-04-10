from flask import render_template, jsonify, request
from namegenserver.app import *
import datetime
import json
from namegenserver.generator.generators import full_name_generator


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Return main page of the app
    """

    print(os.environ['APP_SETTINGS'])
    return render_template('index.html')


@app.route("/name", methods=['POST'])
def get_name():
    """
    Get random name
    """

    data: dict = json.loads(request.data.decode())
    seed = data.get('seed', '')
    name = full_name_generator.generate_name(seed)
    return jsonify({str(datetime.datetime.now()): name})


if __name__ == '__main__':
    app.run()
