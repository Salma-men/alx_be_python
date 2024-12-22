# multiplication_table.py

def generate_multiplication_table():
    try:
        # Prompting user for input
        number = int(input("Enter a number to see its multiplication table: "))

        # Generating multiplication table
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
        