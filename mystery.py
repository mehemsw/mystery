import re

def clean_words_list(str):
    words_list = str.split(" ")
    clean_words = []
    for x in words_list:
        word = re.sub("[.!?]", "", x)
        clean_words.append(word)
    return clean_words

def group_words_length(clean_words):
    word_lengths = {}
    for word in clean_words:
        if len(word) in word_lengths: 
            word_lengths[len(word)] = word_lengths[len(word)] + [word]
        else:
            word_lengths[len(word)] = [word]
    return word_lengths

def odd_length_words(word_lengths):
    odd_words_dict = {}
    for clean_words in word_lengths:
        for x in word_lengths[clean_words]:
            if len(x) % 2 == 1:
                word_lengths[clean_words] = word_lengths[clean_words]
        else:
            continue
    return odd_words_dict




# Tests
# assert(clean_words_list("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
# assert(clean_words_list("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
# print(clean_words_list("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})

print(clean_words_list("This is a sentence. And yet another one!"))
print(group_words_length(clean_words_list("This is a sentence. And yet another one!")))
print(odd_length_words(group_words_length(clean_words_list("This is a sentence. And yet another one!"))))