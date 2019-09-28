import os
from os.path import devnull
import shutil
import csv
import operator


if not os.path.exists('../CFX_file_archive'):
    os.mkdir('../CFX_file_archive')

#print (os.getcwd())
os.chdir ('../CFX_files/')
#print (os.getcwd())

for CFX_file in os.listdir(os.getcwd()):
    #print (str(CFX_file))

    file_name = 'default'
    sortedlist = []
    start_sequence =['Well', 'Fluor', 'Target', 'Content', 'Sample', 'Cq', 'Starting Quantity (SQ)']
    with open (CFX_file, 'r') as f:
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

    shutil.move('./' + str(CFX_file), '../CFX_file_archive')


    os.chdir ('../')
    #print (os.getcwd())
    with open('Data_Table_Diagn.csv', 'a+') as f:
        for key in sample_dict.keys():
            f.write("%s,%s\n"%(key,sample_dict[key]))
    os.chdir ('./CFX_files')


    #print (file_name)
if __name__ == "__main__":
    pass
