# Program to convert binary product code to decimal

# Step 1: Input binary product code
binary_code = input("Enter the binary product code: ")

# Step 2: Validate input
if not all(bit in '01' for bit in binary_code):
    print("Invalid binary number! Please enter only 0s and 1s.")
else:
    # Step 3: Convert binary to decimal
    decimal_value = int(binary_code, 2)

    # Step 4: Display result
    print("The decimal equivalent of the product code is:", decimal_value)
