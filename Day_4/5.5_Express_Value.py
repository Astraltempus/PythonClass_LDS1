
num = int(input(" Please Enter the Maximum Value : "))

atotal = 0

# A Using For loop
for number in range(1, num):
    if(number % 2 != 0): # if number isn't divisible by 2 then
        atotal = atotal + number # add that number in the list

print("A = {0}".format(atotal)) 

# A Using While loop
atotal = 0
number = 1

while number <= num:
    if(number % 2 != 0):
        atotal = atotal + number
    number = number + 1

print("A while method = {0}".format(atotal))

btotal = 0

# B Using For loop
for number in range(2, num):
    if(number % 2 == 0): # if number is divisible by 2 then
        btotal = btotal + number # add that number in the list

print("B = {0}".format(btotal)) 

# B Using While loop

btotal = 0
number = 2

while number <= num - 1:
    if(number % 2 == 0):
        btotal = btotal + number
    number = number + 1

print("B while method = {0}".format(btotal))

# C using for loop

ctotal = 1
for number in range(1, num + 1):
    ctotal = number * ctotal
print("C = {0}".format(ctotal))

# C using while loop

ctotal = 1
number = 1
while number < num +1:
    ctotal = ctotal * number
    number += 1
print("C while method = {0}".format(ctotal))

# D using for loop

dtotal = 1
for number in range(1,num +1):
    if number % 3 == 0:
        dtotal = number * dtotal
print("D = {0}".format(dtotal))

# D using while loop
dtotal = 1
number = 1

while number < num +1:
    if number % 3 == 0:
        dtotal = number * dtotal
        
    number += 1
print("D while method = {0}".format(dtotal))

