import random


s1 = str(input("Enter #1 array: "))
s2 = str(input("Enter #2 array: "))
s3 = str(input("Enter #3 array: "))
index = int(input("Enter a number: "))

choice = random.choice([s1, s2, s3])

print("******************RESULT******************")

print("Length of Array #1: ",len(s1))
print("Length of Array #2: ",len(s2))
print("Length of Array #3: ",len(s3))


last_chars = choice[-index:]
print('S4: ',last_chars)

print("Double of S2:",s2,s2)

