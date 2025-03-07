# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

num = 0

while num <= 100:
        if num % 10 != 0:
                print(num)
        num+=1