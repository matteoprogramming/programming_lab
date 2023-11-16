# Programming-lab exercises of Wednesday 15 November 2023
# -------------------------------------------------------


# Write the following function that could be used as a sorting key:

# --------------
# KEY FUNCTION 1
# --------------

# To order a list of strings ignoring the case, then in lexicographical order:
# ['bar', 'cat', 'Cat', 'car'] -> ['bar', 'car', 'Cat', 'cat']

def key_strings_a(x):
  return x.lower(), x



# --------------
# KEY FUNCTION 2
# --------------

# To order a list of tuples of three integer positive elements considering
# the second element, then the first and finally the third
# [(1,5,6), (3,4,9), (1,1,1)] -> [(1,1,1), (3,4,9), (1,5,6)]

def key_tuples(x):
    return x[1], x[0], x[2]



# --------------
# KEY FUNCTION 3
# --------------

# To order a list of strings considering the number of characters in increasing order,
# then the ending letter, then the lexicographical order:
# ['snake', 'caterpillar', 'rat', 'bat', 'dog'] -> ['dog', 'bat', 'rat', 'snake', 'caterpillar']

def key_strings_b(x):
    return len(x), x[-1], x



# --------------
# KEY FUNCTION 4
# --------------

#To order a list of strings considering the number of vowels in decreasing order,
# then the whole length in increasing order, then the reverse alphabetical order.
# example:
#['pear', 'peach', 'apple', 'banana', 'avocado'] ->['avocado', 'banana', 'pear', 'peach', 'apple']

def count_vowels(word):
  n = 0
  for c in word:
    if c in "aeiouAEIOU":
      n+=1
  return n

def key_vowels(x):
  return count_vowels(x), -len(x), x  #and we will use the reverse=True



# --------------
# KEY FUNCTION 5
# --------------

# To order a list of positive integers so that the odd numbers appear before the even numbers
# and the odd numbers are in increasing order, while the even numbers are in
# decreasing order.
# [1,5,2,6,7,4,5,3,8] -> [1,3,5,5,7,8,6,4,2]

def key_numbers(x):
  return -(x%2), ((x%2))*(x), ((x%2)-1)*(x)



###################################################################################################


if __name__ == "__main__":
   print(['bar', 'cat', 'Cat', 'car'], "--->" , sorted(['bar', 'cat', 'Cat', 'car'], key=key_strings_a))
   print([(1,5,6), (3,4,9), (1,1,1)], "--->", sorted([(1,5,6), (3,4,9), (1,1,1)], key=key_tuples))
   print(['snake', 'caterpillar', 'rat', 'bat', 'dog'], "--->", sorted(['snake', 'caterpillar', 'rat', 'bat', 'dog'], key=key_strings_b))
   print(['pear', 'peach', 'apple', 'banana', 'avocado'], "--->", sorted(['pear', 'peach', 'apple', 'banana', 'avocado'], key=key_vowels, reverse=True))
   print([1,5,2,6,7,4,5,3,8], "--->", sorted([1,5,2,6,7,4,5,3,8], key=key_numbers))

