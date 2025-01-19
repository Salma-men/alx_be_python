# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Retrieve the command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division and display the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

