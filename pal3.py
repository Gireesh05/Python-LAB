roll_number = input("Enter the school roll number: ")

if roll_number == roll_number[::-1]:
    print("The roll number is a palindrome.")
else:
    print("The roll number is not a palindrome.")


digit_freq = {}

for char in roll_number:
    if char.isdigit():
        digit_freq[char] = digit_freq.get(char, 0) + 1

print("Digit frequencies:")
for digit, count in sorted(digit_freq.items()):
    print(f"Digit {digit}: {count} time(s)")
