# with open('devices.txt', 'r') as f:
#     devices = f.read().splitlines()
#     # print(devices)
    
# mylist = []
# for item in devices:
#     tmp = item.split(':')
#     mylist.append(tmp)
    
# print(mylist)


# csv reader is faster

import csv

with open('devices.txt', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    mylist = []
    for row in reader:
        print(row)
