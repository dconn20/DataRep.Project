import mysql.connector
from mysql.connector import cursor

class MovieDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentation'
        )
        
    # Create
    def create(self, movie):
        cursor = self.db.cursor()
        sql = "insert into Movies (title, director, price) values (%s,%s,%s)"
        values = [
            movie['title'],
            movie['director'],
            movie['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # Get All
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from movies'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    # Find by Id
    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from movies where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        
    # Update
    def update(self, movie):
       cursor = self.db.cursor()
       sql = "update movies set title = %s, director = %s, price = %s where id = %s"
       values = [
           movie['title'],
           movie['director'],
           movie['price'],
           movie['id']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return movie

    # Delete    
    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from movies where id = %s'
       values = [id]
       cursor.execute(sql, values)
       
       return {}


    # Convert to dict
    def convertToDict(self, result):
        colnames = ['id','title', 'director', 'price']
        movie = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                movie[colName] = value
        return movie

MovieDao = MovieDao()