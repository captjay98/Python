#name = input("the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the")
#handle = open(name, "r")
#counts = dict()

#for line in handle:
#    words = line.split()
 #   for word in words:
 #         counts[word] = counts.get(word,0) + 1


counts = dict()

text = ("the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the")
words = text.split()

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
