import random
import time


def get_expression(end_digits):
        operators = ["+" , "*" , "-" , "/"]
        number1 = random.randint(1,(end_digits))
        number2 = random.randint(1,(end_digits))
        operator = random.choice(operators)
        expression = f"{number1} {operator} {number2}"

        return expression

def problem_generator(no_of_problems , total_digits):
    starttime = time.time()
    score = 0
    for i in range(no_of_problems):
        expression = get_expression(total_digits)
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
    endtime = time.time()
    totaltime = endtime - starttime

    return totaltime ,score 

def main():
    total_questions = int(input("Enter the total number of questions you want to solve : "))
    total_digits = int(input("Enter the maximum number that u want to solve problem till like (10,100,1000): "))
    timespent , score = problem_generator(total_questions,total_digits)

    print(f"\nThe total time that u hv spent was {round(timespent )} seconds")
    print(f"Your final score is {score}")



if __name__ == "__main__":
    main()