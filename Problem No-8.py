# Write a python script to print squares of first N natural numbers.
n=int(input("Enter the value of N to print squares of first N natural numbers : "))
print([e**2 for e in range(1,n+1,1)])
