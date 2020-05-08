def main():
    hours = int(input('how many hours did you work? '))
    rate = int(input('what is your hourly rate? '))

    if hours <= 40:
        total = hours * rate
    
    else:
        total = 40 * rate + (hours - 40) * (1.5 * rate)

    print("your earnings are", total)

main()
