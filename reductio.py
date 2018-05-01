text_file = open("alice.txt", "r")
full_text = text_file.read()
text_file.close()

full_text = full_text.split()

def wordFrequency(target):
    return len([word for word in full_text if word.lower() == target.lower()])

print "frequency of 'Alice': " + str(wordFrequency("alice"))

def groupFrequency(target_words):
    frequencies = [wordFrequency(word) for word in target_words]
    return reduce((lambda a,b : a + b), frequencies)

print "frequency of 'Alice', 'Rabbit', and 'Cheshire': " + str(groupFrequency(["Alice", "Rabbit", "Cheshire"]))

def mostFrequent(target_words):
    frequencies = [[word, wordFrequency(word)] for word in target_words]
    print frequencies
    return reduce((lambda a, b : a if a[1] > b[1] else b), frequencies)

print "most frequent word in ['Alice', 'Rabbit', 'Cheshire']: " + str(mostFrequent(["Alice", "Rabbit", "Cheshire"]))
