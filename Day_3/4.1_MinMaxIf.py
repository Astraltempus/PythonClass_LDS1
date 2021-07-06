nums = []

num = int(input('How many numbers: '))

a = 0
for inputs in range(num):
    numbers = int(input('Enter numbers:'))
    if numbers > a:
        a = numbers
    nums.append(numbers)
print("Max is:", max(nums))