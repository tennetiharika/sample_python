import json
import sys

def flatten_json(y):
    flatten_out = []

    def flatten(x, name='', out={}):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_', out)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_', out)
                i += 1
        else:
            out[name.strip().strip('_')] = x
        return out
    
    rows = y['result']['data']
    for row in rows:
        flatten_row = flatten(row)
        flatten_out.append(flatten_row)
    return flatten_out

input_file = sys.argv[1]
output_file = sys.argv[2]

f = open(input_file)
data_file = json.load(f)
flat = flatten_json(data_file)

keys = flat[0].keys()

outFile = open(output_file, 'wb')
outFile.write("%s\n" % ','.join(map(str, keys)))

for row in flat:
    row_list = []
    for key in keys:
        row_list.append(row[key])
    outFile.write("%s\n" % ','.join(map(str, row_list)))

outFile.close()

print('output file written at:', sys.argv[2])
