print ("This program tells you if a year is a leap year.")
myyear = input("Enter a valid year")

if int(myyear) > 0: #this is the poor input testing
    if (int(myyear) % 4) == 0: #if it is evenly distributed by 4
        if (int(myyear) % 100) == 0: #if it is evenly distributed by 100
            if (int(myyear) % 400) == 0: #if it is evenly distributed by 400
                print("this is a leap year!")
            else:
                print("year is not a leap year")
        else:
            print("year is a leap year!")
    else:
        print ("year is not a leap year")
else:
    print("poor input")
