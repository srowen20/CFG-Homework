# TASK 1: CONDITIONAL FLOW

"""
QUESTION 1

Create a program that tells you whether or not you need an umbrella when you leave 
the house.

The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'
"""

raining = input('Is it raining outside? (y/n) ')
if raining.lower() == "y":
    print("Take an umbrella")
elif raining.lower() == "n":
    print("You don't need an umbrella")
else:
    print("Invalid response")

"""
QUESTION 2 

I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 
deposit. I've written a program to check that I can afford the cost, but something 
doesn't seem right. Have a look at my program and work out what I've done wrong


my_money = input('How much money do you have? ')
boat cost = 20 + 5
if my_money < boat_cost:
print('You can afford the boat hire')
else :
print('You cannot afford the board hire'
"""

# ANSWER: 
# 1. There is no underscore '_' between 'boat' and 'cost' so the computer 
# thinks they're two different variables, and writing them together like this is 
# invalid syntax. 
# 2. There are also no indents within the if function and so it won't
# accept this. 
# 3. There is an open bracket on the lat print line which must be closed.
# 4. my_money is automatically input as a string, so to compare it to another 
# number it must first be converted to a float (as it might have decimal places) 
# 5. It doesn't make sense to be able to afford the boat if you have less money 
# than the cost of the boat, so this must be changed from a 'less than' to a
# 'greater than' operator. 
# 6. There is a spelling mistake on the final print line, where it should say 
# 'boat' and not 'board'
# The below shows how it should be written:

my_money = input('How much money do you have? ')
boat_cost = 20 + 5
if float(my_money) > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the boat hire')


"""
QUESTION 3

Your friend works for an antique book shop that sells books between 1800 and 1950 
and wants to quickly categorise books by the century and decade that they were 
written. Write a program that takes a year (e.g. 1872) and outputs the century and 
decade (e.g. "Eighteenth Century, Seventies")
"""

# IMPORTANT TO NOTE: the 1800s are in the 19th century, and the 1900s are in the 
# 20th Century

import datetime

year_written = input('What year was the book written? ')

decades = [
    'Noughties',
    'Teens',
    'Twenties',
    'Thirties',
    'Fourties',
    'Fifties',
    'Sixties',
    'Seventies',
    'Eighties',
    'Nineties'
]

def convert_to_words(year):

    if year[0:2] == '18':
        century = 'Nineteenth Century'
    elif year[0:2] == '19':
        century = 'Twentieth Century'
    else:
        print('This book does not belong in this book shop, or the year entered is wrong')

    decade_num = int(year[2])
    decade = decades[decade_num]

    print(century + ', ' + decade)
    
convert_to_words(year_written)


# TASK 2: LISTS AND DICTIONARIES

""" 
Question 1

I have a list of things I need to buy from my supermarket of choice.

shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]

print(shopping_list[1])

I want to know what the first thing I need to buy is. However, when I run the program 
it shows me a different answer to what I was expecting? What is the mistake? How 
do I fix it """

# Python Indexes start with '0'. Therefore, when selecting the first item you must select 
# the '0' index and this will print the first item in the list. The second item has index 
# '1' and so on.

# This is the corrected version:

shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]

print(shopping_list[0])

"""
Question 2

I'm setting up my own market stall to sell chocolates. I need a basic till to check the 
prices of different chocolates that I sell. I've started the program and included the 
chocolates and their prices. Finish the program by
asking the user to input an item and then output its price.
"""

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

for key in chocolates:
    print(key)

item = input('Pick an item from the list printed above: ').lower()

print('The price of ' + item + ' chocolate is ' + str('{:.2f}'.format(chocolates[item])))

"""
Question 3

Write a program that simulates a lottery. The program should have a list of seven 
numbers that represent a lottery ticket. It should then generate seven random 
numbers. After comparing the two sets of numbers, the program should output a 
prize based on the number of matches:

· £20 for three matching numbers
· £40 for four matching numbers
· £100 for five matching numbers
· £10000 for six matching numbers
· £1000000 for seven matching numbers
"""

import random

input_numbers = input('Input your lottery numbers, leaving a space between each number: ')
numbers = input_numbers.split(' ')
if len(numbers) != 7:
    print('You entered the wrong number of items, please try again.')
    input_numbers = input('Input your lottery numbers, leaving a space between each number: ')

random_numbers = []

for i in range(0,7):
    num = random.randint(0,10)
    random_numbers.append(str(num))

count = 0

for i in numbers:
    if int(i) in random_numbers:
        count+=1

prize = [20, 40, 100, 10000, 1000000]

if 3 <= count <= 7:
    prize_money = prize[count - 3]
    print('You have won! You got ' + str(count) + ' matching numbers! Your prize money is £' + str(prize_money))
else:
    print('You did not get enough matching numbers. Better luck next time!')

# TASK 3 (Read and Write files)

"""
Question 1
You're having coffee/tea/beverage of your choice with a friend that is learning to 
program in
Python. They're curious about why they would use pip. Explain what pip is and one 
benefit of using pip.
"""

