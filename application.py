from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hey this is last simple Hello World application in flask!'

@app.route('/inside1')
def hello_world1():
    return 'INSODE 1 Hey this is last simple Hello World application in flask!'

@app.route('/inside2')
def hello_world2():
    return 'INSODE 2 Hey this is last simple Hello World application in flask!'


if __name__ == '__main__':
    app.run()
