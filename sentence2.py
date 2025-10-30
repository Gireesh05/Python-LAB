# Program to count words, numbers, uppercase and lowercase letters in feedback

# Step 1: Input feedback from teacher
feedback = input("Enter the student feedback: ")

# Step 2: Initialize counters
words = len(feedback.split())
numbers = 0
uppercase = 0
lowercase = 0

# Step 3: Loop through each character
for ch in feedback:
    if ch.isdigit():
        numbers += 1
    elif ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

# Step 4: Display results
print("\nFeedback Analysis:")
print("Words:", words)
print("Numbers:", numbers)
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
