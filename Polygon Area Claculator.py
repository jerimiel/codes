class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,new_width):
        self.width=new_width
        print("width is now: ",self.width)

    def set_height(self,new_height):
        self.height=new_height
        print("height is now: ",new_height)

    def get_area(self):
        area=self.width*self.height
        return area

    def get_perimeter(self):
        perimeter=((2*self.width)+(2*self.height))
        return perimeter

    def get_diagonal(self):
        diagonal=((self.width**2)+(self.height**2))**0.5
        return diagonal

    def get_picture(self):
        a=''
        if self.width>60 or self.height>60:
            print("Too big for picture")
        else:
            for i in range(0,round(self.height)-1):
                g="*"*round(self.width)
                a=a+g+'\n'
            g="*"*round(self.width)
            a=a+g
        return a

    def get_amount_inside(self,obj):
        amount=(self.width*self.height)/(obj.width*obj.height)
        return round(amount)

    def __str__(self):
        return "Rectangle(width=%d, height=%d)"%(self.width,self.height)




class Square(Rectangle):

    def __init__(self,side):
        self.side=side
        self.width=side
        self.height=side
        
        

    def set_side(self,new_side):
        self.side=new_side
        self.width=new_side
        self.height=new_side
        print("sides are now: ",self.side)

    def set_width(self,new_width):
        self.width=new_width
        self.height=new_width
        self.side=new_width

    def set_height(self,new_height):
        self.width=new_height
        self.height=new_height
        self.side=new_height

    def __str__(self):
        return "Square(side=%d)"%(self.side)


rect=Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
rect.get_picture()

sq=Square(9)
print(sq.get_area())
sq.set_side(4)
sq.set_width(22)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
   
        






















        
        
