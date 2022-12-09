with open('a.txt', 'r') as a:
    a.seek(4)
    print(a.read(5))

print(a.closed)