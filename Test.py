num = 4
etotal = 0

for number in range(2, num): # +1 because it gets the number before the last number.
    if (num % number) == 0: # If num is divisible by 2, it is not prime
        print(number, "is not a prime number")
    else: # Sucess
        etotal = number + etotal
print("E = {0}".format(etotal))