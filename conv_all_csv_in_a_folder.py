import json
import csv

for x in range(1, 11):
    f = open('9447440523-Huge'+str(x)+'.csv', 'r')
    reader = csv.DictReader(f)
    i=0;
    jsonoutput = str(x)+'.json'
    with open(jsonoutput, 'a') as f:
            f.write('[')
            for x in reader:
                json.dump(x, f)
                f.write(',')
            f.write(']')
