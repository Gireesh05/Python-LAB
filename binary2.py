# Program to convert octal readings to hexadecimal

# Step 1: Input octal reading
octal_value = input("Enter the octal reading: ")

# Step 2: Validate input (only digits 0-7)
if not all(ch in '01234567' for ch in octal_value):
    print("Invalid octal number! Please enter digits 0–7 only.")
else:
    # Step 3: Convert octal to decimal
    decimal_value = int(octal_value, 8)
    
    # Step 4: Convert decimal to hexadecimal
    hexadecimal_value = hex(decimal_value)[2:].upper()
    
    # Step 5: Display the result
    print("Hexadecimal equivalent:", hexadecimal_value)
