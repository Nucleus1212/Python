#Tuple
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#But there is a workaround. You can convert the tuple into a list,
#change the list, and convert the list back into a tuple.

tuple1=("Car", "Bus", "Train")
tuple2=("Mango", "Apple", "Watermelon")
tuple3=tuple1 + tuple2
print(tuple3)

if "Mango" in tuple3:
    print("True")

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

