print("Welcome to my first game v1.2")
name = input("what is your name? ")
age = int(input("What is your age? "))
if age >= 18:
    print ("Great!", name, " you are old enough to continue and play the the game")
    print ("Alright, you have 3 lives and 2 skips. Type 'skip' to pass a question")
    score = 0 # starts player's score at 0 !
    lives = 3 # player's start with three chances !'
    skip = 2 # player's only get two skip for whole game'
    questions = ["Question 1 : What is the capital of Bihar? ", "Question 2 : How many states are there in India? ", "Question 3 : Which state of india is largest in terms of population? ", "Question 4: Which organelle is known as the powerhouse of the cell? ","Question 5: Which river is known as the 'Sorrow of Bihar? ","Question 6: What is the Sl unit of electric current? ","Question 7: Who was the first President of India? ","Question 8: Which vitamin is produced when human skin is exposed to sunlight? ","Question 9: What is the chemical formula of common table salt? ","Question 10: Which planet is known as the Red Planet? "]
    answers = [ ["patna"], ["28", "twenty eight" , "twenty eight"], ["up", "uttar pradesh"], ["mitochondria", "'mitochondrion"], ["kosi", "kosi river"],["ampere", "amp", "a"] , ["dr rajendra prasad", "rajendra prasad"], [ "vitamin d", "d"], ["nacl", "sodium chloride"],["mars"] ]
    for i in range (len( questions)):
        if lives == 0 :
            break
        while True :
            ans = input(questions[i]). lower( ). strip( )
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
    print( " Game Over, ", name, "! your final score is", score)                
else:
    print ("ohh! sorry, your age needs to be 18 or higher to continue")
