import time
i = int(input("Countdown from: "))

while i > 0:
    print(i)
    i -= 1
    time.sleep(0.1)