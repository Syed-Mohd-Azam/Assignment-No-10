# Write a python script to print first N even natural numbers.
n=int(input("Enter the value of N to print first N even natural numbers : "))
print([ e for e in range(2,2*n+1,2)])
