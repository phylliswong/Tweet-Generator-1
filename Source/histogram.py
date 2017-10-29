import random, sys

with open('/usr/share/dict/words', 'r') as f:
    data = f.read()
    # splits at space
    dataList = data.split()

raw_sentence = "one fish two fish red fish blue fish"
sentence = raw_sentence.split()
list_result = []

def histogram_list(sentence):
# stores each unique word and number of times the word appears
#1 as a list of list
    for i in range(0, len(sentence)-1):
        item = sentence[i]
        occurence = sentence.count(item)
        first_list = [item, occurence]
        # prevent adding duplicated item to the list
        if first_list not in list_result:
            list_result.append(first_list)
    print(list_result)

histogram_list(sentence)
