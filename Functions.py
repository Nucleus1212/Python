#Python Functions

#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.

print("This is a function.")

print("")
def my_function(fname):
    print(fname + " Shrestha")

my_function("Asha")

my_function("Saru")

my_function("Nucleus")


words=["cat", "donkey", "watermelon"]
for w in words:
    print(w, len(w))


for i in range(0,10,3):
    print(i)

mo=["Mary", "had", "a", "little", "lamb"]
for i in range(len(mo)):
    print(i, mo[i])
