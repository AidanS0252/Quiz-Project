from random import *



score = 0
lives = 3


 #creates linespaces equal to argument
def linespace(lines):
  int(lines)
  for i in range(lines):
    print("")

def randomnum(low, high):
  return randint(low, high)

def ask():
  answer = input()
  return answer.upper

def quiz():
  question = randomnum(1, 50)

def question1():
  linespace(4)
  print(str(lives))
  print("What is the capital of Alberta?")
  ask()
  answer = ask
  if answer == "EDMONTON":
    print("Correct!")
    score += 1








name = input("What is your name?")






