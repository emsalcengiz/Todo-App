from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emsal.cengiz/Desktop/Todo-App/Todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos = todos)

@app.route("/add", methods=["GET", "POST"])
def addTodo():
    title = request.form.get("title")
    content = request.form.get("content")

    newTodo = Todo(title=title, content=content, complete= False)

    db.session.remove(newTodo)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<int:id>", methods=["GET"])
def complete_Todo(id):
    todo = Todo.query.filter_by(id=id).first()
    if (todo.complete == False):
        todo.complete = True
    else:
        todo.comlete = False
    db.session.commit()
    return redirect(url_for("index"))
    
    


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)


   
if __name__ == "__main__":
    app.run(debug=True, port=3000)
