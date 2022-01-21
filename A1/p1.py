data = open("file.txt","r")
word_frequency = {}
for line in data:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
for key in word_frequency:
    print(key, ":", word_frequency[key])

