from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)

  @app.route("/movies")
  @requires_auth("get:movies")
  def getMovies(reqBody):
    movies = Movies.query.all()
    moviesList = []
    for movie in movies:
      movie_info = movie.format()
      moviesList.append(movie_info)
    return jsonify(
      {
        "success": True,
        "total_movies": len(movies),
        "movies": moviesList
      }
    )
  
  @app.route('/movies/<int:movieId>', methods=['GET'])
  @requires_auth("get:movies")
  def getMovie(reqBody,movieId):
      try:
          movieInfo = Movies.query.get(movieId).format()
          return movieInfo
      except Exception:
            abort(404)

  @app.route("/movies", methods=["POST"])
  @requires_auth("post:movie")
  def postMovies(reqBody):
    body = request.get_json()
    try:
      newMovie = Movies(
        title = body['title'],
        release_date = body['release_date']
      )
      newMovie.insert()
      return jsonify(
        {
          "success": True,
          "Movie": newMovie.format()
        }
      )
    except:
      abort(422)

  @app.route('/movies/<int:movieId>', methods=['PATCH'])
  @requires_auth('update:movie')
  def updateMovie(reqBody,movieId):
      movie = Movies.query.get(movieId)
      if movie==None:
          abort(404)
      try:
          body = request.get_json()
          movie.title = body['title']
          movie.release_date = body['release_date']
          movie.update()
          return movie.format()
      except Exception:
          abort(422)

  @app.route('/movies/<int:movieId>', methods=['DELETE'])
  @requires_auth('delete:movie')
  def deleteMovie(reqBody,movieId):
      movie = Movies.query.get(movieId)
      if movie==None:
          abort(404)
      try:
          movie.delete()
          return "DELETED"
      except Exception:
          abort(422)


  @app.route("/actors", methods=["POST"])
  @requires_auth("post:actor")
  def postActor(reqBody):
    body = request.get_json()
    try:
      newActor = Actors(
        name = body['name'],
        age = body['age'],
        gender = body['gender']
      )
      newActor.insert()
      return jsonify(
        {
          "success": True,
          "Actor": newActor.format()
        }
      )
    except:
      abort(422)

  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def getActors(reqBody):
    actors = Actors.query.all()
    actorsList = []
    for actor in actors:
      actor_info = actor.format()
      actorsList.append(actor_info)
    return jsonify(
      {
        "success": True,
        "total_actors": len(actors),
        "actors": actorsList
      }
    )

  @app.route('/actors/<int:actorId>', methods=['GET'])
  @requires_auth('get:actors')
  def getActor(reqBody,actorId):
      try:
          actorInfo = Actors.query.get(actorId).format()
          return actorInfo
      except Exception:
            abort(404)

  @app.route('/actors/<int:actorId>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def deleteActor(reqBody,actorId):
      actor = Actors.query.get(actorId)
      if actor==None:
          abort(404)
      try:
          actor.delete()
          return "DELETED"
      except Exception:
          abort(422)

  @app.route('/actors/<int:actorId>', methods=['PATCH'])
  @requires_auth('update:actor')
  def updateActor(reqBody,actorId):
      body = request.get_json()
      actor = Actors.query.get(actorId)
      if actor==None:
          abort(404)
      try:
          actor.name = body['name']
          actor.age = body['age']
          actor.gender = body['gender']
          actor.update()
          return actor.format()
      except Exception:
          abort(422)

  @app.errorhandler(403)
  def forbidden_error(error):
    return jsonify({
        'error': 'Forbidden',
        'message': 'You do not have permission to access this resource.'
     }), 403

  # Error Handling
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422

  @app.errorhandler(404)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404
  
  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          "success": False,
          "error": error.error.get("code"),
          "message": error.error.get("description")
      }),error.status_code

  return app
app=create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
