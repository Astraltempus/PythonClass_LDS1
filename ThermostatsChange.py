def start():
    while True:
        try:
            x = float(input("Please enter a number: "))
            
            break
        except ValueError:
            print("Oops! Not valid number.Try again...")
            
    F = 9/5*x+32
    print("******************RESULT******************")
    print(F)
    start()
start()