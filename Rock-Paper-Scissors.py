from random import choice


def wins_against_options(value, choices):
    # Returns a list that contains choices that value will win against
    value_index = choices.index(value)
    temp_choices = choices[value_index + 1:] + choices[:value_index]
    winning = temp_choices[int(len(temp_choices) / 2):]
    print(f"You will win against: {winning}")
    return winning


# win_states = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
file_name = "rating.txt"

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

with open(file_name) as f:
    scores = f.readlines()

for score_line in scores:
    if user_name in score_line:
        score = int(score_line.split()[1])
        break
    else:
        score = 0

# Determine game options
my_options = input()
if not my_options:
    options = ["rock", "paper", "scissors"]
else:
    options = my_options.lower().split(",")

print("Okay, let's start")

while True:
    my_choice = input()
    if my_choice == "!exit":
        print("Bye!")
        break
    elif my_choice == "!rating":
        print(f"Your rating: {score}")
    elif my_choice not in options:
        print("Invalid input")
        continue
    else:
        computer_choice = choice(options)
        if computer_choice == my_choice:
            print(f"There is a draw ({my_choice})")
            score += 50
        elif computer_choice in wins_against_options(my_choice, options):
            print(f"Well done. Computer chose {computer_choice} and failed")
            score += 100
        else:
            print(f"Sorry, but computer chose {computer_choice}")

# Output a line Enter your name: . Note that the user should enter his/her name on the same line (not the one following
# the output!)
# Read input specifying the user's name and output a new line Hello, <name>
# Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score
# specified in the rating.txt for this user as a starting point for calculating the score in the current game.
# If no, start counting user's score from 0.
# Read input specifying the list of options that will be used for playing the game (options are separated by comma).
# If the input is an empty line, play with default options.
# Output a line Okay, let's start
# Play the game by the rules defined on the previous stages:
# Read user's input
# If the input is !exit, output Bye! and stop the game
# If the input is the name of the option, then:
#     Pick a random option
#     Output a line with the result of the game in the following format (<option> is the name of the option chosen
#     by the program):
#         Lose -> Sorry, but computer chose <option>
#         Draw -> There is a draw (<option>)
#         Win -> Well done. Computer chose <option> and failed
# For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses,
# don't change the score.
# If the input corresponds to anything else, output Invalid input
# Play the game again (with the same options that were defined before the start of the game)

# How to determine which options are stronger or weaker that the option you're currently looking at? Well, you can
# try to do it this way: take the list of options (provided by the user of the default one). Find the option for
# which you want to know its relationships with other options. Take all the options that follow this chosen option
# in the list. Add to them the list of options that precede the chosen option. Now you have another list of options
# that doesn't include the "chosen" option and has the different order of elements in it (first go the options following
# the chosen one in the original list, after them are the ones that precede it). So, in this "new" list, the first half
# of options will be defeating the "chosen" option, and the second half will get beaten by it.
#
# For example, the user's list of options is rock,paper,scissors,lizard,spock. You want to know what options are weaker
# than lizard. By looking at the list spock,rock,paper,scissors you realize that spock and rock will be beating the
# lizard, and paper and scissors will get defeated by it. For spock it'll be almost the same, but it'll get beaten by
# rock and paper, and prevail over scissors and lizard. For the version of the game with 15 options, you can look at
# the picture above to understand the relationships between options.

