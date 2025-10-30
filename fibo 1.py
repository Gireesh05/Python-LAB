# Program to display Fibonacci series up to N terms

# Step 1: Input number of terms
N = int(input("Enter the number of terms (N > 0): "))

# Step 2: Check if N is valid
if N <= 0:
    print("Please enter a number greater than 0.")
else:
    # Step 3: Initialize first two terms
    a, b = 0, 1
    print("Fibonacci Series:")

    # Step 4: Loop to generate series
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
