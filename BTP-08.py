def count_words(text):
    words = text.split()
    return len(words)

text = "Hello Panthers!"
word_count = count_words(text)
print("Number of words:", word_count)