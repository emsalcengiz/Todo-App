from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    numbers = [1,4,7,8,9,6,3]
    message = "mesaj gidecek mi !!"
    return render_template("index.html", number = 2020,number_two = 2030, message = message, numbers = numbers)


if __name__ == '__main__':
    app.run(debug = True, port=3000)