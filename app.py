from flask import Flask, render_template, url_for
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


@app.route('/layout/<int:number>')
def layout(number):
    return render_template(f'layout-{number}.html')


@app.route('/contact')
def contact():
    return "No contact page"


@app.route('/legal')
def legal():
    return "No legal page"


if __name__ == '__main__':
    app.config.from_mapping(config)

    server = Server(app.wsgi_app)
    # server.watch
    server.serve()
