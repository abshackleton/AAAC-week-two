import random
x = random.randint(0, 10)
print(x)

from random import *
x = randint(0, 10)
print(x)

import os
current_dir = os.getcwd()
print('1: ', current_dir)
print('2: ', os.listdir())
os.mkdir("AUTOMATION COURSE TEST")
print('3: ', os.listdir())
os.chdir(current_dir + '\\AUTOMATION COURSE TEST')
print('4: ', os.getcwd())
print('5: ', os.listdir())

# this line changes the active location back to where it was when we started
os.chdir(current_dir)

import os
import csv

print(os.listdir())
os.system("copy *.csv results.csv")
print(os.listdir())

with open('results.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(', '.join(row))