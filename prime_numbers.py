def is_prime (n):
    if n<= 1:
        return False
    for item in range (2, int(n**0.5)+1):
        if n % item == 0:
            return False
    return True

# print (is_prime(4))

def genarate_prime (limit):
    primes = []
    for num in range (2,limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
print(genarate_prime(20))


    