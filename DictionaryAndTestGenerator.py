#-------------------------------------------------------------------------------
# Name:        Р СР С•Р Т‘РЎС“Р В»РЎРЉ1
# Purpose:
#
# Author:      tmp
#
# Created:     16.04.2017
# Copyright:   (c) tmp 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unicodedata
import random

a1 = ['CYRILLIC SMALL LETTER SHORT I', 'CYRILLIC SMALL LETTER TSE',
      'CYRILLIC SMALL LETTER U', 'CYRILLIC SMALL LETTER KA',
      'CYRILLIC SMALL LETTER IE', 'CYRILLIC SMALL LETTER EN',
      'CYRILLIC SMALL LETTER GHE', 'CYRILLIC SMALL LETTER SHA',
      'CYRILLIC SMALL LETTER SHCHA', 'CYRILLIC SMALL LETTER ZE',
      'CYRILLIC SMALL LETTER HA', 'CYRILLIC SMALL LETTER HARD SIGN',
      'CYRILLIC SMALL LETTER EF', 'CYRILLIC SMALL LETTER YERU',
      'CYRILLIC SMALL LETTER VE', 'CYRILLIC SMALL LETTER A',
      'CYRILLIC SMALL LETTER PE', 'CYRILLIC SMALL LETTER ER',
      'CYRILLIC SMALL LETTER O', 'CYRILLIC SMALL LETTER EL',
      'CYRILLIC SMALL LETTER DE', 'CYRILLIC SMALL LETTER ZHE',
      'CYRILLIC SMALL LETTER E', 'CYRILLIC SMALL LETTER YA',
      'CYRILLIC SMALL LETTER CHE', 'CYRILLIC SMALL LETTER ES',
      'CYRILLIC SMALL LETTER EM', 'CYRILLIC SMALL LETTER I',
      'CYRILLIC SMALL LETTER TE', 'CYRILLIC SMALL LETTER SOFT SIGN',
      'CYRILLIC SMALL LETTER BE', 'CYRILLIC SMALL LETTER YU',
      'CYRILLIC SMALL LETTER IO']
dictionary1 = [unicodedata.lookup(letter) for letter in a1]
dictionary2 = []
dictionary3 = []
dictionary4 = []

test3 = []
test4 = []


for i in range(33):
    for j in range(33):
        dictionary2.append(dictionary1[i] + dictionary1[j])
        for k in range(33):
            dictionary3.append(dictionary1[i] + dictionary1[j] + dictionary1[k])

a = 0
while a < 50000:
    word = random.sample(dictionary1, k = 4)
    dictionary4.append(word[0] + word[1] + word[2] + word[3])
    a += 1
test1 = dictionary1.copy()
test2 = dictionary2.copy()
test3 = random.sample(dictionary3, k = 50)
test4 = random.sample(dictionary3, k = 100)
dictionaries = [dictionary1, dictionary2, dictionary2, dictionary3, dictionary3, dictionary4, dictionary4]
tests = [test1, test1, test2, test3, test2, test3, test4]


for i in range(7):
    filename = 'united/' + str(i) + '.txt'
    file = open(filename, 'w')
    file.write(str(len(dictionaries[i])) + '\n')
    for dictionary in dictionaries[i]:
        file.write(dictionary + " ")

    file.write('\n' + str(len(tests[i])) + '\n')
    for test in tests[i]:
        file.write(test +' ')

    file.close()
