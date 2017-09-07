import re
from collections import Counter
import csv
from numpy import character
from numpy.core.defchararray import lower
def question():
    c = Counter
    with open('fai.txt','r') as f:
        for line in f.readlines():
            if line == '\n':
                continue

            words = re.findall('\w*',line)
            c.update(words)
    csvfile = open('fai_count.csv','wb+')
    w = csv.writer(csvfile)
    for item in c.items():
        w.writer(item)
    csvfile.close()
