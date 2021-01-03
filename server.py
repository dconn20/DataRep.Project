from flask import Flask, jsonify, url_for, request, redirect, abort

from MovieDAO import MovieDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"

# Get all
@app.route('/movies')
def getAll():
    return jsonify(MovieDao.getAll())

# Find by id
@app.route('/movies/<int:id>')
def findById(id):
    return jsonify(MovieDao.findById(id))

# Create
@app.route('/movies', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    movie = {
        "title": request.json["title"],
        "director": request.json["director"],
        "price": request.json["price"]
    }

    return jsonify(MovieDao.create(movie))
    

# Update
@app.route('/movies/<int:id>', methods=['PUT'])
def update(id):
    foundMovie = MovieDao.findById(id)
    if foundMovie == {}:
        return jsonify({}), 404
    currentMovie = foundMovie
    if 'title' in request.json:
        currentMovie['title'] = request.json['title']
    if 'director' in request.json:
        currentMovie['director'] = request.json['director']
    if 'price' in request.json:
        currentMovie['price'] = request.json['price']
    MovieDao.update(currentMovie)

    return jsonify(currentMovie)

# Delete
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete(id):
    MovieDao.delete(id)

    return jsonify({"done":True})

# Main
if __name__ == "__main__":
    app.run(debug=True)
