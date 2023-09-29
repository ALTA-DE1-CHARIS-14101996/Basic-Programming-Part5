#Fungsi Prima dengan Tc = O(sqrt(n)) dan Sc = O(1)
def prime_number(number):
    if number < 2:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
