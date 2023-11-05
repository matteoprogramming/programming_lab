'''
Write a function that gets two {key:set} dictionaries
and returns a new dictionary in which only the keys in both input dictionaries are present,
and the values are the union of the two input sets associated with the same key.
'''
def same_keys(dict1, dict2):
    return set(dict1.keys()).intersection(dict2.keys())

def join_dict(dict1, dict2):
    union_dict = dict()
    for key in same_keys(dict1, dict2):
        union_dict[key] = dict1[key].union(dict2[key])
    return union_dict

if __name__ == "__main__":
    dict1 = {1:{1,2,3}, 4:{"2543",23,12,22,2}, "home":{"ciccio", True, False}}
    dict2 = {1:{1,2,"3", True}, 4:{False,22,2}, "j":{"wine", True, False}}
    print(join_dict(dict1, dict2))