nums = []

num = int(input('How many numbers: '))

for inputs in range(num):
    numbers = int(input('Enter numbers:'))
    nums.append(numbers)
print("Max is:", max(nums), "\nMin is :", min(nums))