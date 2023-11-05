'''
Write a function that gets a string of words separated by spaces and constructs a dictionary in which the keys are the lengths of the words,
and the values are sets with the words that have exactly that length in numbers of characters.
'''

def words_in_string(string):
    return sorted(string.strip().split(" "), key=len)

def create_dict_words_by_length(string):
    dict_words_by_length = dict()
    for word in words_in_string(string):
        dict_words_by_length[len(word)] = set()
    for word in words_in_string(string):
        dict_words_by_length[len(word)].add(word)
    return dict_words_by_length

if __name__ == "__main__":
    print(create_dict_words_by_length("at my home I eat very well and I drink lovely wine"))