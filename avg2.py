test1 = float(input("Enter the marks for Test 1: "))

test2 = float(input("Enter the marks for Test 2: "))

test3 = float(input("Enter the marks for Test 3: "))

marks = [test1, test2, test3]

marks.sort(reverse=True)

average = (marks[0] + marks[1]) / 2

print(f"The average of the best two test marks is: {average:.2f}")
