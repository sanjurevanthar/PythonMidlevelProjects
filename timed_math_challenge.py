import random
import time

OPERATORS = ["+","-","*"]
START_VALUE = 1
END_VALUE = 12
TOTAL_PROBLEMS = 10

#create_problem() -> creates the problem along with answers to compare them with the users

def create_problem():
    left_operand = random.randint(START_VALUE, END_VALUE)
    right_operand = random.randint(START_VALUE, END_VALUE)
    operator_selected = random.choice(OPERATORS)

    expression = str(left_operand) + " " + operator_selected + " " + str(right_operand)
    answer = eval(expression)
    return expression,answer

wrong = 0
input("Press Enter to start")
print("--------------------")
#Calculate time:
START_TIME = time.time()

for i in range(TOTAL_PROBLEMS):
    #we iterate to generate the Total_problems number
    expr,ans = create_problem()
    while True:
        user_guess = input("Problem #"+ str(i+1) + "/" + str(TOTAL_PROBLEMS) + ": " + expr + " = ")
        if user_guess == str(ans):
            break
        wrong +=1

#when we come out of the loop we stop the time
STOP_TIME = time.time()
total_time = round(STOP_TIME - START_TIME, 2) #round off by 2 places

print("--------------------")
print("Nice Work! "+ "You Finished in "+ str(total_time) + " seconds" )