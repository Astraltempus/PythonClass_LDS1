def start():
    num = int(input("Input a number: "))

    if num > 1:

        # start from 2 to number / 2
        for i in range(2, int(num/2)+1): # +1 because it gets the number before the last number.
            
            if (num % i) == 0: # If num is divisible by 2, it is not prime
                print(num, "is not a prime number")
                start()
                break
        else: # Sucess
            print(num, "is a prime number")
            start()
    
    else:
        print(num, "is not a prime number") # less than 1
        start()
start()