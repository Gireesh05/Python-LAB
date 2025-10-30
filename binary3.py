# Program to convert a binary access key to decimal and verify its validity

# Step 1: Input binary key
binary_key = input("Enter the binary access key: ")

# Step 2: Validate that input has only 0s and 1s
if not all(bit in '01' for bit in binary_key):
    print("Invalid access key! Please enter only binary digits (0 or 1).")

else:
    # Step 3: Convert binary to decimal
    decimal_key = int(binary_key, 2)

    # Step 4: Display the decimal equivalent
    print("Decimal equivalent of access key:", decimal_key)

    # Step 5: Verify validity
    if decimal_key > 100:
        print("Access Granted ")
    else:
        print("Access Denied ")
