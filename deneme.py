from flask import Flask
app = Flask(__name__)

@app.route('/')
def deneme():
    return 'deneme..'
@app.route('/search')
def search():
    return "search page"
@app.route('/delete/<string:id>')
def deleteId(id):
    return "ID:" + id



if __name__ == '__main__':
    app.run(debug = True, port=3000)