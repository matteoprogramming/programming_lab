'''
Write a function that gets a list of strings and returns a dictionary
with keys to all the characters found in the strings of the list and, as values,
a list of all the strings that contain the character of the key.
The lists in the dictionary are sorted in alphabetical order.
Example: words_with_char(['dog', 'hot', 'dot']) -> {'d':['dog', 'dot'], 'o':['dog', 'dot', 'hot'], 'g':['dog'], 'h':['hot'], 't':['dot', 'hot']} 
'''

def extract_char_set(strings_list):
    return set("".join(strings_list))

def list_strings_with_char(char, strings_list):
    result_list = list()
    for word in strings_list:
        if char in word:
            result_list.append(word)
    return result_list


def words_with_char(strings_list):
    char_words_dict = dict()
    for char in sorted(extract_char_set(strings_list)):
        char_words_dict[char] = sorted(list_strings_with_char(char, strings_list))
    return char_words_dict




if __name__ == "__main__":
    print(words_with_char(['dog', 'hot', 'dot']))