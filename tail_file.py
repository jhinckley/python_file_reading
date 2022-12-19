# Defintion to open, read and display a numbered
# set of lines from the end of the file
def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-4:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        return my_str


t = tail('test.txt', 3)
print(t)