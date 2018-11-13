import math as m
import random as r

def game1():
    x = True
    #lets the game run forever
    while (x == True):
        
        flag = True
        while (flag == True):
            input1 = input("Would you like to play a game? (yes or no): ")
            print(" ")
            input1 = input1.strip()
            input1 = input1.lower()

            if (input1 == "yes"):
                print("The game will start now")
                print(" ")
                flag = False
                
            elif (input1 == "no"):
                print("Sorry to see you leave.")
                print(" ")
                flag = False
                
            else:
                print("Please try again")
                print(" ")
                flag = True

                
        if (input1 == "no"):
            x = False
            break

                
        # gives the players the name they wish to be called.
        player1_name = input("Please input player one's name: ")
        print(" ")
        player1_name = player1_name.strip()

        player2_name = input("Please input player two's name: ")
        print(" ")
        player2_name = player2_name.strip()

        print("player's names are " + player1_name + " " + player2_name)
        print(" ")
        print("Now the two of you will be fighting to the death.")
        print(" ")
        print("Good luck for the both of you")
        print(" ")
        player1_health = 100
        player2_health = 100
        flag = True
        while (flag == True):
            # gives player one the option to attack or to defend
            inputs = True
            while inputs == True:
                player1_input = input("Player one, Attack or Defend: ")
                print(" ")
                player1_input = player1_input.strip()
                player1_input = player1_input.lower()
                if player1_input == "attack" or "defend":
                    inputs = False

                else:
                    print("Try again.")
                    print(" ")
                    inputs = True

            # gives player two the option to attack or to defend
            inputs = True
            while inputs == True:
                player2_input = input("Player two, Attack or Defend: ")
                print(" ")
                player2_input = player2_input.strip()
                player2_input = player2_input.lower()

                if player1_input == "attack" or "defend":
                    inputs = False
                else:
                    print("Please try again.")
                    print(" ")
                    inputs = True
                    
            # this algorithm gives the  results of the attacks by both players
            if (player1_input == "attack" and player2_input == "attack"):
                damage1 = r.randint(0, 10)
                damage2 = r.randint(0, 10)
                
                player2_health = player2_health - damage1 
                player1_health = player1_health - damage2
                
                print(player1_name + " did " + str(damage1) + " to player two")
                print(" ")
                print(player2_name + " has " + str(player2_health) + " now.")
                print(" ")
                
                print(player2_name + " did " + str(damage2) + " to player one")
                print(" ")
                print(player1_name + " has " + str(player1_health) + " now.")
                print(" ")
            
            # This algorithm gives the results of the attack of player 1 and the defense of player 2
            elif (player1_input == "attack" and player2_input == "defend"):
                damage1 = r.randint(0, 20)
                damage2 = r.randint(0, 20)
                
                player2_health = player2_health - (damage1 // 2)
                player1_health = player1_health - 1
                
                print(player1_name + " did " + str(damage1 // 2) + " to player two")
                print(" ")
                print(player2_name + " has " + str(player2_health) + " now.")
                print(" ")

                print(player2_name + " has defended this round")
                print(" ")
                print(player2_name + " " + str(1) + " to player one")
                print(" ")
                print(player1_name + " has " + str(player1_health) + " now.")
                print(" ")

                
            #this algorithm gives the results of the defence of player 1 and the attack of player 2
            elif (player1_input == "defend" and player2_input == "attack"):
                damage1 = r.randint(0, 10)
                damage2 = r.randint(0, 10)

                player2_health = player2_health - 1
                player1_health = player1_health -(damage1 // 2)


                print(player1_name + "has defended this round")
                print(" ")
                print(player1_name + " did " + str(1) + " to player two")
                print(" ")
                print(player2_name + " has " + str(player2_health) + " health left")
                print(" ")
                
                print(player2_name + " did " + str(damage1//2) + " to player one")
                print(" ")
                print(player1_name + " has " + str(player1_health) + " health left")
                print(" ")

            elif (player1_input == "defend" and player2_input == "defend"):
                print("Both players will do no damage this round")
                print(" ")
                
                


            #           determines who wins, in this case it player two will win
            if (player1_health <= 0):
                print(player2_name + " has won")
                print(" ")
                print(player1_name + " has " + str(player1_health) + " health left")
                print(" ")
                x = False
                inputs = False
                flag = False

            #           determines who wins, in this case it is player one who wins    
            elif (player2_health <= 0):
                print(player1_name + " has won")
                print(" ")
                print(player2_name + " has " + str(player2_health) + " health left")
                print(" ")
                x = False
                inputs = False
                flag = False
                
                

            
        
                
    return print("Program ends.")

game1()
