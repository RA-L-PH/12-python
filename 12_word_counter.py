def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    return len(text)

def count_sentences(text):
    return sum(1 for ch in text if ch in ".!?")

text = input("Enter a sentence or paragraph:\n")

words = count_words(text)
chars = count_chars(text)
sentences = count_sentences(text)

print(f"\nWord count:      {words}")
print(f"Character count: {chars}")
print(f"Sentence count:  {sentences}")
