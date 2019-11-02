import os
import shutil
import csv
import operator
from pathlib import Path
# you have to run the file from "./code/" directory


def CFX_file_reader(CFX_file):
    sortedlist = []
    start_sequence = ['Well', 'Fluor', 'Target', 'Content', 'Sample', 'Cq', 'Starting Quantity (SQ)']
    with open(CFX_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for line in csv_reader:
            if line == start_sequence:
                sortedlist = sorted(csv_reader, key=operator.itemgetter(4, 0, 1), reverse=False)
    return (sortedlist)


def sample_dict_former(sortedlist):
    sample_dict = {}
    for elem in sortedlist:
        if elem[4] in sample_dict:
            sample_dict[elem[4]].append(elem[5])
        else:
            sample_dict[elem[4]] = [elem[5]]
    return (sample_dict)


def formating_dict(sample_dict):
    form_dict = {}
    for key in sample_dict:
        for value in sample_dict[key]:
            # print (value)
            if value == 'NaN':
                value = str(value)
            try:
                value = round(float(value), 1)
                if key in form_dict:
                    form_dict[key].append(value)
                else:
                    form_dict[key] = [value]
            except TypeError:
                if key in form_dict:
                    form_dict[key].append(value)
                else:
                    form_dict[key] = [value]
    return (form_dict)


def data_writer(form_dict):
    with open('Data_Table_Diagn.csv', 'a+') as f:
        f.write(str(CFX_file))
        f.write('\n')
        for key in form_dict.keys():
            f.write("%s,%s\n" % (key, form_dict[key]))


def move_file_to_archive(CFX_file):
    destination = Path('../CFX_file_archive')
    # source = './' + str(CFX_file)
    source = str(Path(CFX_file))  # it's work
    shutil.move(source, destination)


def strar_script():
    if not os.path.exists(Path('../CFX_file_archive')):
        os.mkdir(Path('../CFX_file_archive'))
    os.chdir(Path('../CFX_files/'))


if __name__ == "__main__":
    strar_script()
    for CFX_file in os.listdir(os.getcwd()):
        if CFX_file in os.listdir(Path('../CFX_file_archive')):
            continue
        sortedlist = CFX_file_reader(CFX_file)
        sample_dict = sample_dict_former(sortedlist)
        form_dict = formating_dict(sample_dict)
        move_file_to_archive(CFX_file)
        os.chdir(Path('../'))
        data_writer(form_dict)
        os.chdir(Path('./CFX_files'))
