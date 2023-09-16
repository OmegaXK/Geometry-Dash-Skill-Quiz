# A quiz to determine your skill level in geometry dash.
# Quiz by Acer Of Dragons.
# Program by Omega_XK (omegaxk314@gmail.com).
# Original, unedited quiz here: 
# https://geometry-dash.fandom.com/f/p/2722795733647559979
# Raw quiz here:
# https://raw.githubusercontent.com/OmegaXK/Geometry-Dash-Skill-Quiz/main/raw_quiz.txt


from pathlib import Path 
import json 

# Load in the data.
path = Path('quiz_data.json')
contents = path.read_text()
quiz_data = json.loads(contents)

# Define the introduction.
introduction = quiz_data['introduction']

# Define the instructions.
instruc1 = quiz_data['instructions'][0]
instruc2 = quiz_data['instructions'][1]
instructions = instruc1 + instruc2

# Define the questions and options.
questions = quiz_data['questions']
options = quiz_data['options']

# Load the final question data. "fq" stands for "final question".
fq_instruc1 = quiz_data['final question']['instruc1']
fq_instruc2 = quiz_data['final question']['instruc2']
fq_options = quiz_data['final question']['options']
fq_point_list = list(quiz_data['final question']['options'].values())

# Load the experience data.
ranks = quiz_data['experience ranks']['ranks']
explanations = quiz_data['experience ranks']['explanations']


def main():
    """The main code for the quiz."""
    points = 0
    
    # Print the introduction and some whitespce before the questions.
    quiz_introduction()
    print('\n')
    
    # The first five questions.
    for index in range(0, len(questions)):
        next_point_value = question(questions[index], options[index])
        points += next_point_value
        
    # Final question.
    fq_points = final_question()
    points += fq_points
        
    # Evaluate results.
    print(f"\n\nYou scored {points} points!\n")
    
    # Print the user's rank.
    rank_explanation = calculate_rank(points)
    print(rank_explanation)


def quiz_introduction():
    """
    Print the introduction of the quiz. The user will press enter to
    move on to the next part of the introduction.
    """
    
    print(f'\n\n\n{introduction}\n')
    input('Press enter to continue: ')
    
    print(f'\n\n{instructions}\n')
    input('Press enter to continue: ')
    
    return


def question(question, options):
    """Ask a question and return the amount of points the player 
    recievesmfor that answer. Accepts a string for the question and a 
    dictionary with keys being the options and values being the point
    values as integers  (e.x. Stereo Madness: 25).
    """
    
    print(f"\n{question}\n")
    
    # Print the options.
    count = 1
    for option in options.keys():
        print(f"[{count}] {option}")
        count += 1
    
    # Make sure the player inputs one of the options.
    possible_answers = list(range(1, count))
    while True:
        try:
            answer = int(input('\n>>> '))
        except ValueError:
            print(f"\nPlease enter one of the following: {possible_answers}.")
            continue    
            
        if answer not in possible_answers:
            print(f"\nPlease enter one of the following: {possible_answers}.")
        else:
            break

    # Return the point value of the option the player chose.
    count = 1
    for option, points in options.items():
        if answer == count:
            return int(points)
        
        count += 1
        
        
def final_question():
    """
    Prompt the player with the final question and return the coorect
    amount of points.
    """
    fq_points = 0
    
    # Print the instructions and prompt the player to press enter.
    print(f"\n{fq_instruc1}\n{fq_instruc2}\n")
    input('Press enter to move on: ')
    print()
    
    # Print the options.
    count = 1
    for option in fq_options.keys():
        print(f"[{count}] {option}")
        count += 1
        
    # Collect the user's response.
    answer = (input('\n>>> ')).split()
    
    # Evaluate the user's response.
    count = 1
    for point_value in fq_point_list:
        if str(count) in answer:
            fq_points += point_value
        count += 1

    return fq_points


def calculate_rank(points):
    """Figure out the user's rank based on the amount of points."""
    
    # Loop through the rank point thresholds.
    for rank, point_value in ranks.items():
        if points >= point_value:
            user_rank = rank
            
    # Loop through the ranks and find the correct explanation.
    for rank, explanation in explanations.items():
        if user_rank == rank:
            user_explanation = explanation
    
    # Return the proper explanation.
    return user_explanation

        
if __name__ == '__main__':
    while True:
        main()
        answer = input('\nInput "r" to play again: ')
        if answer.lower() != "r":
            break