import sqlite3
import pandas 

my_feature_tables = {}
db = sqlite3.connect( 'features.db3' )
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table_name = table_name[0]
    table = pandas.read_sql_query("SELECT * from %s" % table_name, db)
    my_feature_tables.update( { table_name: table } ) 

print( my_feature_tables ) 
