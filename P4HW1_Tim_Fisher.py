# Tim Fisher
# 11/01/2024
# P4HW1
# Create and evaluate loops to collect scores and evalute under certain parameters


print()
print()
# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Empty list to store the scores
score_list = []

# for loop to collect the scores
for s in range(num_scores):

    # Allow looping until a valid score is entered
    while True: 
        score = float(input(f"Enter score #{s + 1}: "))
        
        # Check if the score is valid
        if 0 <= score <= 100:
            # Add the valid score to score_list
            score_list.append(score)
            # Exit the while loop if the score is valid
            break  
        else:
            print()  
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            
            

# Find the lowest score
lowest_score = min(score_list)

# Create a list by removing the lowest score
modified_list = score_list.copy()
modified_list.remove(lowest_score)  

# Calculate the average of the modified list
if modified_list:
    # Create variable for the average of scores
    average_score = sum(modified_list) / len(modified_list)
    
    # Assign letter grade based on the average score
    if average_score >= 90:
        letter_grade = 'A'
    elif average_score >= 80:
        letter_grade = 'B'
    elif average_score >= 70:
        letter_grade = 'C'
    elif average_score >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    # Display the results in a neat lined format
    print()
    print("\n--------------------Results---------------------")
    print(f"{'Lowest Score':14} : {lowest_score}")
    print(f"{'Modified List':14} : {modified_list}")
    print(f"{'Scores Average':14} : {average_score:.2f}")
    print(f"{'Grade':14} : {letter_grade}")
    print("------------------------------------------------")
