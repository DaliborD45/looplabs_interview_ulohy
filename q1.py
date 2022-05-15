def is_prime(number):
    dividers = []
    for i in range(1, number+1):
        if number % i == 0:
            dividers.append(i)
    if len(dividers) == 2 and dividers[0] != dividers[1]:
        return True
    else:
        return False


print(is_prime(1))  # !
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))  # !
print(is_prime(5))
print(is_prime(7))
print(is_prime(11))
print(is_prime(12))  # !
print(is_prime(1321))
print(is_prime(832911))  # !
