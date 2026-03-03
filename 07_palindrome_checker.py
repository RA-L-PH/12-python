def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f'"{word}" is a palindrome!')
else:
    print(f'"{word}" is not a palindrome.')
