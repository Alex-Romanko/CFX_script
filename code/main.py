import os
from os.path import devnull
import shutil
import csv
import operator

print (os.getcwd())
os.chdir ('../CFX_files/')
print (os.getcwd())


'''
data_conteiner = []
with open ('admin_2019-09-14 14-09-54_CFX96N6NEW.csv', 'r') as f:
    print (f.name, f.mode)
    for line in f:
        data_conteiner.append(list(line.split()))


for i in data_conteiner:
    print(i)

'''

file_name = 'default'
sortedlist = []
start_sequence =['Well', 'Fluor', 'Target', 'Content', 'Sample', 'Cq', 'Starting Quantity (SQ)']
with open ('admin_2019-09-14 14-09-54_CFX96N6NEW.csv', 'r') as f:
    file_name = str(f.name)
    csv_reader = csv.reader(f, delimiter=',')
    for index, line in enumerate(csv_reader):
        if index > 17:
            sortedlist = sorted(csv_reader, key=operator.itemgetter(4, 0, 1), reverse=False)

len_list = len (sortedlist)
print (len_list)

sample = ''
data_store = []
counter = 0
for i in sortedlist:
    if i[4] == sample:
        data_store.append(i[5])
    sample = i[4]
    counter +=1
for j in data_store:
    print(j)

print (data_store)
print (counter)

















print (file_name)
if __name__ == "__main__":
    pass