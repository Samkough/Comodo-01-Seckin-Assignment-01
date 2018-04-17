import sqlite3
import csv
import os

script_dir = os.path.dirname(r'C:\Users\sammy\Desktop\DOWNLOADS\PROGRAMMING\Comodo\_Data-Analysis') #<-- absolute dir the script is in
rel_path = "_Data-Analysis/netflow_day-02.csv"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, 'r') # open the csv data file
next(f, None) # skip the header row
reader = csv.reader(f)

sql = sqlite3.connect('database.db')
cur = sql.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS seckin(Time INTEGER, Duration INTEGER, SrcDevice TEXT, DstDevice TEXT, Protocol INTEGER, SrcPort INTEGER, DstPort INTEGER, SrcPackets INTEGER, DstPackets INTEGER, SrcBytes INTEGER, DstBytes INTEGER)''') # create the table if it doesn't already exist

for row in reader:
	cur.execute("INSERT INTO seckin VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

f.close()
sql.commit()
sql.close()
