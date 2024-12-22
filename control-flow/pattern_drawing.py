# pattern_drawing.py

def draw_square_pattern():
    try:
        # Prompting user for input
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Using while loop to iterate through rows
        row = 0
        while row < size:
            # Using for loop to print each row
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1
    except ValueError:
        print("Invalid input. Please enter a positive integer.")