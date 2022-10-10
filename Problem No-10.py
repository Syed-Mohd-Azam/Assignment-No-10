# Write a python script to display all prime numbers within a range.range start = 15 and end = 45.
for e in range(15,45,1):
    for k in range(2,e,1):
        if e%k==0:
            break
        else:
            continue
    else:
        print(e,end=" ")
