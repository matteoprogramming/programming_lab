'''
Write a function that gets a dictionary of the type {key:integer list} and returns a new dictionary with the same keys and with values the average of the integers in the original dictionary list.
'''

def average(numbers_list):
    return sum(numbers_list)/len(numbers_list)

def create_average_dict(intial_dict):
    average_dict = dict()
    for n in intial_dict:
        average_dict[n] = average(intial_dict[n])
    return average_dict


if __name__ == "__main__":
    print(create_average_dict({3:[3,4,5], 5:[234,123,234], 78:[234,54,3]}))