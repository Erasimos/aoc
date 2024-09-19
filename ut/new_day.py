import shutil
import sys
import os


def create_new_day(day_template, new_day, year):
    new_file_name = os.getcwd() + '/' + year + '/day_' + str(new_day) + '.py'
    shutil.copy(day_template, new_file_name)
    with open(os.getcwd() + '/' + year + '/input/day_' + str(new_day) + '.txt' , 'w') as fp:
        pass

if __name__ == '__main__':
    new_day = sys.argv[1]
    year = sys.argv[2]
    template_file = os.getcwd() + '/ut/' + 'day_template.py'
    create_new_day(template_file, new_day, year)