sum = 0
n = 10
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first", n, "numbers is: ", sum )
print("##################################################################")
sum2 = 0
n2 = 1
while n2 <= 10:
    sum2 +=n2     
    n2 += 1
print("Total 2nd method:", sum2)

num = int(input("Enter a number:"))

print("Multiplication Table of :", num)  
i = 0
while i <= 9:
   i += 1
   print(num,'x',i,'=',num*i)  