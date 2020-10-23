from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emsal.cengiz/Desktop/Todo-App/Todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def addTodo():
    title = request.form.get("title")
    content = request.form.get("content")
    newTodo = Todo( title=title, content=content, complete= False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index.html"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

   
if __name__ == "__main__":
    app.run(debug=True, port=3000)
