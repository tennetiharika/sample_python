import json
import sys

def flatten(x, name='', out={}):
    # if json is a dictionary,send all the keys to flatten again recursively
    if type(x) is dict:
        for a in x:
            flatten(x[a], name + a + '_', out)
    # if json is a list, loop through the list and send each element to flatten again recursively
    elif type(x) is list:
        i = 0
        for a in x:
            flatten(a, name + str(i) + '_', out)
            i += 1
    # if json is a not a list or dictionary, then write it to the out dict
    else:
        out[name.strip().strip('_')] = x
    
    return out

input_file = sys.argv[1]
output_file = sys.argv[2]

# get input as a dictionary
json_input_data = json.load(open(input_file))
# Given that the input file have JSON with hierarchy result --> data, and data being a list of rows
rows = json_input_data['result']['data']
flattened_jsons = []
for row in rows:
    # Get flattened dictionary
    flattened_jsons.append(flatten(row))

# Get header from flattened dictionary. If header is given as argument then take it
headerList = flattened_jsons[0].keys()
if(len(sys.argv) >= 4):
    headerList = sys.argv[3].split(",")

# create output stream using outputr file name given as an argument
outFile = open(output_file, 'wb')
outFile.write("%s\n" % ','.join(map(str, headerList)))

for flattened_json in flattened_jsons:
    row_list = []
    for header in headerList:
        row_list.append(flattened_json.get(header, ""))
    outFile.write("%s\n" % ','.join(map(str, row_list)))

outFile.close()

print('output file written at:%s' % sys.argv[2])
