# Character Counter Program

def count_characters(word):
    count = len(word)
    return count

print("=== Character Counter ===")
word = input("Enter a word: ")
result = count_characters(word)
print(f"The word '{word}' has {result} characters.")
