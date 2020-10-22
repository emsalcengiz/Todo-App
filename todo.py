from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emsal.cengiz/Desktop/Todo-App/Todo.db'
db = SQLAlchemy(app)


