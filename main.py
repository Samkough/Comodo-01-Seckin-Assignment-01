import csv
import sys
import sqlite3
import os

# creates the main parts to connecting to a database
conn = sqlite3.connect(":memory:")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS seckin(Time INTEGER, Duration INTEGER, SrcDevice TEXT, DstDevice TEXT, Protocol INTEGER, SrcPort INTEGER, DstPort INTEGER, SrcPackets INTEGER, DstPackets INTEGER, SrcBytes INTEGER, DstBytes INTEGER)")
create_table()

script_dir = os.path.dirname(r'C:\Users\sammy\Desktop\DOWNLOADS\PROGRAMMING\Comodo\_Data-Analysis') #<-- absolute dir the script is in
rel_path = "_Data-Analysis/netflow_day-02.csv"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, 'rb') as fin:
        csv_reader = csv.DictReader(fin)
        to_db = [(i['Time'], i['Duration'], i['SrcDevice'], i['DstDevice'], i['Protocol'], i['SrcPort'], i['DstPort'], i['SrcPackets'], i['DstPackets'], i['SrcBytes'], i['DstBytes']) for i in csv_reader]

c.executemany("INSERT INTO seckin(Time INTEGER, Duration INTEGER, SrcDevice TEXT, DstDevice TEXT, Protocol INTEGER, SrcPort INTEGER, DstPort INTEGER, SrcPackets INTEGER, DstPackets INTEGER, SrcBytes INTEGER, DstBytes INTEGER) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
c.commit()
c.close()
