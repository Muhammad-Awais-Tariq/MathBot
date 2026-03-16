import random
import time

score = 0
for i in range(10):
    operators = ["+" , "*" , "-" , "/"]
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    operator = random.choice(operators)
    expression = f"{number1} {operator} {number2}"
    answer = round(float(eval(expression)))
    counter = 0
    while True:
        user_answer = float(input(f"{expression} = "))
        counter +=1
        if user_answer == answer:
            score +=1
            break
        print("Wrong answer!")
        if counter == 3:
            print(f"The correct answer was {answer}")
            score -=1
            break  

print(f"Your final score is {score}") 