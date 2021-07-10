
num = int(input(" Please Enter the Maximum Value : "))

atotal = 0

# A Using For loop
print("A =", end=" ")
for number in range(1, num):
    if(number % 2 != 0): # if number isn't divisible by 2 then
        atotal = atotal + number # add that number in the list
        print(number, end= " + ")
print(" = {0}".format(atotal)) 

# A Using While loop
#atotal = 0
#number = 1

#while number <= num:
#    if(number % 2 != 0):
#        atotal = atotal + number
#    number = number + 1

#print("A while method = {0}".format(atotal))

btotal = 0

# B Using For loop
print("B =", end=" ")
for number in range(2, num):
    if(number % 2 == 0): # if number is divisible by 2 then
        print(number, end= " + ")
        btotal = btotal + number # add that number in the list

print(" = {0}".format(btotal)) 

# B Using While loop

#btotal = 0
#number = 2

#while number <= num - 1:
#    if(number % 2 == 0):
#        btotal = btotal + number
#    number = number + 1

#print("B while method = {0}".format(btotal))

# C using for loop

ctotal = 1
print("C =", end=" ")
for number in range(1, num + 1):
    ctotal = number * ctotal
    print(number, end= " + ")
print(" = {0}".format(ctotal))

# C using while loop

# ctotal = 1
# number = 1
# while number < num +1:
#     ctotal = ctotal * number
#     number += 1
# print("C while method = {0}".format(ctotal))

# D using for loop

dtotal = 1
print("D =", end=" ")
for number in range(1,num +1):
    if number % 3 == 0:
        print(number, end= " + ")
        dtotal = number * dtotal
print(" = {0}".format(dtotal))

# D using while loop
# dtotal = 1
# number = 1

# while number < num +1:
#     if number % 3 == 0:
#         dtotal = number * dtotal
        
#     number += 1
# print("D while method = {0}".format(dtotal))

# E using for loop


etotal = 0

print("E =", end=" ")
for number in range(1, num+1):             
    tam = 0
    for j in range(1, number+1):         # Kiểm tra i có phải số nguyên tố
        so_du = number % j
        if so_du == 0:
            tam += 1
    else:
        if tam == 2:                # Nếu là số nguyên tố bắt đầu tính E
            etotal += number
            print(number, end=" + ")
else:
    print("=", etotal)
    
