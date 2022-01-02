from flask import Flask
from werkzeug.exceptions import NotFound
import json

from services import root_dir, nice_json


app = Flask(__name__)

with open("{}/database/movies.json".format(root_dir()), "r") as f:
    movies = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movies/<movieId>", methods=['GET'])
def movie_info(movieId):
    if movieId not in movies:
        raise NotFound

    result = movies[movieId]
    result["uri"] = "/movies/{}".format(movieId)

    return nice_json(result)


@app.route("/movies", methods=['GET'])
def movie_record():
    return nice_json(movies)


if __name__ == "__main__":
    app.run(port=5001, debug=True)

