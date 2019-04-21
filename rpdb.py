# imports
import pymysql
from sqlalchemy import create_engine
import pandas as pd

# Function to read a table from the database
def read_table(table):
	cs  = 'mysql+pymysql://root:root@35.246.218.28/run_moves'
	engine = create_engine(cs)
	Ssql = f'SELECT * FROM {table}'
	return pd.read_sql(Ssql,engine)

def read_table_sql(table, Ssql):
	cs  = 'mysql+pymysql://root:root@35.246.218.28/run_moves'
	engine = create_engine(cs)
	return pd.read_sql(Ssql,engine)	
	
def export_table(dataframe, table, METHOD='replace'):
	cs  = 'mysql+pymysql://root:root@35.246.218.28/run_moves'
	engine = create_engine(cs)
	dataframe.to_sql(con=engine, name=table,  if_exists= METHOD)