# ItemCatalog

### File Descriptions 

* templates : Contain HTML files that would be rendered in UI
* database_setup.py : Used by SQL Alchemy to create ORM mapping with SQlite DB
* itemcatalogwithusers.db : DB to be used while authentication of user 
* itemcatalog.db : DB to be used while authentication of user 
* populatedb2.py : Used to provide inital data for the database with itemcatalogwithusers.db 
* populatedb.py : Used to provide inital data for the database with itemcatalog.db 
* itemcatalog.py : Main business logic for the project is here with routing , HTML escaping and authentication 

### How to run the project ?


* Use any VM like vagrant to host the files [ I used vagrant with SQLite installed ] - Not a requirement
* Install SQlite database 
* Install Python 2.7.12
* Install packages Flask and SQLAlchemy 
* By accessing the folder run `python itemcatalog.py`
