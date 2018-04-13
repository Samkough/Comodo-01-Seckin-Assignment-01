import csv
import os

script_dir = os.path.dirname(r'C:\Users\sammy\Desktop\DOWNLOADS\PROGRAMMING\Comodo\_Data-Analysis') #<-- absolute dir the script is in
rel_path = "_Data-Analysis/netflow_day-02.csv"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            print(line)
