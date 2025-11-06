
def area_square(sides):
    area = sides * sides 
    print(f"The area of your square is {area}")

def area_rectangle(width, length):
    area = width * length
    print(f"The area of your reactangle is {area}")

def area_triangle(base,height):
    area = 1/2 * base * height
    print(f"The area of your triangle is {area}")

def area_circle(radius):
    radius_to_the_power_of_2 = pow(radius, 2)
    area = 3.14*radius_to_the_power_of_2
    print(f"The area of your circle is {area}")


print("I can calculate the area of a shape for you.")
shape = input("Which shape do you want me to calculate the area of?: \n").lower()
if shape == "square":
    sides = input("Enter measurement of sides: ")
    try:
        sides = float(sides)  
        area_square(sides)    
    except ValueError:
        print("Sorry, please enter a valid number")

elif shape == "triangle":
    base = input("Enter measurement of base: ")
    height = input("Enter measurement of height: ")
    try:
        base = float(base) 
        height = float(height)  
        area_triangle(base, height)
    except ValueError:
        print("Sorry, please enter a valid number")

elif shape == "rectangle":
    width = input("Enter measurement of width: ")
    length = input("Enter measurement of length: ")
    try:
        base = float(width) 
        length = float(length)  
        area_rectangle(length, length)
    except ValueError:
        print("Sorry, please enter a valid number")

elif shape == "circle":
    radius = input("Enter measurement of radius: ")
    try:
        radius = float(radius)  
        area_circle(radius)
    except ValueError:
        print("Sorry, please enter a valid number")
else:
    print("Sorry, invalid shape. The only options are: Square, rectangle, triangle and circle")



