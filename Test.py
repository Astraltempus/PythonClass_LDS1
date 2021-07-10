btotal = 0
num = 4
# B Using For loop
print("B =", end=" ")
for number in range(2, num):
    if(number % 2 == 0): # if number is divisible by 2 then
        print(number, end= " + ")
        btotal = btotal + number # add that number in the list

print(" = {0}".format(btotal))