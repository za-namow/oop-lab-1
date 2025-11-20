import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_location(spread=300, vertical=200, similar=False):
    if similar:
        x = random.randint(-spread//4, spread//4)
        y = random.randint(-vertical//4, vertical//4)
    else:
        x = random.randint(-spread, spread)
        y = random.randint(-vertical, vertical)
    return [x, y]

def draw_pattern(pattern, count=20):
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)

    for _ in range(count):
        if pattern == 1:  # all triangles
            num_sides = 3
            loc_similar = False
        elif pattern == 2:  # all rectangles
            num_sides = 4
            loc_similar = False
        elif pattern == 3:  # all pentagons
            num_sides = 5
            loc_similar = False
        elif pattern == 4:  # triangles, rectangles, pentagons random
            num_sides = random.randint(3,5)
            loc_similar = False
        elif pattern in [5,6,7]:  # many polygons in similar spots
            if pattern == 5:
                num_sides = 3
            elif pattern == 6:
                num_sides = 4
            else:
                num_sides = 5
            loc_similar = True
        elif pattern in [8,9]:  # mix in similar spots
            num_sides = random.randint(3,5)
            loc_similar = True
        else:
            print("Invalid pattern. Choose 1-9.")
            return

        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = random_location(similar=loc_similar)
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

    turtle.update()
    turtle.done()

# Ask user for pattern
pattern = int(input("Select pattern (1-9): "))
draw_pattern(pattern)