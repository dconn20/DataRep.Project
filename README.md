# HDip Data Analytics 2020 Data Representation project

### Lecturer: Andrew Beatty

### Student: Damien Connolly

### Student Number: G00340321
******************************************************************************************************************************

#### Purpose
Demonstrate a python Flask server with a REST API that performs CRUD operations on two sql tables, and an
html web interface that uses AJAX to connect to the server to perform the CRUD operations. The 'MySQL' package
is used to access and update the sql database.

#### Repository files

server.py - the Flask server to perform the CRUD operations
MovieDAO.py - library file loaded by 'server.py', to execute the sql operations
createDatabase.py - code to create the database
index.html - the web interface that issues AJAX commands to 'server' to read/update the sql tables
requirements.txt - text file containing environment context for running the code


To run
'MySQL' will need to be installed first (if it is not already present). 
For instructions: https://dev.mysql.com/doc/mysql-installation-excerpt/5.5/en/windows-install-archive.html 
Download and include python option.

At the command prompt: If 'flask' and 'mysql-connector' are not yet installed:
pip install flask
pip install mysql-connector

python createDatabase.py - this code uses 'MySQL' to create a database

set FLASK-APP server - 'server' is the name of the server here. flask run - this starts the server running at 127.0.0.1:5000

In a browser address bar: http://127.0.0.1:5000/DRproject.html - starts the web interface that uses AJAX to perform database I/O via the server CRUD operations can then be performed against both tables.
