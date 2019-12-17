import json
import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]


output_dict = {}

inputFile = open(input_file_path, "r")
columns = inputFile.readline().split(",")

UniqueParentColumns = []
for col in columns:
    UniqueParentColumns.append(col.split(".")[0])
UniqueParentColumns = list(dict.fromkeys(UniqueParentColumns))

for col in UniqueParentColumns:
    output_dict[col.strip()] = []

row = 0
for x in inputFile:
    values = x.split(",")
    i = 0
    for col in UniqueParentColumns:
        output_dict[col.strip()].append({})

    for value in values:
        column = columns[i]
        splitValues = column.split(".")
        if len(splitValues) == 2:
            output_dict[splitValues[0].strip()][row][splitValues[1].strip()] = value.strip()
        else:
            output_dict[splitValues[0].strip()][row] = value.strip()
        i += 1
    row += 1

with open(output_file_path, 'wb') as op:
    json.dump(output_dict, op,indent=4)

inputFile.close()

print('output file written at:%s' % output_file_path)
