import tfidf
import numpy
import collections

fai_result ={}

data = tfidf.TfIdf()
fai = data.csv2dict("/home/wzswan/Downloads/github/DD-LSTW/fai.csv")
fai_count = collections.Counter(fai)
pe = data.csv2dict("/home/wzswan/Downloads/github/DD-LSTW/pe.csv")
stock = data.csv2dict("/home/wzswan/Downloads/github/DD-LSTW/stock.csv")
print fai
print fai_count
#print pe
#print stock
table = tfidf.TfIdf()
table.add_document("FAI",fai)
table.add_document("PE",pe)
table.add_document("STOCK_INDEX",stock)

#print table

#print "key 16 is:%s"%(table.similarities(["16"]))


fai_result = {'24':table.similarities(["24"]), '25': table.similarities(["25"]),'26':table.similarities(["26"]) ,
'27':table.similarities(["27"]),'20': table.similarities(["20"]),'21':table.similarities(["21"]),
'22':table.similarities(["22"]) ,'23':table.similarities(["23"]) ,'28':table.similarities(["28"])
,'29': table.similarities(["29"]), '38':table.similarities(["38"]) ,'15':table.similarities(["15"]) ,
'17':table.similarities(["17"]) ,'16':table.similarities(["16"]) ,'33':table.similarities(["33"]) ,
'18':table.similarities(["18"]) ,'30':table.similarities(["30"]) ,'37':table.similarities(["37"]) ,
'35':table.similarities(["35"]) ,'34':table.similarities(["34"]) ,'19':table.similarities(["19"]) ,'32':table.similarities(["32"])}

#print fai_result
