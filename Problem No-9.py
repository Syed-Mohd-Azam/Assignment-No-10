# Write a python script to print cubes of first N natural numbers.
n=int(input("Enter the value of N to print cubes of first N natural numbers : "))
print([e**3 for e in range(1,n+1,1)])
