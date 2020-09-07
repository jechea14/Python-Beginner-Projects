# Objective: User inputs their first name and three of their exam scores. The
# program calculates the average of the scores and prints out a summary of the user's scores, the average exam score, and the grade letter of the average score.

name = input(f"What is your first name? ")

scores = []
max_exam_score = 100
    
for i in range(3):
    score = int(input(f"Please enter the score of exam #{i+1}: "))
    if score > max_exam_score:
        print("Your score is greater than 100. Please try again.")
        exit()
    else:
        scores.append(score)
    
avg_score = sum(scores) / 3

if avg_score >= 90:
    grade_letter = 'A'
elif avg_score >= 80:
    grade_letter = 'B'
elif avg_score >= 70:
    grade_letter = 'C'
elif avg_score >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'
    
print(f"Hi {name}, based on your exam scores of {scores[0]}, {scores[1]}, and {scores[2]}, your average is {avg_score} with a grade letter of a {grade_letter}")