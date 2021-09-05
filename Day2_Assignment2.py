##Assignment No.2 Python ZERO TO HERO Course

## PROBLEM : Write a program to find the prime no

num = int(input("Enter no to Check Prime or Not Prime : "))
Prime = True
for i in range(2,num):
    if (num%i == 0):
        Prime = False
        break

if Prime:
    print(f"{num} is PRIME")
else:
    print(f"{num} is NOT PRIME")


# We get the output enter num is prime or not


