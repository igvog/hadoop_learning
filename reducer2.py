import sys
words = {}
main_words = []
for line in sys.stdin:
    word, doc = line.split()
    main_words.append(line)
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1
for key in main_words:
    a, b = key.split()
    c, d, _ = b.split(";")
    print(a + "#" + c + "\t" + d + "\t" +  str(words[a]))