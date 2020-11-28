from app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name= db.Column(db.String(200), nullable=False)
    relese_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return self.movie_name