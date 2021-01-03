from MovieDAO import MovieDao

movie = {
    'id': 123,
    'price': 12,
    'director': 'Quentin Tarantino',
    'title': 'Pulp Fiction'
}

movie2 = {
    'id': 1234,
    'price': 9,
    'director': 'Francis Ford Coppola',
    'title': 'The Godfather'
}

#returnValue = MovieDao.create(movie)
returnValue = MovieDao.getAll()
print(returnValue)
returnValue = MovieDao.findById(movie2['id'])
print("find By Id")
print(returnValue)
returnValue = MovieDao.update(movie2)
print(returnValue)
returnValue = MovieDao.findById(movie2['id'])
print(returnValue)
returnValue = MovieDao.delete(movie2['id'])
print(returnValue)
returnValue = MovieDao.getAll()
print(returnValue)