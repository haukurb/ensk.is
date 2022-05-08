
import csv
import json

d = dict()
with open("en_US.txt") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for e in tsv_file:
        d[e[0]] = e[1]

print(json.dumps(d))
