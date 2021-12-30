#A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.


def my_function(fname):
    print(fname + " Shrestha")
    
my_function("Nucleus")

my_function("Asha")

my_function("Saru")



def my_name(lname, cname):
    print(lname + " " + cname)
    
my_name("Cristiano", "Ronaldo")


#Arbitrary Arguments are often shortened to *args in Python documentations.

def my_child(*kids):
    print("My youngest son is " + kids[2])

my_child("Max", "Martin", "Austin")



#If the number of keyword arguments is unknown, add a double ** before the parameter name

def my_unction(**kid):
  print("His last name is " + kid["lname"])

my_unction(fname = "Tobias", lname = "Refsnes")
