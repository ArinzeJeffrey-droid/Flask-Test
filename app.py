from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Movie

app = Flask(__name__)
app.config['SECRET_KEY'] = "hafadfadfa"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)







@app.route('/movies', methods=['GET'])
def get_movies():
    pass




if __name__ == "__main__":
    app.run(debug=True)




