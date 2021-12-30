import random
num1=random.randint(1,6)
num2=random.randint(1,6)

print("You rolled a " + str(num1) + " and " + str(num2))
print (" ")

if num1 == 6 and num2 ==6:
    print ("You've got two sixes!")
    print ("You've got another chance!")
elif num1==1 and num2==1:
    print ("You've got another chance")
else:
    print ("Try Again!")
