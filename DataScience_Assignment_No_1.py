# Course - Data Science
# Assignment No 1

a=10
b=20

#print(a*b)
print(a*b)     # Output = 200

#print(a/b)
print(a/b)      # Output = .5

#print(a%b)
print(a%b)       # Output = 10

#print((a*b)+(a/b)) ##BODMAS
print((a*b)+(a/b))     # Output = 200.5




# Write a program which accept principle, rate and time from user and print the simple interest. The formula to calculate simple interest is:: simple interest = principle x rate x time / 100 Solution.

principle = int(input("Enter The Principle : "))
rate = int(input("Enter The Rate : "))
time = int(input("Enter The Time : "))

simple_interest = (principle * rate * time) / 100 
print("The Simple Interest is : ",simple_interest)



