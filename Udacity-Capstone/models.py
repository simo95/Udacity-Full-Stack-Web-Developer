
import os
from sqlalchemy import Column, String, Integer, create_engine, Table, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import json
# from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

database_path = os.environ.get("DATABASE_PATH")
# Base = declarative_base()
db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()
    # Base.metadata.create_all(bind=create_engine(database_path))

class dbFunctions(db.Model):
    __abstract__ = True
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

# association_table = Table('association',
#     Column('movie_id', ForeignKey('Movie.id'), primary_key=True),
#     Column('actor_id', ForeignKey('Actor.id'), primary_key=True)
# )

class Movies(dbFunctions):
    __tablename__ = 'Movie'

    id = Column(Integer,  primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(String, nullable=False)
    # actors = relationship("Actors",
    #                 secondary=association_table)


    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

class Actors(dbFunctions):
    __tablename__ = 'Actor'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
