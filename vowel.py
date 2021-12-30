
#WAp to count the total number of letters in the string and count the
#number of vowel letters

user=str(input("Enter a word: "))
total=len(user)
print(total)


vowel=0
consonant=0
for i in user:
  if(i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
    vowel=vowel +1
  else:
    consonant=consonant+1
print("The total number of vowel letters in the word is: " + str(vowel))

print("The total number of consonant letters in the word is: " + str(consonant))


    
