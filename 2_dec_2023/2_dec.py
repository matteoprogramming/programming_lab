# Programming-lab exercises of Friday 2 December 2023
# ---------------------------------------------------


# RECURSIVE FUNCTIONS

# Write a recursive function that takes as input a list of numbers
# and returns true if it is monotone increasing and false if it is not.

def is_monotone_increasing(l):
    if len(l)<2:
        return True
    elif l[0]<l[1]:
        return is_monotone_increasing(l[1:])
    else:
        return False


# Write a recursive function that takes as input a list of numbers
# and returns true if it is monotone decreasing and false if it is not.


def is_monotone_decreasing(l):
    if len(l)<2:
        return True
    elif l[0]>l[1]:
        return is_monotone_decreasing(l[1:])
    else:
        return False


# Write a recursive function that takes as input a list of numbers
# and returns their sum.

def sum_rec(l):
    if len(l) == 1:
         return l[0]
    else:
        return l[0]+sum_rec(l[1:])
    

# Write a recursive function that takes as input a list of numbers
# and returns their minimum.

def min_rec(l):
    if len(l) == 1:
        return l[0]
    m = min_rec(l[1:])
    if m<l[0]:
        return m
    else:
        return l[0]


# Write a recursive function that takes as input a list of numbers
# and returns their maximum.

def max_rec(l):
    if len(l) == 1:
        return l[0]
    m = max_rec(l[1:])
    if m>l[0]:
        return m
    else:
        return l[0]



if __name__ == "__main__":
    t = [[85, 77, 25, 75, 23, 84, 2955, 758, 6589], [25, 78, 1455, 8999, 45585], [89988, 85, 74, 5, 3, 1]]
    for el in t:
        print(f"is {el} monotone increasing?", is_monotone_increasing(el))
    for el in t:
        print(f"is {el} monotone decreasing?", is_monotone_decreasing(el))
    for el in t:
        print("sum_rec:", sum_rec(el), "\t\texpected:\t", sum(el))
    for el in t:
        print("min_rec:", min_rec(el), "\t\texpeted:\t", min(el))
    for el in t:
        print("max_rec:", max_rec(el), "\t\texpected:\t", max(el))