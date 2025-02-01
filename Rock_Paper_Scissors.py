Player1 = input("Player 1 Enter your answer :").lower().capitalize()
Player2 =input("Player 2 enter your answer :").lower().capitalize()
if  Player1 =="Scissor" and Player2 =="Rock" :
    print("Player 2 Wins!")
elif Player1 =="Rock" and Player2 =="Scissor":
    print("Player 1 Wins!")
elif Player1 =="Paper" and  Player2 =="Rock":
    print("Player 1 Wins!")
elif Player1 =="Rock" and Player2=="Paper":
    print("Player 2 Wins!")
elif Player1 =="Paper" and Player2=="Scissor":
    print("Player 2 Wins!")
elif Player1 =="Scissor" and Player2=="Paper":
    print("Player 1 Wins!")
elif Player1==Player2:
    print("It's a Tie!")
else :
    print("Try again!")






