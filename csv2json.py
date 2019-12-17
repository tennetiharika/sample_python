

Skip to content
Using Gmail with screen readers

5 of 7,838
(no subject)
Inbox
x

Tenneti Harika
AttachmentsSun, Dec 15, 12:09 PM (2 days ago)
help needed with python Hi Jahnavi Got your contact from Madhu. Attaching the exact i/p and o/p needed. Thanks a lot for your time :)
12

Mail Delivery Subsystem
AttachmentsMon, Dec 16, 1:11 PM (21 hours ago)
Delivery incomplete There was a temporary problem delivering your message to maddy152@gmail.com. Gmail will retry for 46 more hours. You'll be notified if the d

Harsha Tenneti
Attachments
Mon, Dec 16, 10:35 PM (11 hours ago)
to me

Hi,

PFA python file. 

Usage: python sample3.py <Input file name> <output file name>

Example:
python sample3.py sample.csv output1.json

Input: sample.csv
employee.id,employee.first_name,employee.last_name,employee.designation,employee.experience
156861,Harika,Tenneti,TechLead,12Y
673408,kjsvk,hhgjn,jknvkfjllk,15Y
76768,jdnlkfnkn,JKSHLJ,LKDMKKLF,10Y
87989,jfgf,djkfhgj,kjfklk,9Y

Output: outpu1.json
{
  "employee": [
    {
      "experience": "12Y",
      "first_name": "Harika",
      "last_name": "Tenneti",
      "id": "156861",
      "designation": "TechLead"
    },
    {
      "experience": "15Y",
      "first_name": "kjsvk",
      "last_name": "hhgjn",
      "id": "673408",
      "designation": "jknvkfjllk"
    },
    {
      "experience": "10Y",
      "first_name": "jdnlkfnkn",
      "last_name": "JKSHLJ",
      "id": "76768",
      "designation": "LKDMKKLF"
    },
    {
      "experience": "9Y",
      "first_name": "jfgf",
      "last_name": "djkfhgj",
      "id": "87989",
      "designation": "kjfklk"
    }
  ]
}

This also works if you have both schemas in same file like lets say if input have both employee and teacher information like below
employee.id,employee.first_name,employee.last_name,employee.designation,employee.experience,teacher.name
156861,Harika,Tenneti,TechLead,12Y,a
673408,kjsvk,hhgjn,jknvkfjllk,15Y,b
76768,jdnlkfnkn,JKSHLJ,LKDMKKLF,10Y,c
87989,jfgf,djkfhgj,kjfklk,9Y,d

Then output will be
{
  "employee": [
    {
      "experience": "12Y",
      "first_name": "Harika",
      "last_name": "Tenneti",
      "id": "156861",
      "designation": "TechLead"
    },
    {
      "experience": "15Y",
      "first_name": "kjsvk",
      "last_name": "hhgjn",
      "id": "673408",
      "designation": "jknvkfjllk"
    },
    {
      "experience": "10Y",
      "first_name": "jdnlkfnkn",
      "last_name": "JKSHLJ",
      "id": "76768",
      "designation": "LKDMKKLF"
    },
    {
      "experience": "9Y",
      "first_name": "jfgf",
      "last_name": "djkfhgj",
      "id": "87989",
      "designation": "kjfklk"
    }
  ],
  "teacher": [
    {
      "name": "a"
    },
    {
      "name": "b"
    },
    {
      "name": "c"
    },
    {
      "name": "d"
    }
  ]
}

Attachments area
Thanks a lot.Got it, thanks!Thanks a lot for sharing.

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
    json.dump(output_dict, op)

inputFile.close()

print('output file written at:%s' % output_file_path)
sample3.py
Displaying sample3.py.
