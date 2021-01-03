# HDip Data Analytics 2020 

# Data Representation Project

### Lecturer: Andrew Beatty

### Student: Damien Connolly

### Student Number: G00340321
******************************************************************************************************************************

#### Purpose

Build a python Flask server with a REST API that performs CRUD operations on a database table, and create a
html web interface that uses AJAX to connect to the server to perform the CRUD operations. The 'MySQL' package
is used to access and update the sql database.

********************************************************************************************************************************

#### Repository files

server.py - The Flask server to perform the CRUD operations

MovieDAO.py - Library file loaded by 'server.py', to execute the sql operations

createDatabase.py - Code to create the database

index.html - The web interface that issues AJAX commands to 'server' to read/update the sql tables

testMovieDAO.py - Script used to test CRUD operations

initdb.sql - Sql script that could be used to create database table

requirements.txt - Text file containing environment context for running the code

***********************************************************************************************************************************************************

#### To Run

MySQL will need to be installed first (if it is not already present). 

For instructions: https://dev.mysql.com/doc/mysql-installation-excerpt/5.5/en/windows-install-archive.html 

Download and include python option

Open a terminal or command prompt

Navigate to the folder with requirements.txt

run: pip install -r requirements.txt

Installation of dependencies is complete

In the command prompt run python server.py, this starts the server running at 127.0.0.1:5000

In a browser address bar open http://127.0.0.1:5000/index.html - this starts the web interface that uses AJAX to perform database I/O via the server 

***********************************************************************************************************************************************************************
