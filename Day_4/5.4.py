def start():
    num = int(input("Input a number: "))

    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                start()
                break
        else:
            print(num, "is a prime number")
            start()
    
    else:
        print(num, "is not a prime number") #less than 0
        start()
start()