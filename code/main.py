import os
from os.path import devnull
import shutil
import csv
import operator

print (os.getcwd())
os.chdir ('../CFX_files/')
print (os.getcwd())


file_name = 'default'
sortedlist = []
start_sequence =['Well', 'Fluor', 'Target', 'Content', 'Sample', 'Cq', 'Starting Quantity (SQ)']
with open ('admin_2019-09-14 14-09-54_CFX96N6NEW.csv', 'r') as f:
    file_name = str(f.name)
    csv_reader = csv.reader(f, delimiter=',')
    for  line in csv_reader:
        if line == start_sequence:
            sortedlist = sorted(csv_reader, key=operator.itemgetter(4, 0, 1), reverse=False)




sample_dict = {}
for elem in sortedlist:
    if elem[4] in sample_dict:
        sample_dict[elem[4]].append(elem[5])
    else:
        sample_dict[elem[4]] = [elem[5]]

print (sample_dict['T12345'])









print (file_name)
if __name__ == "__main__":
    pass