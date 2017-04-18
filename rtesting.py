from subprocess import Popen,PIPE
import os
import sys

ac = False
solution1 = "main.py"
solution2 = 'C:/Users/tmp/Documents/GitHub/levenshtein_automaton/bin/Release/Trie.exe'
foldername = 'united/'
outfolder1 = 'ans1/'
outfolder2 = 'ans2/'

for i in range(7):
    input_file = foldername + str(i) + '.txt'
    output_file = str(i) + '.txt'
    s = os.system ('python ' + solution1 + " <" + input_file +" >" + outfolder1 + output_file)
    d = os.system (solution2 + " <" + input_file +" >" + outfolder2 + output_file)
    if s != 0 or d != 0:
        print(i, "--------- Runtime Error ---------")
        sys.exit()
    print(i, 'DONE')
    validator = os.system('python ' + 'validator.py' + ' ' + outfolder1 + output_file + ' ' + outfolder2 + output_file)
    if validator != 0:
        print(i, 'errer')
        sys.exit()



#running

