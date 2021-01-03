import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",

    database="datarepresentation"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE Movies(id INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(100), Director VARCHAR(100), Price INT)"

mycursor.execute(sql) 