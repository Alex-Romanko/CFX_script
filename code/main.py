import os
import shutil
import csv

print (os.getcwd())
os.chdir ('../CFX_files/')
print (os.getcwd())



with open ('admin_2019-09-14 14-09-54_CFX96N6NEW.csv', 'r') as f:
    print (f.name, f.mode)
    for line in f:
        print(line)




try:
    os.chdir ('../datatable')
except FileNotFoundError:
    os.chdir ('../')
    os.mkdir ('datatable')
os.chdir ('../datatable')



if __name__ == "__main__":
    pass