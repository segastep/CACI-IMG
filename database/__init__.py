from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Column = db.Column
Model = db.Model


from database.model import Test
