# look at counted loops

def main():
    sum=0.0
    loops = int(input("How many numbers do you want to enter: "))
    for i in range(loops):
        number = int(input("Enter an integer "))
        sum =sum + number
    average=sum/10.0
    print("the total is:",sum)
    print("the average is:",average)

main()

    
        
