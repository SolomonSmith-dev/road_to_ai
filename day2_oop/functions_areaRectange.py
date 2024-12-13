# Function to find area of a rectangle
def calculate_area(length, width):
    return length * width

# Function to calculate the perimeter
def calculate_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3

print(f"Area: {calculate_area(length, width)}")
print(f"Perimeter: {calculate_perimeter(length, width)}")
