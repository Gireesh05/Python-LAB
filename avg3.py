trial1 = float(input("Enter performance for Trial 1: "))

trial2 = float(input("Enter performance for Trial 2: "))

trial3 = float(input("Enter performance for Trial 3: "))

performances = [trial1, trial2, trial3]

performances.sort(reverse=True)

average = (performances[0] + performances[1]) / 2

print(f"The average of the best two performances is: {average:.2f}")

