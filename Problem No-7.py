# Write a python script to print first N odd natural numbers.
n=int(input("Enter the value of N to print first N odd natural numbers: "))
print([(2*e-1) for e in range(1,n+1,1)])
