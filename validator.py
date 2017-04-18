import os
from sys import argv

name, file1_path, file2_path = argv
file1 = open(file1_path, 'r')
file2 = open(file2_path, 'r')
big1 = []
big2 = []
for line in file1:
    big1.append(line.split().sort())

for line in file2:
    big2.append(line.split().sort())

for b1, b2 in zip(big1, big2):
    if b1 != b2:
        print('erroe', b1, b2, sep='\n')
        exit(1)



