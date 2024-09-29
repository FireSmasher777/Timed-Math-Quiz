import random
import time
import threading

def question_generator():
    num1 = random.randint(1,20) # Assigns opperands 
    num2 = random.randint(1,20)
    operators = "+", "-", "/", "*"
    operator = random.choice(operators) # chooses one of 4 operators used in the questions
    x = answers(num1, num2, operator) # call to answers()
    return(f"What is {num1} {operator} {num2} = ") 

def answers(num1, num2, operator):
    global x
    if operator == "+":
        x = num1 + num2
    elif operator == "-":
        x = num1 - num2
        return(x)
    elif operator == "*":
        x = num1 * num2
        return(x)
    elif operator == "/":
        x = num1 / num2
        x = round(x, 1) # rounds the float num to the tenths place
        return(x)
    
# def answers() basically creates the needed answers using the args from the question_generator function

def timer():
    global Q1_time
    Q1_time = 30
    while Q1_time > 0:
        time.sleep(1)
        Q1_time -= 1
        if questions_count == 0:
            return(print(f"{name.capitalize()}, your score was {score}."), exit()) # if user answers all questions
    return(print(f"\nTimes up! {name.capitalize()}, your score was {score}."), exit()) # if timer reaches 0
    
""" def timer() counts down using Q1_time until it reaches the value of 0 which will output the users' score or if the question_count
 varaible reaches zero due to the user answering all generated questions""" 

# main function:

name = str(input("What is your name?: "))
questions = int((random.randint(5, 10))) # amount of questions the user will answer
questions_count = questions
score = 0
three_words = ["Ready.", "Set.", "Go!!!"]

print(f"""{name.capitalize()}, you are going to answer {questions} basic math questions.

NOTE: For division questions, answer with decimals only to the tenths place please.""") # multi-line f-string

time.sleep(1) # waits for 1 seconds

print(f"You have {30} seconds to complete this easy math quiz")



for i in range(3):
    print(three_words[i]) # incrementaly prints out the list 'three_words'
    time.sleep(.5)

timer_thread = threading.Thread(target = timer) # sets up the def function timer() to start along with main algorithm
timer_thread.start() # starts the function timer()

for i in range(0, questions):
    y = question_generator()
    user_choice = input(y)
    
    try:
        user_choice = int(user_choice) # if user outputs an non-float number, it will be an whole number
    except:
        user_choice = float(user_choice) # if the users' output is not a whole number then it is a decimal number (float-num)
   
    if user_choice == x:
        print("CORRECT.")
        score += 1 # scores goes up by 1 due to user getting answer correct
        questions_count -= 1 # this is the number of questions and will go down no matter what due to an answer being implented
    else:
        print("Wrong!")
        questions_count -= 1
        if score != 0:
            score -= 1 

         # if the score is already 0, it will NOT go down, the score will only go down if the user already has points





""" NOTE: if the timer ends, the user can still input an answer BUT the algorithm will output an error,
 due to the exit() function being implented."""







