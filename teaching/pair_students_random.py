import pandas as pd
import random

df = pd.read_excel('phys15a_list.xlsx', sheet_name='homework') 
students = df['Name'].tolist()
print(students)

random.shuffle(students)

print(students)

itr = iter(students)
listitr = [itr]*2

groups = zip(*[iter(students)]*2)

for first_student, second_student in groups:
    print("\n",first_student, "and", second_student)
