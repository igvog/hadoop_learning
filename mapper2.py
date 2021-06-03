import sys

for line in sys.stdin:
    word, doc, frequency = line.strip().split('\t')
    print(word, "\t", doc, ";", frequency, ";", "1",sep="")