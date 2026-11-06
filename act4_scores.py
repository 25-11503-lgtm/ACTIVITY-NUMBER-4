n = int(input("How many students? "))

scores = []

for i in range(n):
    score = float(input("Enter score: "))
    scores.append(score)

total = sum(scores)
average = total / n
highest = max(scores)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
