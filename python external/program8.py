#mehtos overloading
class Addition:
    
    def add(self,a,b=0,c=0):
        print("Addition : ", a+b+c)
        
obj = Addition()        

obj.add(10,20)
obj.add(12,22,11)
obj.add(90,43,22)