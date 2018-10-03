def isLeap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        
    
    
    return leap

if __name__ == "__main__":
    year = int(input("Enter a number: "))
    print("You entered: " + str(year))
    leapYear = isLeap(year)
    if leapYear: 
        print( str(year) + " is a leap year")
    else:
        print( str(year) + " is not a leap year")
    
