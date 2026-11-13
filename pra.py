try:
    
    a = int(input("Enter the val : "))
    b = int(input('Enter the val : '))
    
    result = a / b
    
    print("Division is : ", result)
    
except ZeroDivisionError:
    print("Can not divided by the zero")
    
except ValueError:
    print("Please enter the valid number")
   
finally:
    print("Program excetued completly")            