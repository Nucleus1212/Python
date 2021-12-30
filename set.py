# The set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.

# You cannot access items in a set by referring to an index or a key.

# Once a set is created, you cannot change its items, but you can add new items.

#------------------------------------------------------------------------------


thisset={"apple", "banana", "carrot", "bunny"}
print(thisset)

for a in thisset:
    print(a)
    

thatset={"Calculator", "Pen", "Pencil", "Eraser"}
thatset.add("Sharpner")
print(thatset)

x=input("Enter a fruit name: ")
if x in thisset:
    print("True")
else:
    print("False")

herset={"Solid", "Liquid", "Gas"}
herset.update(["Methane", "Ethane", "Propane"])
print(herset)
