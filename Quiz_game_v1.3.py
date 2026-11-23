import random 
print("Welcome to my first game v1.3")
name = input("what is your name? ")
age = int(input("What is your age? "))
if age >= 18:
    print ("Great!", name, " you are old enough to continue and play the the game")
    print ("Alright, you have 3 lives and 2 skips. Type 'skip' to pass a question")
    score = 0 # starts player's score at 0 !
    lives = 3 # player's start with three chances !'
    skip = 2 # player's only get two skip for whole game'
    questions = ["What is the capital of Bihar? ", " How many states are there in India? ", "Which state of india is largest in terms of population? ", "Which organelle is known as the powerhouse of the cell? "," Which river is known as the 'Sorrow of Bihar? ","What is the Sl unit of electric current? ","Who was the first President of India? "," Which vitamin is produced when human skin is exposed to sunlight? ","What is the chemical formula of common table salt? ","Which planet is known as the Red Planet? "]
    answers = [ ["patna"], ["28", "twenty eight" , "twenty eight"], ["up", "uttar pradesh"], ["mitochondria", "'mitochondrion"], ["kosi", "kosi river"],["ampere", "amp", "a"] , ["dr rajendra prasad", "rajendra prasad"], [ "vitamin d", "d"], ["nacl", "sodium chloride"],["mars"] ]
    order = list (range(len(questions)))
    random.shuffle(order)
    q_num = 1
    for i in order :
        if lives == 0 :
            break
        while True :
            ans = input (f" Question {q_num} : {questions [i]}"). lower( ). strip( )
            if ans == "skip":
                if skip > 0:
                    skip = skip - 1
                    print ("Skipped ! Skips left: ", skip)
                    break
                else: 
                    print ("No skip left ! you must answer this one. ") 
            elif ans in answers [i] :
                score = score + 10
                print (" Correct ! Score: ", score)
                break
            else:
                 lives = lives - 1 
                 if lives == 0:
                     print ("Wrong! No lives left !") 
                     break
                 else: 
                    print (" Wrong! Lives left: ", lives) 
        q_num = q_num + 1
    print( " Game Over, ", name, "! your final score is", score)                
else:
    print ("ohh! sorry, your age needs to be 18 or higher to continue")
