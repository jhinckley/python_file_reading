f =  open('configuration.txt', 'r')

content = f.read(5)
print(content)

content = f.read(3)
print(content)

print(f.closed)

f.close()

print(f.closed)