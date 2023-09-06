book = open('BookOfJohnText.txt','r')
contents = book.read()
words = contents.split()


required_words = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']


word_counts = {}


for word in words:
   if word in required_words:
       word_counts[word] = word_counts.get(word,0) + 1


print('Father: ' + str(word_counts['Father']))
print('God: ' + str(word_counts['God']))
print('Christ: ' + str(word_counts['Christ']))
print('Spirit: ' + str(word_counts['Spirit']))
print('life: ' + str(word_counts['life']))
print('man: ' + str(word_counts['man']))


book.close()
