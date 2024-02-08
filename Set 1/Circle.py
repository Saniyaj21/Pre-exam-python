import math

def calculate_circle_properties(radius):
    # Calculate circumference
    circumference = 2 * math.pi * radius
    
    # Calculate area
    area = math.pi * radius**2
    
    return circumference, area


# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))
    
# Calculate circumference and area
circumference, area = calculate_circle_properties(radius)
    
# Display the results
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.2f}")
