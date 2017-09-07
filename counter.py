from collections import Counter
import csv
import weithter
weight_countht_result = {}
element_counts = Counter()
output_value = {}
table = weithter.CoreFunction()
with open('/home/wzswan/Downloads/github/DD-LSTW/stock.txt') as f:
    for line in f:
        element_counts.update(line.strip().split(':'))

#print element_counts
#print len(element_counts)
for k in element_counts:
    weight_countht_result[k]= int(10/(element_counts[k]/1.41))
#print weight_countht_result




for k in weight_countht_result:
    output_value[k] = table.Simgoid(weight_countht_result[k])
    #output_value[k] = table.Linear(weight_countht_result[k])

print output_value
