EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

midterm_exam_grade = float(input("Enter your midterm exam grade (0-100): "))
final_exam_grade = float(input("Enter your final exam grade (0-100): "))
if midterm_exam_grade >= 0 and midterm_exam_grade <= 100:
    if final_exam_grade >= 0 and final_exam_grade <= 100:
        exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT
    else:
        print("Invalid final exam grade. Please enter a value between 0 and 100.")
else:
    print("Invalid midterm exam grade. Please enter a value between 0 and 100.")

assignment_one = float(input("Enter your assignment one grade (0-100): "))
assignment_two = float(input("Enter your assignment two grade (0-100): "))
if assignment_one >= 0 and assignment_one <= 100:
    if assignment_two >= 0 and assignment_two <= 100:
        assignment_grade = (assignment_one + assignment_two) / 2 * ASSIGNMENT_WEIGHT
    else:
        print("Invalid assignment two grade. Please enter a value between 0 and 100.")
else:
    print("Invalid assignment one grade. Please enter a value between 0 and 100.")

quiz_one = float(input("Enter your quiz one grade (0-100): "))
quiz_two = float(input("Enter your quiz two grade (0-100): "))
if quiz_one >= 0 and quiz_one <= 100:
    if quiz_two >= 0 and quiz_two <= 100:
        quiz_grade = (quiz_one + quiz_two) / 2 * QUIZ_WEIGHT
    else:
        print("Invalid quiz two grade. Please enter a value between 0 and 100.")
else:
    print("Invalid quiz one grade. Please enter a value between 0 and 100.")

exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT
final_grade = (exam_grade + assignment_grade + quiz_grade) / 100

print(f"Your final grade is: {final_grade:.2%}")