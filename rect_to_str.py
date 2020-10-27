class Rectangle:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def rect_to_str(self):
        return f"Rectangle ({self.x:d}, {self.y:d}, {self.width:d}, {self.height:d})"
        
r=Rectangle(5,10,50,100)

print(r.rect_to_str())