# Pip is the python package manager which allows you to install and use packges written by other people. 
# it is free to use and allows you to use many more in-built functions for specific applications. 
# It is easy to install and makes package installation very easy. 
# It also makes it easy to uninstall packages. 

"""
Question 2
This program should save my data to a file, but it doesn't work when I run it. What 
is the problem and how do I fix it?
""" 

""" poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'r') as poem_file:
    poem_file.write(poem) """

# The file was opened in the mode 'read'. This means the file cannot be written to and can only be 
# accessed to read.

# The correct version is written below:
poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w+') as poem_file:
    poem_file.write(poem)

"""
Question 3

Here is a snippet of Elton John’s song “I’m Still Standing”

You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use
And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away
Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind
I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)

Tasks:
1. Write the lyrics to a new file called song.txt
2. Check that a file has been created successfully.
3. Then read lines from this file and print out ONLY those lines that have a word 
‘still’ in them. 
"""

# task 1: write the lyrisc to a new file called song.txt

lyrics = '''You could never know what it's like 
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use

And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away

Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind

I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)'''

with open('song.txt', 'w+') as still_standing:
    still_standing.writelines(lyrics)


with open('song.txt', 'r') as still_standing:
    print(still_standing.readlines()) 


word = 'still'
with open('song.txt', 'r') as still_standing:
    for line in still_standing:
        if word in line.lower():
            print(line, end = '')



# TASK 4 (API)

"""
Question 1

In this session you used the Pokémon API to retrieve a single Pokémon.

I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
Use a list to store about 6 Pokémon IDs. Then in a for loop call the API to retrieve the data for 
each Pokémon. Save their names and moves into a file called 'pokemon.txt'
"""

import random
import requests
from pprint import pprint as pp

pokemon_numbers = []
for i in range(6):
    n = random.randint(1,898)
    pokemon_numbers.append(n)

names_moves = []

for i in pokemon_numbers:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
    response = requests.get(url)
    
    pokemon = response.json()
    poke_name = pokemon['name'].capitalize()
    
    moves = pokemon['moves']
    poke_moves = []
    for j in moves:
        poke_m = j['move']['name'].capitalize()
        poke_moves.append(poke_m)

    poke_moves = ', '.join(str(x) for x in poke_moves)
    if poke_moves == '':
        poke_moves = 'This Pokemon has no saved moves'
    names_moves.append(poke_name + ': ' + poke_moves + '\n')


with open('pokemon.txt', 'w+') as pokemon_details:
    pokemon_details.writelines(names_moves)

with open('pokemon.txt') as pokemon_details:
    pp(pokemon_details.readlines())



"""
Question 2 (optional)
Here is a link to a really cool API: https://opentdb.com/

Answer the following questions:
· What is the name of this API?
· What does it do?
· Example URL to make a call to this API?
· Example output?
"""

# 1. What is the name of this API?
   # it is called 'Open Trivia Database

# 2. What does it do?


# 3. Example URL to make a call to this API?
import requests
from pprint import pprint as pp
import random
from html import unescape

# Access the API
url = 'https://opentdb.com/api.php?amount=10&category=9'
response = requests.get(url)
trivia = response.json()
pp(trivia)

count = 0 # To know what question number you are on
score = 0 # Keep track of the score

# A for loop to go through each question
for i in trivia['results']:
    # Start at question 1
    count +=1 

    # Decode special characters from html to a format python can read
    question = unescape(i['question'])
    print('Question ' + str(count) + ': ' + question) # Print the question number and the question

# There are boolean and multiple choice questions. Separate the process for these two.
    if i['type'] == 'boolean':
        # Create a dictionary for the answers and print the options for the player
        answer_dictionary = {'a)': 'True', 'b)': 'False'}
        print('a) True \nb) False')

# Multiple choice questions
    elif i['type'] == 'multiple':
        idx = []
        idx = random.sample(range(4), 4) # Create list of numbers from 0 to 4 in a random order

        answers = i['incorrect_answers'] 
        answers.append(i['correct_answer']) # combine the list of incorrect answers with the correct one

        options = []

        for j in idx:
            options.append(unescape(answers[j])) # create a new list with all choices of answer in a random order

        letter = ['a)', 'b)', 'c)', 'd)']
        answer_dictionary = dict(zip(letter, options)) # Create a dictionary with letters as keys and answers as values
        print('Your choice of answers are: ')
        
        for key, value in answer_dictionary.items():
            print('{} {}'.format(key, value)) # Print the dictionary in a nice way, i.e. 'a) answer'

    answer = input('Type your answer to the question here: ') # user inputs 'a', 'b', etc. 
    answer = answer_dictionary[(answer.lower() + ')')] # letter is converted to lower case and the value from the dictionary is saved as answer

    if answer.lower() == unescape(i['correct_answer']).lower(): # value is compared to the lower case version of the correct answer
        score +=1 # if correct, the score increases by 1
        print('Correct! Your score is now ' + str(score) + '/' + str(count)) # the current score is printed
    else:
        # if not correct the correct answer is printed along with the current score
        print('Incorrect. The correct answer is ' + unescape(i['correct_answer']) + '. Your score is ' + str(score) + '/' + str(count))

print('Well done for completing the quiz. Your final score is ' + str(score) + '/' + str(count))