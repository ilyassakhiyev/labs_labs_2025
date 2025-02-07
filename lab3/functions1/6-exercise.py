def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

print(reverse_words("We are ready"))