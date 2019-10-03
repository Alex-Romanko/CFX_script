import os
import shutil
import csv
import operator
from pathlib import Path

if not os.path.exists(Path('../CFX_file_archive')):
    os.mkdir(Path('../CFX_file_archive'))

#print (os.getcwd())
os.chdir (Path('../CFX_files/'))
#print (os.getcwd())

for CFX_file in os.listdir(os.getcwd()):
    # print (str(CFX_file))

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

    form_dict = {}
    for key in sample_dict:
        for value in sample_dict[key]:
            # print (value)
            if value == 'NaN':
                value = 38
            try:
                value = round(float (value), 1)
                if key in form_dict:
                    form_dict[key].append(value)
                else:
                    form_dict[key] = [value]
            except:
                
                if key in form_dict:
                    form_dict[key].append(value)
                else:
                    form_dict[key] = [value]
            

    destination = Path('../CFX_file_archive')
    source = './' + str(CFX_file)
    shutil.move(source, destination)


    os.chdir (Path('../'))
    #print (os.getcwd())
    with open('Data_Table_Diagn.csv', 'a+') as f:
        f.write(str(CFX_file))
        f.write('\n')
        for key in form_dict.keys():
            f.write("%s,%s\n"%(key,form_dict[key]))
    os.chdir (Path('./CFX_files'))


    #print (file_name)
if __name__ == "__main__":
    pass
