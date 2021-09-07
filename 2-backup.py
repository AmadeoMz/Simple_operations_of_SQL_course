import sqlite3 as sql
import sys

script= sys.argv[0]
original_db=sys.argv[1]

def main():
	"""This program reads a .db file and stores the numbers
	greater than 20.0 in a previously created file named backup.db

	"""
	assert len(sys.argv)==2, 'Introduce a file, e.g. original.db'
	print('Loading')
	create_table('backup.db')
	fill_table('backup.db')
	print('Done')


def create_table(database):
	query="CREATE TABLE Pressure(reading real not null);"
	connection = sql.connect(database)
	cursor = connection.cursor()
	cursor.execute(query)
	connection.close()

def fill_table(database):
	connection_original = sql.connect(original_db)
	cursor_original = connection_original.cursor()
	connection_backup= sql.connect(database)
	cursor_backup = connection_backup.cursor()

	query_filtering = "SELECT reading FROM Pressure WHERE reading > 20.0;"
	cursor_original.execute(query_filtering)
	data = cursor_original.fetchall()
	assert len(data)>0, 'Something wrong, there is no data extracted from the original file.'

	for record in data:
	  query_fill = "INSERT INTO Pressure(reading) VALUES (?);"
	  cursor_backup.execute(query_fill, [record[0]])

	cursor_original.close()
	cursor_backup.close()
	connection_original.close()
	connection_backup.commit()
	connection_backup.close()

if __name__ == '__main__':
	main()
