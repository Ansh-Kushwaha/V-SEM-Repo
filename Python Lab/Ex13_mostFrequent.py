# Opening the file
file = open("text.txt", "r")
most_freq_word = ""
freq = 0

# List of words
words = []

for line in file:
    # splitting the line into words, and replacing punctuations and spaces
    line_words = line.lower().replace(',', '').replace('.', '').split(" ")
    for word in line_words:
        words.append(word)

for i in range(len(words)):
    count = 1
    for j in range(i + 1, len(words)):
        if words[i] == words[j]:
            count += 1

    if count > freq:
        freq = count
        most_freq_word = words[i]

print("Most frequent word int the file", file.name, ":", most_freq_word, ",frequency:", freq)