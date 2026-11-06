class A:
    def show(self):
        print("This is class A")
    
class B(A):
    def display(self):
        print("This is class B")   
    
class C(A):
    def print_data(self):
        print("This is the class C")
       
class D(B,C):
    def result(self):
        print("This is class D")        
     
obj = D()
obj.show()
obj.display()
obj.print_data()
obj.result()         
                 