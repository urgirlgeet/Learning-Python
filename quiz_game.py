# quiz game
# practice the use of 2d collections

questions = ("When was Python language created?",
             "What type of language is Python?",
             "Which is the correct syntax to print 'Hello World'?",
             "What is the correct file extension for Python files?")

options = (("A. 1981", "B. 1927", "C. 1991", "D. 1947"),
           ("A. Object Oriented", "B. Procedure Oriented", "C. None", "D. Both"),
           ("A. echo('Hello World)", "B. p('Hello World)", "C. alert('Hello World)", "D. print('Hello World)"),
           ("A. .py", "B. .p", "C. .th", "D. .pyt"))

answers = ("C", "B", "D", "A")

guesses = []

ques_no = 0
score = 0

for ques in questions:
    print("-------------------------------------------")
    print(ques)
    for opt in options[ques_no]:
        print(opt)
    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_no]:
        print("CORRECT")
        score += 1
    else : 
        print("INCORRECT")
        print(f"Correct answer is option {answers[ques_no]}")
    ques_no += 1

print("-------------------------------------------")
print("                   RESULT                  ")
print("-------------------------------------------")

print(f"Your score is {score}/{len(questions)}") 