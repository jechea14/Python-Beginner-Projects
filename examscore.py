# Objective: User inputs a maximum exam score and their own score. The program
# outputs a summary of the score with a letter grade and how many percent points
# the user is away from the next letter grade.

def summary(grade_letter, percentage):
    print(f"You scored a {grade_letter}, and you were {percentage} percent away from the next letter grade.")

def percent(score):
    return 10 - (score % 10)

grade_letter = ''
percentage = 0

max_exam_score = int(input("Please enter the maximum exam score:"))
score = int(input("Please enter your exam score:"))

if score <= max_exam_score:
    if score >= 90:
        grade_letter = 'A'
        print(f"You scored an {grade_letter}.")
    elif score >= 80:
        grade_letter = 'B'
        percentage = percent(score)
        summary(grade_letter, percentage)
    elif score >= 70:
        grade_letter = 'C'
        percentage = percent(score)
        summary(grade_letter, percentage)
    elif score >= 60:
        grade_letter = 'D'
        percentage = percent(score)
        summary(grade_letter, percentage)
    else:
        grade_letter = 'F'
        print(f"You scored an {grade_letter}.")
else:
    print("Score is over the maximum score. Please try again.")