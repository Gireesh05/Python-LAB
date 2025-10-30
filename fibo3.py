# Program to generate Fibonacci sequence for garden layout

# Step 1: Input number of terms
N = int(input("Enter the number of garden sections (N > 0): "))

# Step 2: Validate input
if N <= 0:
    print("Please enter a number greater than 0.")
else:
    # Step 3: Initialize first two Fibonacci numbers
    a, b = 0, 1
    print("Fibonacci Garden Layout:")

    # Step 4: Generate Fibonacci sequence
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
