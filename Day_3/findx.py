def start():
    while True:
        try:
            x = abs(float(input("Please enter a number: ")))
            
            break
        except ValueError:
            print("Oops! Not valid number.Try again...")

    print("******************RESULT******************")
    print (x)
    start()
start()