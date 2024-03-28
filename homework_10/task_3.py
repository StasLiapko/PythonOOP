class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def area(self):
        return self._width * self._height
    
    def __setattr__(self, attr, value):
        if attr in ('width', 'height'):
            raise AttributeError("Modification of width and height is not allowed")
        super().__setattr__(attr, value)
    
    def __getattr__(self, attr):
        if attr in ('width', 'height'):
            raise AttributeError(f"Rectangle object has no attribute '{attr}'")
        else:
            raise AttributeError(f"Rectangle object has no attribute '{attr}'")


rectangle = Rectangle(5, 10)
print(rectangle.width)  
print(rectangle.height) 
print(rectangle.area()) 

try:
    rectangle.width = 8  
except AttributeError as e:
    print(e)  

try:
    print(rectangle.noproperty)  
except AttributeError as e:
    print(e)