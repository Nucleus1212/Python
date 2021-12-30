#For Loops
#Nested Loops



adj=["nice", "big", "smooth"]
noun=["car", "apple", "surface"]

for x in adj:
    for y in noun:
        print(x,y)

fruits=["Apple", "Banana", "Cherry", "Watermelon"]

for x in fruits:
    print(x)
    if x=="Banana":
     break

vegetables=["Potato", "Tomato", "Brinjal"]
for x in vegetables:
    if x=="Potato":
        continue
    print(x)

for y in range(6):
    print(y)

print("This is a statement")


for z in range(2,6):
    print(z)

print("This is statement number 2")

for d in range(6):
    print(d)
else:
    print("Finished")
