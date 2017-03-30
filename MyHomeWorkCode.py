# 1st and 2nd
# with open('str.txt', 'w', encoding='utf-8') as myfile:
#     myfile.write('Чето там пишем и че то там выводим')

# write-mode - not deadable
# with open('str.txt', 'r', encoding='utf-8') as myfile:
#     print(myfile.read())

# read as bite
# with open('str.txt', 'rb') as myfile:
#     print(myfile.read())

with open('str.txt', 'w', encoding='latin-1') as myfile:
    myfile.write('more short')

with open('str.txt', 'r', encoding='latin-1') as myfile:
    print(myfile.read())