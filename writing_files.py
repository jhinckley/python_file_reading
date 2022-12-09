# with open('myfile.txt', 'a') as f:
#     f.write('\nJust a line\n')
#     f.write('Just a second line\n')
    
with open('configuration.txt', 'r+') as f:
    f.write('Line added with r+\n')