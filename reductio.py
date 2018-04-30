text_file = open("alice.txt", "r")
full_text = text_file.read()
text_file.close()

full_text = full_text.split()

def wordFrequency(input):
 return len([word for word in full_text if word == ""])


print "frequency of '': " wordFrequency()
