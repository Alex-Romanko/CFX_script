import os
import shutil
import csv
import operator
from pathlib import Path
from pprint import pprint
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
# you have to run the file from "./code/" directory


# autorization
CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '16Ox7jX0ljQ5r6Zc7492uaW583-3wDS9HlREXVRNCY9Q'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)


# here is how to insert data to the particular line
# now data must be in format of a como separated string
# insert_data = "a777, na, 32, na, na, 33, 32, 32, 34, 22, 23"  # the sample of data


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
                value = str(round(float(value), 1))
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


def data_preparation(sample_name, form_dict):
    transitional_data_storrage = []
    transitional_data_storrage.append(sample_name)
    transitional_data_storrage.extend(form_dict.get(sample_name))
    return(transitional_data_storrage)


def prep_data_to_push(transitional_data_storrage):
    insert_data = ''
    for number, value in enumerate(transitional_data_storrage):
        if number <= len(transitional_data_storrage)-2:
            insert_data = insert_data + value + ', '
        else:
            insert_data = insert_data + value
    return(insert_data)


def data_writer_headder():
    with open('Data_Table_Diagn.csv', 'a+') as f:
        f.write(str(CFX_file))
        f.write('\n')


def sample_data_writer(insert_data):
    with open('Data_Table_Diagn.csv', 'a+') as f:
        f.write(insert_data)
        f.write('\n')


def move_file_to_archive(CFX_file):
    destination = Path('../CFX_file_archive')
    # source = './' + str(CFX_file)
    source = str(Path(CFX_file))  # it's work
    shutil.move(source, destination)


def strar_script():
    if not os.path.exists(Path('../CFX_file_archive')):
        os.mkdir(Path('../CFX_file_archive'))
    os.chdir(Path('../CFX_files/'))


strar_script()
for CFX_file in os.listdir(os.getcwd()):
    if CFX_file in os.listdir(Path('../CFX_file_archive')):
        continue
    sortedlist = CFX_file_reader(CFX_file)
    sample_dict = sample_dict_former(sortedlist)
    form_dict = formating_dict(sample_dict)
    move_file_to_archive(CFX_file)
    os.chdir(Path('../'))
    samples_from_protocol = sorted(form_dict.keys())
    data_writer_headder()  # writes protocol id

    for sample_name in samples_from_protocol:
        insert_data = prep_data_to_push(data_preparation(sample_name, form_dict))  # now we can push or write data on each step of cycle
        # print(insert_data, "===> pushed")
        sample_data_writer(insert_data)

    # data_writer(form_dict)
    os.chdir(Path('./CFX_files'))
