#Python Programming Language

#If and else statement

x= str(input("Enter a number: "))

y= str(input("Enter another number: "))

if x > y:
    print(x + " is greater than " + y)
elif y > x:
    print(y + " is greater than " + x)
else:
    print(x + " is equal to " + y)



#This technique is known as Ternary Operators, or Conditional Expressions.
a = 2
b = 330
print("A") if a > b else print("B")


c = 330
d = 330
print("C") if c > d else print("=") if c == d else print("D")




    
