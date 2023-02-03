class Shape:
  def __init__(self,colour):
    	self._colour = colour


class Circle(Shape):
    def __init__(self,colour,radius):
        super().__init__(colour)
        self._radius = radius

my_circle = Circle("black",4.5)

my_circle.pretty_print()