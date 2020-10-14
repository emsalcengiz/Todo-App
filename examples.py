from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    numbers = [1,4,7,8,9,6,3]
    message = "mesaj gidecek mi !!"
    return render_template("index_ex.html", number = 2020,number_two = 2030, message = message, numbers = numbers)

@app.route("/sum", methods = ["GET","POST"])
def sum():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("sum.html", total = int(number2) + int(number2))
        
    else:
        #return render_template("sum.html")
        return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug = True, port=3000)