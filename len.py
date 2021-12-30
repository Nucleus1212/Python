#Hello world!
#This is Python
#We are creating a list and counting the numbers of item on the list
#copy and input command

mylist=["Birthday", "September", "Thursday", "Cake"]
print(mylist)

x=len(mylist)
print("There are " + str(x) + " items now")

mylist.insert(1,"Holiday")
y=len(mylist)
print(mylist)
print("There are " +str(y)+ " items after insert")

k=input("Enter days name: ")
if k in "Thursday":
   print("It is true")
else:
    print("It is not true")


herlist=["Apple", "Banana", "Papaya"]
hislist=herlist.copy()
print(hislist)
