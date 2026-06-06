import random
#RANDOM MODULE->helps generate randon numbers

n=random.randint(1,100)
#generates a random integer from 1 to 100

a=-1 #variable a stores the user's guess
#we choose some value for a to define it so that error "a is not defined" can be removed
#and why only a=-1? a can hold any value except from 1 to 100 because our loop syas a!=n

guesses=1
while(a!=n):
    a=int(input("guess a number: "))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
    guesses+=1

print(f"you have guesses the number {n} correctly in {guesses} attempt!")