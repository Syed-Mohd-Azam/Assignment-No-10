# Write a python script to print first M multiples of N.
N,M=int(input("Enter the value of N :")),int(input("How many multiples of N you want: "))
print( [(N*e) for e in range(1,M+1,1)])
