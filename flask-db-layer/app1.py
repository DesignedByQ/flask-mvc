from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app1 = Flask(__name__)

app1.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db1 = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)