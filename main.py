import datetime

from application import salary
from datetime import date

from db import people
# def print_hi(name):
#     print(f'Hi, {name}')

if __name__ == '__main__':
    # print_hi('PyCharm')
    print(date.today())
    salary.calculate_salary(1,2)
    people.get_employees('Альфайрий')



