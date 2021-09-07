###PYTHON HERO TO ZERO
### ASSIGNMENT NO 4 

# Question : Write a program to implement insertion sort

def insertion_Sort(lis):
    for i in range(1, len(lis)):
        tem = lis[i]
        j = i - 1
        while (j >= 0 and tem < lis[j]):
            lis[j + 1] = lis[j]
            j = j - 1
        lis[j + 1] = tem

lis = input("Enter the list of no. : ").split()
lis = [int(x) for x in lis]
insertion_Sort(lis)
print("Sorted list : ", end=" ")
print(lis)



### Output
'''
input : 12 32 45 85 98 75 105 450 9 73 99
Output : ===> Sorted list :  [9, 12, 32, 45, 73, 75, 85, 98, 99, 105, 450]
'''




