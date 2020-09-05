import random
count = 0
count_limit = 10
computer_win = 0
player_win = 0
draw_game = 0
while count_limit != count:
    choice = ["S","W","G"]
    player = input("Choose S as snake and W as water and G as gun:\n")
    computer = random.choice(choice)
    print("computer output is:", computer)
    if player == "S":
        if computer == "W":
            print ("player win")
            player_win = player_win + 1
        elif computer == "G":
            print(" computer win") 
            computer_win= computer_win + 1
        elif computer == "S":
             print("play again") 
             draw_game = draw_game + 1   
    elif player == "W":
        if computer == "G":
            print("player win")
            player_win = player_win + 1
        elif computer == "S" :
            print(" computer win") 
            computer_win= computer_win + 1
        elif computer == "W":
             print("play again")
             draw_game = draw_game + 1 
    elif player == "G":
        if computer == "S":
            print(" palyer win") 
            player_win = player_win + 1 
        elif computer == "W":
            print("computer win") 
            computer_win= computer_win + 1
        elif computer == "G":
             print ("play again") 
             draw_game = draw_game + 1  
    count = count + 1 
print("Number of times player wins:\n",player_win)
print("Number of times computer win:\n", computer_win)  
print("Number of times the game is draw:\n",draw_game)                   
print("count_limit is finished ")  
if player_win < computer_win:
    print ("computer is the main winner of whole game by" , computer_win)
else:
     print ("player is the main winner of whole game by", player_win)   
            

        
    

