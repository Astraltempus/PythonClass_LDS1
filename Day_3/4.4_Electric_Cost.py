def start():
    while True:
        try:
            kwh = int(input("How many kWh? "))
            
            break
        except ValueError:
            print("Oops! Not valid number.Try again...")
            
    a, b, c, d, e, f = 1484, 1533, 1786, 2242, 2503, 2587

    ta = 50 * a
    tb = ta + (50*b)
    tc = tb + (100*c)
    td = tc + (100*d)
    te = td + (100*e)

    if kwh <= 0:
        print("Wrong input")
        
    elif kwh <= 50:
        cost = kwh * a
        print("Total: ", cost)

    elif kwh <= 100:
        cost = ta + ((kwh - 50)*b)
        print("Total: ", cost)

    elif kwh <= 200:
        cost = tb +((kwh-100)*c)
        print("Total: ", cost)

    elif kwh <= 300:
        cost = tc + ((kwh -200)*d)
        print("Total: ", cost)

    elif kwh <= 400:
        cost = td + ((kwh -300)*e)
        print("Total: ", cost)

    elif kwh > 300:
        cost = te + ((kwh -400)*f)
        print("Total: ", cost)
    start()
start()
