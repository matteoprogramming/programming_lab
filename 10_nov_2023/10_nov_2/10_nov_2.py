# Programming-lab exercise n. 2 of Friday 10 November 2023
# --------------------------------------------------------
#
# Define a function words_in_file(input_filename, output_filename, length)
# that takes two strings representing two filenames and an integer as input.
#  The file named input_filename contains strings separated by spaces,
#  tabs, or carriage returns.

#  The function must return the number of strings of the requested length
#  found in the input file.

# The function must create a new text file named output_filename
# containing all the strings of length 'length' present in the file
# input_filename organized by rows.
# The rows are in alphabetical order.
# The words in each row:
# - have the same initial letter, with no distinction between
#   uppercase and lowercase;
# - are separated by a space;
# - are sorted in alphabetical order, with no distinction between
#   uppercase and lowercase. In the case of equal words, they are
#   in lexicographical order (UPPERCASE before lowercase).


# SOLUTION

# This function will be used as a criterion of the sorted() function
# to sort the words first alphabetically and then lexicographically
def mykey(word):
    return word.lower(), word

# Principale function
def words_in_file(input_filename, output_filename="", length=0):

    # First we read the entire input file and extract all the words
    with open(input_filename, "r", encoding="utf-8") as f_in:
        all_words = f_in.read().split()

    # Then select only words as long as length
    words = [word for word in all_words if len(word)==length]

    # Let's create a dictionary like this:
    # key: intial letter regardless of whether it is lowercase or uppercase 
    # --> value: a set with the words that start with that letter
    word_dict = {}
    for word in words:
        i_l = word[0].lower()   #initial letter lowercase
        word_dict.setdefault(i_l, set())
        word_dict[i_l].add(word)

    # To print the words in the output file,
    # we first iterate the initial letters in alphabetical order
    # and then the words corresponding to that letter
    # according to the criterion defined above
    with open(output_filename, "w", encoding="utf-8") as f_out:
        for i_l in sorted(word_dict):
            ord_words = sorted(word_dict[i_l], key=mykey)
            # We print the first n-1 words with a space at the end,
            # The last with a carriage return (default value of print())
            for word in ord_words[:-1]:
                print(word, file = f_out, end=" ")
            print(ord_words[-1], file = f_out)

if __name__ == "__main__":
    files_dict= {
        "test01.txt": ["test01_out.txt", 3],
        "test02.txt": ["test02_out.txt", 8],
        "test03.txt": ["test03_out.txt", 7]
    }
    for input_file, output_info in files_dict.items():
        words_in_file(input_file, output_info[0], output_info[1])
