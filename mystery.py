import re

def process_sentence(sentence):
    words_list = sentence.split(" ")
    clean_words = []
    for sentence in words_list:
        word = re.sub("[.!?]", "", sentence)
        clean_words.append(word)
    word = {}
    for stuff in clean_words:
        if len(stuff) in word: 
            word[len(stuff)] = word[len(stuff)] + [stuff]
        else:
            word[len(stuff)]=[stuff]
    words_list = {}
    for clean_words in word:
        for sentence in word[clean_words]:
            if len(sentence) % 2 == 1:
                words_list[clean_words] = word[clean_words]
        else:
            continue
    return words_list




# Tests
assert(process_sentence("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(process_sentence("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
print(process_sentence("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})