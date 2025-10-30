pnr = input("Enter the railway PNR number: ")

if pnr == pnr[::-1]:
    print("The PNR number is a palindrome.")
else:
    print("The PNR number is not a palindrome.")

digit_freq = {}

for char in pnr:
    if char.isdigit():
        digit_freq[char] = digit_freq.get(char, 0) + 1

print("Digit frequencies:")
for digit, count in sorted(digit_freq.items()):
    print(f"Digit {digit}: {count} time(s)")
