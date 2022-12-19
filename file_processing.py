with open('devices.txt', 'r') as f:
    devices = f.read().splitlines()
    # print(devices)
    
mylist = []
for item in devices:
    tmp = item.split(':')
    mylist.append(tmp)
    
print(mylist)
    