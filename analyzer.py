# The following script was written by Sofia Chepovetskaya

import nltk
import config

d = {}

for i in range(len(config.text.split('  '))):
    d[config.text.split('  ')[i]] = config.gram_list[i]

s = input()

if s == 'Океан никак не безопаснее бассейна, поэтому следите за энергией своих ныряльщиков и пловцов.':
    parser = nltk.ChartParser(d[config.text.split('  ')[0]])
    for tree in parser.parse(config.text.split('  ')[0].replace(',', '').replace('.', '').lower().split()):
        print(tree)
        tree.draw()
elif s in d:
    parser = nltk.ChartParser(d[s])
    for tree in parser.parse(s.replace(',', '').replace('.', '').lower().split()):
        print(tree)
        tree.draw()
else:
    print('No Data')
