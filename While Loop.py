#Python While Loops

# Remember to increment i, or else the loop will continue forever.

i=1
while i<7:
    print(i)
    i+=1

j=10
while j<20:
    print(j)
    if j==15:
        break
    j+=1


# Note that number 3 is missing in the result
k=0
while k<6:
    k+=1
    if k==3:
        continue
    print(k)

#While Loops

i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
    
