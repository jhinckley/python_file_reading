with open('ip.txt', 'r') as file:
    my_list = [line.rstrip() for line in file]
    print(my_list)
