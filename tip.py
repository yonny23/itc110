#tip.py
#include meal amount tip % and output with result. 

def main():
    amount = input("Amount of bill is, $")
    tipPercent = input("What % are you tipping, %")

    amount = int(amount)
    tipPercent = (float(tipPercent) / 100)

    tip = amount * tipPercent
    total = amount + tip

    print("Your bill amount is", amount + tip)
main()
    
                       
    
    
    
    
