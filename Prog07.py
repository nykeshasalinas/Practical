# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers. 
sum = 0

for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    sum += number

print("The sum of all numbers is", sum)