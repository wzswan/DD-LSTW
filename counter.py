from collections import Counter
import csv

element_counts = Counter()
with open('/home/wzswan/Downloads/github/DD-LSTW/stock.txt') as f:
    for line in f:
        element_counts.update(line.strip().split(':'))

print element_counts

with open('stock_count.csv', "wb") as f:
    w = csv.DictWriter(f,element_counts.keys())
    w.writeheader()
    w.writerow(element_counts)
