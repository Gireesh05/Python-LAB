
transaction_id = input("Enter the transaction ID: ")
if transaction_id == transaction_id[::-1]:
    print("The transaction ID is a palindrome.")
else:
    print("The transaction ID is not a palindrome.")
digit_freq = {}
for digit in transaction_id:
    if digit.isdigit():
        digit_freq[digit] = digit_freq.get(digit, 0) + 1
print("Digit frequencies:")
for digit, count in sorted(digit_freq.items()):
    print(f"Digit {digit}: {count} time(s)")

