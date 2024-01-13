import re

def make_dict_with_odd_length_words(input_string):
    split_word_list = input_string.split(" ")
    cleaned_list = []
    for word in split_word_list:
        clean_word = re.sub("[.!?]", "", word)
        cleaned_list.append(clean_word)
    temp_dict = {}
    for word in cleaned_list:
        if len(word) in temp_dict: 
            temp_dict[len(word)] = temp_dict[len(word)] + [word]
        else:
            temp_dict[len(word)]=[word]
    final_dict = {}
    for word_length in temp_dict:
        for word in temp_dict[word_length]:
            if len(word) % 2 == 1:
                final_dict[word_length] = temp_dict[word_length]
        else:
            continue
    return final_dict




# Tests
assert(make_dict_with_odd_length_words("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(make_dict_with_odd_length_words("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
assert(make_dict_with_odd_length_words("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})
