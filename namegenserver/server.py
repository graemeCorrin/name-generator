from flask import render_template, jsonify
from namegenserver.app import *
import datetime
from namegenserver.generator import namegenerator


@app.route('/', methods=['GET', 'POST'])
def index():
    print(os.environ['APP_SETTINGS'])
    return render_template('index.html')


@app.route("/name", methods=['POST'])
def get_name():
    name = namegenerator.generatre_name()
    return jsonify({str(datetime.datetime.now()): name})


if __name__ == '__main__':
    app.run()
