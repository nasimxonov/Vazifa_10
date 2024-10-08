class Shape:


    def draw(self):

        raise NotImplementedError("draw method must be implemented by subclasses")

class Line(Shape):


    def draw(self):

        for _ in range(24):
            print('*', end='')
        print()

class Triangle(Shape):


    def draw(self):

        a = 4
        for i in range(a):
            if i == a - 1:
                print('*' * (2 * a - 1))  
            else:
                print(' ' * (a - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))

class Rectangle(Shape):


    def draw(self):

        width = 7
        height = 4

        for i in range(height):
            if i == 0 or i == height - 1:
                print('*' * width)  
            else:
                print('*' + ' ' * (width - 2) + '*') 

class NullShape(Shape):

    def draw(self):

        print("Bo'sh shakl")

def shape_factory(shape_type):

    if shape_type.lower() == 'line':
        return Line()
    elif shape_type.lower() == 'triangle':
        return Triangle()
    elif shape_type.lower() == 'rectangle':
        return Rectangle()
    else:
        return NullShape()

shape_name = input("Shakl nomini kiriting (Line, Triangle, Rectangle): ")
shape = shape_factory(shape_name)
shape.draw()
#ozgina suniy intelektdan foydalandim