print("Welcome to my First Game!")
name = input("What is your name? ")
age = int (input (" What is your age? "))
if age >= 18:
    print (" Awesome", name, " - you are old enough to continue and play!")
    score = 0 # Starts the player's score at 0
    
    # --- Question 1 ---
    while True:
        ans = input( " Question 1: What is the capital of bihar? ")
        if ans.lower( )== "patna":
           score = score + 10
           print( "Correct ! Score: ", score )
           break  # stops repeating Question 1 and moves to Question 2 !
        else:
         print( "Wrong ! Please try again. ")    
     # --- Question 2 ---
    while True:
        ans2 = input(" Question 2 : What gas do plants absorb from air? ")
        if ans2.lower( )== "carbon dioxide" or  ans2.lower( )== "co2":
             score = score +10
             print("Correct ! Score: ", score )
             break # stops repeating Question 2 and moves to Question 3 !
        else:
            print("Wrong ! Please try again.")
    print(" Game over, sorry for short game", name, " ! Your final score is: ", score)
                 
else : 
     print ("Sorry",  name, "- you need to be 18 years or older to continue")
