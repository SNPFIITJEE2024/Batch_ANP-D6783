correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong = 0
# checking the score if it is correct or wrong
print("Incorrectly answered question numbers:")

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong += 1
        print(i + 1)

print("Correct Answers =", score)
print("Wrong Answers =", wrong)

# percentage calculation

percentage = (score / len(correct)) * 100
print("Percentage =", percentage, "%")

if percentage >= 60:
    print("Pass")
else:
    print("Fail")