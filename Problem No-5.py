# Write a python script to print first N odd natural numbers in reverse order.
for var in range(int(input("Enter the value of n to print first odd natural numbers in reverse order: "))-1,-1,-1):
    print((2*var+1),end=" ")
print()