# Program to count words, digits, uppercase and lowercase letters in a chat message

# Step 1: Input message from user
message = input("Enter the chat message: ")

# Step 2: Initialize counters
words = len(message.split())
digits = 0
upper = 0
lower = 0

# Step 3: Loop through each character
for ch in message:
    if ch.isdigit():
        digits += 1
    elif ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

# Step 4: Display the results
print("\nChat Log Analysis:")
print("Words:", words)
print("Digits:", digits)
print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
