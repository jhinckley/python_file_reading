with open('test.txt', 'r') as f:
    # read the file and split the lines
    content = f.read().splitlines()
    # show output
    # print(content)
    
    # reassemble the text back into string (concatentate)
    my_str = '\n'.join(content)
    print(my_str)
