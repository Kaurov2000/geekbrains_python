# encoding = 'utf-8'

from sys import argv

script_name, work_hours, salary, bonus = argv

wage =round(float(work_hours) * float(salary) + float(bonus),2)

print(wage)