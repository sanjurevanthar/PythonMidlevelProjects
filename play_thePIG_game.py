#Here we are designing a mini project on PIG game
#Users or players -> 2-4
import random


#roll()-> a method or function which returns a number from 1->6 (Single Dice Outcomes )

def roll():
    #we use random here to generate the number
    start_val =1
    end_val = 6
    return random.randint(start_val,end_val)

#This piece of code runs util unless you put in a valid Input
while True:
    no_user = input("Enter the number of user playing ? ")
    if no_user.isdigit():
        no_user = int(no_user) #we update the number of user into integer value
        #the range should be from 2 to 4
        if 2<= no_user <= 4:
            break #if this condition satisfies -> come out of this if else ask for valid i/p
        else:
            print("Please enter a number between 2 and 4")
    else:
        print("Invalid Input")

max_score = 50 #if a player reaches 50 they wins

#store the players score in the list
players_score = [0]*no_user #[0,0,0,0] #initially 0 list to track the score of each player
print(players_score)

#we play until any one of the player get the max_score
while max(players_score) < max_score:

    #Dice role chances from user 1-> 4
    for index in range(no_user):
        print("\nPlayer No: ", index+1 , "is playing now!\n")

        current_score = 0
        #Now Iterate for the dice roll by calling roll() function
        while True:
            options = input("Do you want to play ? (y) ")
            if options.lower() == 'y':
                #we call the roll()
                roll_output = roll()
                if roll_output == 1:
                    current_score = 0 #cupdate back to 0
                    break
                else:
                    current_score += roll_output
                    print("Your Score is  ", current_score)
            else:
                print("Invalid input: you lost your turn")
                break

        #Now update the list
        players_score[index] += current_score
        print("Your score is ", players_score[index])

#Base condition:
print("User", players_score.index(max(players_score))+1, "Wins the Game! with", max(players_score), "points")



