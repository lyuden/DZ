with open('str.txt', 'w', encoding='utf-8') as myfile:
    myfile.write('mystring')

# write-mode - not deadable
with open('str.txt', 'r', encoding='utf-8') as myfile:
    print(myfile.read())