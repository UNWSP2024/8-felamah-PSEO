# Author: Faith Lamah
# Date: 10/24/2025
# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random
def states_quiz():
    US_States = {'Alabama':'Montgomery', 'Montana':'Helena', 'Alaska':'Juneau', 'Nebraska':'Lincoln', 'Arizona':'Phoenix', 'Nevada':'Carson City', 'Arkansas':'Little Rock', 'New Hampshire':'Concord', 'California':'Sacramento', 'New Jersey':'Trenton', 'Colorado': 'Denver', 'New Mexico':'Santa Fe', 'Connecticut':'Hartford', 'New York':'Albany', 'Delaware':'Dover', 'North Carolina':'Raleigh', 'Florida':'Tallahassee', 'North Dakota':'Bismarck', 'Georgia':'Atlanta', 'Ohio':'Columbus', 'Hawaii':'Honolulu', 'Oklahoma':'Oklahoma City', 'Idaho':'Boise', 'Oregon':'Salem', 'Illinois':'Springfield', 'Pennsylvania':'Harrisburg', 'Indiana':'Indianapolis', 'Rhode Island':'Providence', 'Iowa':'Des Moines', 'South Carolina':'Columbia', 'Kansas':'Topeka', 'South Dakota':'Pierre', 'Kentucky':'Frankfort', 'Tennessee':'Nashville', 'Louisiana':'Baton Rouge', 'Texas':'Austin', 'Maine':'Augusta', 'Utah':'Salt Lake City', 'Maryland':'Annapolis', 'Vermont':'Montpelier', 'Massachusetts':'Boston', 'Virginia':'Richmond', 'Michigan':'Lansing', 'Washington':'Olympia', 'Minnesota':'Saint Paul', 'West Virginia':'Charleston', 'Mississippi':'Jackson', 'Wisconsin':'Madison', 'Missouri':'Jefferson City', 'Wyoming':'Cheyenne'}

    correct_answer = 0
    incorrect_answer = 0

    print('Welcome to State Quiz. There are 10 questions you need to answer.')

    for i in range(10):
        state = random.choice(list(US_States.keys()))
        guess = input(f'What is the capital of {state}?')
        if guess.lower() == US_States[state].lower():
            print('Correct!')
            correct_answer += 1
        else:
            print('Incorrect!')
            incorrect_answer += 1
            print(f'The correct answer is {US_States[state]}.')
        del US_States[state]

    print(f'The number of correct answers you got is {correct_answer}. ')
    print(f'The number of incorrect answers you got is {incorrect_answer}. ')
states_quiz()
