print ("hello")
x=6
print(x)
6
y = x * 7
print(y)


name = input("the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the")
handle = open(name, "r")
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
          counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in list(iterable=counts.items()) :
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


print('4')
type("hello, world")
