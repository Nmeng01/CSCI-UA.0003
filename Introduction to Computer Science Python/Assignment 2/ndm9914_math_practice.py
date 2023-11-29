"""
This script allows the user to practice speed addition. The user can set the boundaries depending on how advanced
they want the addition to be.

Submitted by Nicholas Meng, NetID ndm9914
First, the user is asked how many questions they want to answer.
Next, the user is asked what maximum number can be used in the module.
Then, the user presses Enter to begin the test, and answers each question. The script records how long the test took and
how many the user got correct. The user can exit the test at anytime by pressing Enter without inputting an answer.
After the test ends, the user receives a summary of their results.

"""

import random
import time

while True:
    max_questions = input(f"{'How many questions would you like in this practice session? '}")
    if not max_questions:
        continue
    else:
        max_questions = int(max_questions)
        if max_questions > 0:
            break
        print(f"{'Please enter a positive number.'}")
while True:
    max_number = input(f"{'What is the maximum number to be used in the questions? '}")
    if not max_number:
        continue
    else:
        max_number = int(max_number)
        if max_number > 0:
            break
        print(f"{'Please enter a positive number.'}")
tern1 = "question" if max_questions == 1 else "questions"
print(f"Preparing {max_questions} {tern1} with numbers between 0 and {max_number}.")
start = input(f"{'Press Enter when ready to start; any other answer put before pressing Enter exits. '}")
if not start:
    question_count = 0
    correct = 0
    incorrect = 0
    start_time = time.time()
    while question_count < max_questions:
        int1 = random.randint(0, max_number)
        int2 = random.randint(0, max_number)
        answer = input(f"Q{question_count + 1}) What is {int1} + {int2}? ")
        if answer == '':
            end_time = time.time()
            break
        elif int(answer) == int1 + int2:
            correct += 1
        else:
            incorrect += 1
        question_count += 1
    end_time = time.time()
    if question_count + 1 == 1:
        print(f"{'No practice was run.'}")
    else:
        tern2 = "question" if max_questions == 1 else "questions"
        tern3 = "was" if correct == 1 else "were"
        tern4 = "was" if incorrect == 1 else "were"
        print(f"From {question_count} {tern2}, {correct} {tern3} correct and {incorrect} {tern4} incorrect.")
        final_score = correct/question_count
        total_time = end_time - start_time
        average_time = total_time/question_count
        tern5 = "Well done!" if final_score > 0.8 and average_time < 5 else "Try again!"
        print(f"You practiced for {total_time:.2f} seconds: {average_time:.3f} seconds per question. {tern5}")
    print(f"{'Bye!'}")
else:
    print(f"{'Exit'}")






