import os
import sys

def create_new_year(new_year):
    folder_path = os.getcwd() + '/' + new_year
    os.mkdir(folder_path)
    os.mkdir(folder_path + '/input')


if __name__ == '__main__':
    new_year = sys.argv[1]
    create_new_year(new_year)