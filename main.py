with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def num_of_words(txt):
    words = txt.split()
    total_words = 0 
    for i in words:
        total_words += 1 
    return total_words

print("--- Begin report of books/frankenstein.txt ---\n")
print(f"{num_of_words(file_contents)} words found in the document\n")

def charFrequency(txt):
    text = txt.lower()
    charSet = set(text)
    frequency = {}
    for char in charSet:
        frequency[char] = text.count(char)

    return frequency

charDict = charFrequency(file_contents)
charList = list(charDict.items())
sorted_charlist = sorted(charList)


for char in sorted_charlist:
    if char[0].isalpha():
        print(f"The '{char[0]}' character was found {char[1]} times")

print("\n--- End report ---")

    
