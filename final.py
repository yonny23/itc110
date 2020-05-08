class area():
    def __init__(self, sidea, sideb):
        self.sidea=sideb
        self.sideb=sideb
        self.totalarea = 0

    def getSidea(self):
        return self.sidea

    def getSideb(self):
        return self.sideb

    def calculatetotalarea(self):
        result=0
        if self.totalarea !=0:
            sidea= input("enter the area of side a")
            sideb= input("enter the area of side b")
            area=self.sidea * self.sideb
            
            print ("The total area of side a and side b is ", self)

    def __str__(self):
         return self.sidea + "The area of side a is" + self.sideb + "The area of side b is"


                         
                          
    

        
        

      

    
        
        
    
    

    

    

    
        
