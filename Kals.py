file = input('Enter File: ')
if len(file) < 1:
    file = 'C:\ppy\intro.txt'

handle = open(file)

dic = {}
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1
        print(word, 'new', dic[word])
# print(dic)


largest = -1
theword = None
for key, value in dic.items():
    print(key, value)
    if value > largest:
        largest = value
        theword = key
print('Done', theword, '--', largest)
