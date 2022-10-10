# Write a python script to print the first 10 multiples of N in reverse order.
N=int(input("Enter the value of N to print first 10 multiples of N in reverse order: "))
print ([(N*e) for e in range(10,0,-1)])
