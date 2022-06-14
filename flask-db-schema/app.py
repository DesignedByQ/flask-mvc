from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    #adding cars for relational example
    cars = db.relationship('Car', backref='userbr')

#adding cars for relational example
class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')