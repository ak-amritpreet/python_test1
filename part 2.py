# Defining variables
RED = "red"
YELLOW = "yellow"
BLUE = "blue"

# inputs for color1 and color2
color1 = input("Enter the first primary color: ").lower()
color2 = input("Enter the second primary color: ").lower()

if color1 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color1")

elif color1 == color2:
    print("Error: The two colors you entered are same")

elif color2 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color2")

else:

    if color1 == RED:
        if color2 == BLUE:
            result = "purple"
        else:
            result = "orange"

    elif color1 == BLUE:
        if color2 == RED:
            result = "purple"
        else:
            result = "green"

    else: # color1 == YELLOW
        if color2 == RED:
            result = "orange"
        else:
            result = "green"

    # Print the result
    print(f"The resulting color of mixing {color1} and {color2} is {result}")
