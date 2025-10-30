# Program to display Fibonacci-style seating arrangement

# Step 1: Input number of seats
N = int(input("Enter the number of seats (N > 0): "))

# Step 2: Validate input
if N <= 0:
    print("Please enter a number greater than 0.")
else:
    # Step 3: Initialize first two seat counts
    a, b = 0, 1
    print("Fibonacci Seating Arrangement:")

    # Step 4: Generate and display Fibonacci sequence
    for i in range(N):
        print(a, end=" ")
        a, b = b, a + b
