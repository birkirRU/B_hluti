
# Birkir Snær Axelsson

skra = open("lorem.txt", "tr")

letter_dict = {}

for line in skra:
    line = line.strip()
    word_list = line.split(" ")

for word in word_list:
    if word[0].lower() not in letter_dict:
        letter_dict[word[0].lower()] = []
    letter_dict[word[0].lower()].append(word)

max_words = 0
letter_max_words = ""
for letter in letter_dict:
    a_words = len(letter_dict[letter])
    print(letter + ":")

    for word in letter_dict[letter]:
        print(f"\t{ word }")

    if a_words > max_words:
        max_words = a_words
        letter_max_words = letter

print(f"\nFlest orðin byrja á stafnum '{letter_max_words}', þau eru {max_words} talsin")
    