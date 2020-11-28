from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#app initialization and configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = "hafadfadfa"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['TESTING'] = True
db = SQLAlchemy(app)

from models import *



#adding records to the db
@app.before_first_request
def add_movie_records():
    db.create_all()
    movies = Movie.query.all()
    if not movies:
        movie1 = Movie(movie_name="Titanic")
        movie2 = Movie(movie_name="Rome")
        db.session.add_all([movie1, movie2])
        db.session.commit()



@app.route('/', methods=['GET'])
def get_movies():
    #querying the data for the records
    movies = Movie.query.all()
    if not movies:
        return jsonify({ "message": "No records"}), 404
    #parsing the data to be a readable json response
    output = []
    for movie in movies:
        movie_data = {}
        movie_data['id'] = movie.id
        movie_data['movie_name'] = movie.movie_name
        movie_data['relese_date'] = movie.relese_date
        output.append(movie_data)
    return jsonify({ "Movie": output }), 200




if __name__ == "__main__":
    app.run(debug=True)




