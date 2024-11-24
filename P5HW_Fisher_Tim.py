# Tim Fisher
# 11/08/2024
# P5HW
# Create a dual game with Definition's, Function's, and Library's


# Import rando library for generating random numbers
# Import emoji library to use emoji's in the code

import random
import emoji

def main():
 #"""Main function to run the game with a replay option."""
    while True:
        # Welcome message
        print("\n\n")
        print("                         \U0001F609\U0001F609 !!! Welcome !!! \U0001F609\U0001F609")
        print("                                    to")
        print("                    \U0001F609\U0001F609\U0001F609 !!! Striking Mania !!! \U0001F609\U0001F609\U0001F609\n\n")
        print()
        print("      The objective of this game: a random number of 1-5 will be generated.")
        print("    You must guess/strike the number that is generated before it's generated.")
        print("                 If you guess/strike correctly, you win a point.")
        print("                   The first to score 3 points wins the game!\n")
        for _ in range(29):
            print("\U0001F4A3", end=" ")
        print("\n\n")    
  # Ask the player if it's a 1-player or 2-player game
        mode = input("Do you want to play a 1-Warrior or 2-Warrior game? (Enter 1 or 2): ")
        
        if mode == '1':
            # Create the first player
            player1 = create_character()
            make_believe_player = {
                "Name": "Virtual's",  # Create AI opponent without asking for input
                "Points": 0,
                "Missed": 0
            }
            play_game(player1, make_believe_player, one_player=True)
        elif mode == '2':
            # Create both players
            player1 = create_character()
            player2 = create_character()
            play_game(player1, player2, one_player=False)
        else:
            print("Invalid input. Please enter 1 or 2.")
            continue

        # Ask if the players want to play again
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print()
            print()
            print("                             !!! Great  Battle !!!")
            print("                            !!! Until Next Time !!!")

            break

def create_character():
    """This function creates a character and returns a dictionary of their attributes."""
    # Get input from the user for the character's attributes
    print()
    name = input("Enter your Warrior's name: ")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
   
    
    # Initialize character attributes
    character = {
        "Name": name,
        "Points": 0,
        "Missed": 0
    }
    
    # Return the character dictionary
    return character

def guess_number():
    """Randomly draws a number between 1 and 5."""
    return random.randint(1, 5)

def play_game(player1, player2, one_player):
    """Main game loop. It runs until one player reaches 3 points."""
    while player1["Points"] < 3 and player2["Points"] < 3:
        # Player 1's turn
        print(f"\nWarrior {player1['Name']}'s Strike:")
        player_guess = int(input(f"Guess a number between 1 and 5: "))
        correct_number = guess_number()
        update_score(player1, player_guess, correct_number)

        if player1["Points"] >= 3:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("                           \U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3")
            print("                           \U0001F4A3                       \U0001F4A3")
            print("                           \U0001F4A3   !!! Game Over !!!   \U0001F4A3")
            print("                           \U0001F4A3                       \U0001F4A3")
            print("                           \U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3")
            print("\n\n\n\n\n\n\n\n\n")       
            break
        
        # Player 2's turn
        if one_player:
            print("\nWarrior Virtual's Strike:")
            player_guess = random.randint(1, 5)  # AI makes a random guess
        else:
            print(f"\nWarrior {player2['Name']}'s Strike:")
            player_guess = int(input(f"Guess a number between 1 and 5: "))
        
        correct_number = guess_number()
        update_score(player2, player_guess, correct_number)

        if player2["Points"] >= 3:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("                           \U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3")
            print("                           \U0001F4A3                       \U0001F4A3")
            print("                           \U0001F4A3   !!! Game Over !!!   \U0001F4A3")
            print("                           \U0001F4A3                       \U0001F4A3")
            print("                           \U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3\U0001F4A3")
            print("\n\n\n\n\n\n\n\n\n")  
            break

    # Display final character stats at the end of the game
    print("------------------------------------------------")
    print("Warrior's Final Battle Scores")
    display_characters([player1, player2])

def update_score(player, player_guess, correct_number):
    """Updates the player's points or missed attempts based on the guess."""
    print(f"The correct number was {correct_number}.")
    if player_guess == correct_number:
        player["Points"] += 1
        print(f"Warrior {player['Name']} Striked correctly \U0001F604\U0001F604 Points: {player['Points']}")
    else:
        player["Missed"] += 1
        print(f"Warrior {player['Name']} Striked wrong \U0001F626\U0001F626 Missed: {player['Missed']}")

def display_characters(character_list):
    """Displays the attributes of all characters in the character list."""
    
    
    print("------------------------------------------------")
    for character in character_list:
        print(f"Name: {character['Name']}, Points: {character['Points']}, Missed: {character['Missed']}")
        
        # Find the player with the highest points to congratulate
    winner = max(character_list, key=lambda x: x["Points"])
    print(f"\n\U0001F64C \U0001F64C \U0001F64C \U0001F525\U0001F525 Congratulation's to {winner['Name']} for the Victory!!!")
    print()
    print("\U0001F64C \U0001F64C \U0001F64C \U0001F525\U0001F525 You Won the Battle of Striking Mania!!!")
    print()
    print("\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604")
    print("\n\n\n\n\n")
# Call the game
if __name__ == "__main__":
    main()



