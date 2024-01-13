'''
Write a function that gets a list of integers and returns a dictionary in which the keys are the prime numbers of the lists and the values are the largest multiples of the key in the list.
    Example: [5, 33, 6, 2, 30, 1, 3] -> {5:30, 2:30, 3:33}
'''
def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def find_max_multiples(n, numbers_list):
    multiples_list = list()
    for number in numbers_list:
        if number % n == 0:
            multiples_list.append(number)
    return max(multiples_list)

def create_prime_max_multiple_dict(number_list):
    prime_max_multiple_dict = dict()
    for n in number_list:
        if isPrime(n):
            prime_max_multiple_dict[n] = find_max_multiples(n, number_list)
    return prime_max_multiple_dict

if __name__ == "__main__":
    print(create_prime_max_multiple_dict([5, 33, 6, 2, 30, 1, 3]))
