"""
This script lets the user practice simple addition problems.

Submitted by Nicholas Meng, NetID ndm9914
The user inputs the number of questions they want to answer and the maximum number
they want to see in any of the problems. After inputting these, the practice session
begins and records each question, the user's answer, and the correct answer in a list.
At the end of the practice, the user receives a summary of their score and can choose to
see the list of correct answers before the script ends.
"""


import time
import random
from ndm9914_utilities import ask_user_input
from ndm9914_utilities import to_be
from ndm9914_utilities import plural

summary_list = []
correct_answers = 0
incorrect_answers = 0
answered_questions = 0
print("Answer the questions as presented. Be quick, this practice session is"
      " timed. A blank answer ends the practice.")

# Preparing to ask the number of questions desired.
questions_desired = ask_user_input("How many questions would you like in this practice session? ", min_value=1)
# Preparing to ask the maximum number to be used in the questions.
min_number = 0  # Fixed at this stage
max_number = ask_user_input("What is the maximum number to be used in the question? ", default=100, min_value=1)
print()
# The plural form is handled with a ternary operator.
print(f"Preparing {questions_desired} " + plural("question", questions_desired) +
      f" with numbers between {min_number} and {max_number}.")
prompt = "Press Enter when ready to start; any other answer exits."

continue_prog = not input(prompt)
# These sessions are timed.
start_time = time.time()
# print(f"Start time: {begin_time}")
while continue_prog and answered_questions < questions_desired:
    first_number = random.randint(min_number, max_number)
    second_number = random.randint(min_number, max_number)
    question = (f"Q{answered_questions + 1}) What is {first_number} "
                f"+ {second_number}? ")
    correct_answer = first_number + second_number
    user_string = input(question)
    if not str(user_string):
        break
    # The timer is stopped here unless another question is answered
    end_time = time.time()
    user_answer = int(user_string)
    summary_list.append(f"Q{answered_questions + 1}) What is {first_number} "
                        f"+ {second_number}? You answered {user_string}. The correct answer "
                        f"was {correct_answer}.")
    # Keeping track of the questions/answers
    answered_questions += 1
    if user_answer == correct_answer:
        correct_answers += 1
    else:
        incorrect_answers += 1

if answered_questions:
    delta_time = end_time - start_time
    # For calculations notice that only answered questions count
    average_time = delta_time / answered_questions
    correct_fraction = correct_answers / answered_questions
    # Message chosen using a ternary operator
    message = ("Well done!" if correct_fraction > 0.8 and average_time < 5.0
               else "Try again!")

    print(f"From {answered_questions} " + plural("question", answered_questions) + ", "
          f"{correct_answers} " + to_be(correct_answers, 1) +
          f" correct and {incorrect_answers} " + to_be(incorrect_answers, 1) + " incorrect.")
    print(f"You practiced for {delta_time:.2f} seconds: "
          f"{average_time:.3f} seconds per question. "
          f"{message}")
    list_input = input("Press 'enter' to see a summary of your practice. Any other answer exits. ")
    print()
    if not list_input:
        for item in summary_list:
            print(item)
else:
    print("No practice was run.")

print("Bye!")
