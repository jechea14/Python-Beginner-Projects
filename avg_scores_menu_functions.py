# Objective: 
# Create a menu for the user to choose to enter their name, enter their exam scores,
# display average exam score, display summary of scores with average score and
# letter grade, or quit. The chosen choice will do their functionality using
# functions and will return to the menu. 
# 
# Error check to see if the user has not entered their scores when they choose
# to display their average score or summary and their name when they choose to
# display the summary

name_entered = False
scores_entered = False

loop = True
while loop:
    print("1. Enter your name.")
    print("2. Enter exam scores.")
    print("3. Display average exam scores.")
    print("4. Display summary.")
    print("5. Quit.")
    
    choice = input("\nPlease enter choice: ")
    
    if choice == "1": # Enter user name
        name = input(f"\nWhat is your first name? ")
        name_entered = True
        
    elif choice == "2": # Enter exam scores
        scores = []
        max_exam_score = 100
    
        for i in range(3):
            score = int(input(f"Please enter the score of exam #{i+1}: "))
            if score > max_exam_score:
                print("\nError: Your score is greater than 100. Please try again.\n")
                break
            else:
                scores.append(score)
        scores_entered = True
                
    elif choice == "3": # Display average exam scores
        if scores_entered == True:
            print(f"\nAverage exam score: {getAvg(scores)}.\n")
        elif scores_entered == False:
            print("\nError: Please use the menu to enter your scores.\n")
            
    elif choice == "4": # Display summary
        if name_entered == True and scores_entered == True:                
            print(f"\nHi {name}, based on your exam scores of {scores[0]}, {scores[1]}, and {scores[2]}, your average is {getAvg(scores)} with a grade letter of a {getGradeLetter(avg_score)}.\n")
        else:
            print("\nError: Please use the menu to enter your name and scores.\n")
        
    elif choice == "5": # Quit
        print("\nQuitting program.")
        exit()
        
    else: # Invalid input
        print("\nInvalid input. Please try again.\n")
        
def getAvg(scores):
    return sum(scores) / 3

def getGradeLetter(average_score):
    if average_score >= 90:
        grade_letter = 'A'
    elif average_score >= 80:
        grade_letter = 'B'
    elif average_score >= 70:
        grade_letter = 'C'
    elif average_score >= 60:
        grade_letter = 'D'
    else:
        grade_letter = 'F'
    