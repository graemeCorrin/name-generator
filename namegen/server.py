from flask import render_template, jsonify
from namegen.app import *
import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    print(os.environ['APP_SETTINGS'])
    return render_template('index.html')


@app.route("/name", methods=['POST'])
def get_name():

    return jsonify({str(datetime.datetime.now()): 'bob'})


if __name__ == '__main__':
    app.run()
