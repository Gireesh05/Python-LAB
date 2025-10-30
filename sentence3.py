# Program to analyze a newspaper headline

# Step 1: Input headline
headline = input("Enter a newspaper headline: ")

# Step 2: Initialize counters
words = len(headline.split())
uppercase = 0
lowercase = 0
digits = 0
special = 0

# Step 3: Loop through each character
for ch in headline:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1

# Step 4: Display results
print("\nHeadline Statistical Breakdown:")
print("Words:", words)
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special)
