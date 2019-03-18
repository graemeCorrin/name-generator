from namegen.app import *


@app.route('/')
def hello():
    print(os.environ['APP_SETTINGS'])
    return "Hello World!"


if __name__ == '__main__':
    app.run()
