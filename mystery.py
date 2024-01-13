import re

def make_cleaned_list(input_string):
    # Split up the input into a clean list of words
    split_word_list = input_string.split(" ")
    cleaned_list = []
    for word in split_word_list:
        clean_word = re.sub("[.!?]", "", word)
        cleaned_list.append(clean_word)
    return cleaned_list

def make_first_dict(input_clean_list)
    # Create a dictionary with key value pairs in format: <word length>: <word>
    first_dict = {}
    for word in input_clean_list:
        if len(word) in first_dict: 
            first_dict[len(word)] = first_dict[len(word)] + [word]
        else:
            first_dict[len(word)]=[word]
    return first_dict

def make_odd_dict(input_dict_of_words)
    # Create a new dictionary which has words of only odd length
    odd_dict = {}
    for word_length in input_dict_of_words:
        for word in input_dict_of_words[word_length]:
            if len(word) % 2 == 1:
                odd_dict[word_length] = input_dict_of_words[word_length]
        else:
            continue
    return odd_dict

def whole_process(input_string)
    


# Tests
assert(make_odd_dict("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(make_odd_dict("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
assert(make_odd_dict("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})
