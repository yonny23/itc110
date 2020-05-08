#programming exercise 6.9: create function that returns a grade (based on 5.3)

def main():
    grade = float(input("enter your grade:" ))

    if grade > 90:
            print("A")
            
    elif grade >= 60 and grade < 70:
            print("D")

    elif grade >= 70 and grade < 80:
            print("C")

    elif grade >= 80 and grade < 90:
            print("B")

    else:
        print("F")

main()
    
