from flask import Flask,render_template_string
app = Flask(__name__)

@app.route('/')
def index():
    return 'fist page..'


if __name__ == '__main__':
    app.run(debug = True, port=3000)