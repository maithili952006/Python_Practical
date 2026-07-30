marital = input("Enter the marital status : ")

if marital == "yes":
    print("Driver is insured")
else:
    
    gender = input("Enther the gender : ")
    age = int(input("Enter the age : "))
    
    if gender == "male" and age > 30:
        print("Driver is insured")
    elif gender == "female" and age > 25:
        print("Driver is insured")
    else:
        print("Driver is not insured")            