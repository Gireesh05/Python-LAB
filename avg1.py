m1=float(input("Enter your marks in Internal test-I:"))

m2=float(input("Enter your marks in Internal test-II:"))

m3=float(input("Enter your marks in Internal test-III:"))

marks=[m1,m2,m3]

marks.sort(reverse=True)

best_two=marks[:2]

avg=sum(best_two)/2

print("The best two test marks:",best_two)

print("Average of best two tests:",avg)

