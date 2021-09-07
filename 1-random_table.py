import sqlite3 as sql
import sys
import random

script= sys.argv[0]
database=sys.argv[1]

def main():
	"""This program reads an empty .db file, creates a table with just one field
	and fills it with 100000 random numbers between 10.0 and 25.0.
	"""
	assert len(sys.argv)==2, 'Introduce a file, e.g. survey.db'
	createdata(database)
	filltable(database)
	

def createdata(database):
	query="CREATE TABLE Pressure(reading real not null);"
	connection = sql.connect(database)
	cursor = connection.cursor()
	cursor.execute(query)
	connection.close()

def filltable(database):
	query = "INSERT INTO Pressure(reading) VALUES (?);"
	connection = sql.connect(database)
	cursor = connection.cursor()
	for i in range(100000):
	  ran = round(random.uniform(10.0, 25.0) , 2)
	  print( i+1, "of", len(range(100000)), ":", ran)
	  cursor.execute(query, [ran])
	cursor.close()
	connection.commit()
	connection.close
	  
if __name__ == '__main__':
	main()
