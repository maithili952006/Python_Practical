try:
    a = 10
    b = 20
    
    res = a / b
    print(res)
    
except ZeroDivisionError:
    print("Not divide br the 0")
    
except ValueError:
    print("Enter the correct value") 
    
finally:
    print('The program is exicuted')    
           