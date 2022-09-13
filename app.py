from flask import Flask, render_template
from livereload import Server

config = {
    "DEBUG": True,  # run app in debug mode
    'TEMPLATES_AUTO_RELOAD': True
}

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index-v2')
def index2():
    return render_template('index-v2.html')


if __name__ == '__main__':
    app.config.from_mapping(config)

    server = Server(app.wsgi_app)
    # server.watch
    server.serve()
