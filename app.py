from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    message = "mesaj gidecek mi !!"
    return render_template("index.html", number = 2020,number_two = 2030, message = message)


if __name__ == '__main__':
    app.run(debug = True, port=3000)