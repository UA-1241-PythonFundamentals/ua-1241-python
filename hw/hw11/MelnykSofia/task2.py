def number_day_week():
    try:
        day=int(input("Enter the number day: "))
        if day>=8 or day<=0:
            raise ValueError ("A week has only 7 days")
        if day == 1:
            print ("Monday")
        if day == 2:
            print ("Tuesday")
        if day == 3:
            print ("Wednesday")
        if day == 4:
            print ("Thursday")
        if day == 5:
            print ("Friday ")
        if day == 6:
            print ("Saturday")
        if day == 7:
            print ("Sunday")
    except ValueError as e:
        print (f"Error {e}. Check the correctness of the entered data.")

number_day_week()
