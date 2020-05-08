#Exercise 7 calculcate student class standing
#This program will show you what is your class standing

def main():

    credits = float(input("How many credits do you have? "))
    
    #Here are the credits basis
    
    if credits >= 7 and credits <16:
        print("You are a Sophomore")

    elif credits >= 16 and credits <26:
       print("You are a Junior")

    elif credits >= 26:
        print("You are a Senior")

    else:
       print("You are a Freshman")
    
main() 

