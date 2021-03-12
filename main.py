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



def quizstart():
  name = input("What is your name?")
  score = 0
  lives = 3
  
  
  while lives >= 0:
  
    question = randomnum(1, 30)




 #Question 1 answer "Edmonton"
    if question == 1:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the capital of Alberta?")
      answer = input()

      if answer.upper() == "EDMONTON":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1


 #Question 2 answer "Albany"
    if question == 2:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the capital of New York?")
      answer = input()

      if answer.upper() == "ALBANY":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
      



       #Question 3 answer "Popemobile"

    if question == 3:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the vehicle used by the pope during public appearances?")
      answer = input()

      if answer.upper() == "POPEMOBILE":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1




       #Question 4 answer "George Washington"

    if question == 4:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("Who was the first president of the United States?")
      answer = input()

      if answer.upper() == "GEORGE WASHINGTON":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1




       #Question 5 answer "name" variable

    if question == 5:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is your name?")
      answer = input()

      if answer.upper() == name.upper():
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1



       #Question 6 answer "Canada"

    if question == 6:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the second largest country by land mass?")
      answer = input()

      if answer.upper() == "CANADA":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1



       #Question 7 answer "75"

    if question == 7:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is 25 x 3?")
      answer = input()

      if answer == "75":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
      



       #Question 8 answer "Canada"

    if question == 8:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What country is known for maple syrup?")
      answer = input()

      if answer.upper() == "CANADA":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1


       #Question 9 answer "Water"

    if question == 9:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the common name for H₂O?")
      answer = input()

      if answer.upper() == "WATER":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1


       #Question 10 answer "5040"

    if question == 10:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does 7! equal?")
      answer = input()

      if answer == "5040":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1


       #Question 11 answer "Russia"

    if question == 11:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the largest country by land mass?")
      answer = input()

      if answer.upper() == "RUSSIA":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1


       #Question 12 answer "Vatican City"

    if question == 12:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the smallest country by land mass?")
      answer = input()

      if answer.upper() == "VATICAN CITY":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 13 answer "Noun"
  
    if question == 13:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("A person, place or thing is a...?")
      answer = input()

      if answer.upper() == "NOUN":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 14 answer "Barack Obama"
  
    if question == 14:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("Who was the first black president of the United States?")
      answer = input()

      if answer.upper() == "BARACK OBAMA" or answer.upper() == "OBAMA":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 15 answer "Barack Obama"
  
    if question == 15:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("Who was the 44th president of the United States?")
      answer = input()

      if answer.upper() == "BARACK OBAMA" or answer.upper() == "OBAMA":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 16 answer "Never Gonna give you up"
  
    if question == 16:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("Translate the following from Italian:'Non ti lascerà mai stare'")
      answer = input()

      if answer.upper() == "NEVER GONNA GIVE YOU UP":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 17 answer "Rick Roll"
  
    if question == 17:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the act of presenting a link on a online site that goes to Rick Astley-Never Gonna Give You Up?")
      answer = input()

      if answer.upper() == "RICK ROLL" or answer.upper() == "RICK ROLLING" or answer.upper() == "RICK ROLLED":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 18 answer "Potato"
  
    if question == 18:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What food caused a famine in Ireland that lasted from 1842 to 1852?")
      answer = input()

      if answer.upper() == "POTATOES" or answer.upper() == "POTATO":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 19 answer "Usain Bolt"
  
    if question == 19:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("As of 2021 who is the fastest person in the world?")
      answer = input()

      if answer.upper() == "USAIN BOLT":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 20 answer "Potato"
  
    if question == 20:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What food caused a famine in Ireland that lasted from 1842 to 1852?")
      answer = input()

      if answer.upper() == "POTATOES" or answer.upper() == "POTATO":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 21 answer "Homo Sapien"
  
    if question == 21:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What is the scientific name for humans?")
      answer = input()

      if answer.upper() == "HOMO SAPIEN" or answer.upper() == "HOMO SAPIENS":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 22 answer "2"
  
    if question == 22:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does 1+1 equal?")
      answer = input()

      if answer == "2":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 23 answer "0"
  
    if question == 23:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does (8073564 ÷ 826783678 ÷ 983749476 x 37386568436588 + (738658648658 x 3734837975975 ÷ 9379757479549 ÷ 4375484568568)) x 0 equal?")
      answer = input()

      if answer == "0":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 24 answer "1"
  
    if question == 24:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does anything to the power of 0 equal?")
      answer = input()

      if answer == "1":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 25 answer "0"
  
    if question == 25:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does anything times 0 equal?")
      answer = input()

      if answer == "0":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 26 answer "8008"
  
    if question == 26:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does 4004 x 2 equal?")
      answer = input()

      if answer == "8008":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 27 answer "1"
  
    if question == 27:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does -1+2 equal?")
      answer = input()

      if answer == "1":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 28 answer "25"
  
    if question == 28:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does 100÷4 equal?")
      answer = input()

      if answer == "25":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 29 answer "5"
  
    if question == 29:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does 20÷4 equal?")
      answer = input()

      if answer == "5":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1
 
 
 #Question 30 answer "14"
  
    if question == 30:
      linespace(3)
      print("Lives:", str(lives))
      print("Score", str(score))

      print("What does 28÷2 equal?")
      answer = input()

      if answer == "14":
        print("Correct!")
        score += 1
      else:
        print("Incorrect...")
        print("Minus 1 lives.")
        lives -= 1










  print("Game Over")
  print(name + ' your total score is ' + str(score) + ".")















quizstart()



