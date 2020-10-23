import math

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
        
    def getArea(self):
        return self.width*self.height
        
class Circle:
    def __init__(self,radius):
        self.radius=radius        
        
    def getRadius(self):
        return self.radius    
        
    def getArea(self):
        return math.pi*self.radius