def main():
    milesDriven = float( input("enter the number of miles driven: " ))
    gallonsOfGas = float( input( "enter the gallons of gas used: " ))
    milesPerGallon = milesDriven / gallonsOfGas
    print( "The car's MPG is " + str(milesPerGallon) + " miles/gallon" )
main()
