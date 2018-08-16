"""Niestety program dla ćwiczenia drugiego nie do końca spełnia swoje założenia, przede wszystkim dlatego, że nie udało
mi się opanować regexa, a nie znalazłem sprytniejszego sposobu na wycięcie adresów. Tym samym program działa, ale widać jak daleko mu do
perfekcji."""


import os
import re
import csv
report={}
urls=[]
nice_urls=[]
with open('today.log',"r") as f:
    for line in f:
        url = re.findall('http(?:s)?:\/\/(?:[\w-]+\.)*([\w-]{1,63})(?:\.(?:\w{3}|\w{2}))(?:$|\/)', line)
        #url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
        urls.append(url)

for line in urls:
    for extra in line:
        nice_urls.append(extra)

for x in nice_urls:
    if not x in report:
        report[x] = 1
    else:
        report[x] +=1

with open('report.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in report.items():
       writer.writerow([key, value])



