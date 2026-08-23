def frequency(text):
    words = text.split()
    for word in words:
        print(word, words.count(word))