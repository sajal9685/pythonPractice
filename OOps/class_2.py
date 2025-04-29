class calculator():
    def __init__(self,n):
        self.n=n      
    def square(self):
       print(self.n**2)
    def cube (self):
        print (self.n**3)
    def sqRoot(self):
        print( self.n*0.5)    
        
    
num=calculator(4)
num.square()
num.cube()
num.sqRoot()
    