from art import logo, vs
from game_data import data
from random import shuffle
import os

DATA_LENGTH = len(data)
shuffle(data)


def comparison(guess, person_a, person_b):
    """
    Print the comparison text
    """
    if guess == 'a' and person_a['follower_count'] > person_b['follower_count']:
        return True
    elif guess == 'b' and person_a['follower_count'] < person_b[
            'follower_count']:
        return True
    else:
        return False


def get_data(current_index):
    """
    Get the data to compare
    """
    # Get data for people to compare
    person_a = data[current_index]
    person_b = data[current_index + 1]

    # Format the data
    return person_a, person_b


def format_data(data):
    """
    Format the person's data into a line of text
    """
    info = f"{data['name']}, a {data['description']}, from {data['country']}."
    return info


def request_guess_and_make_comparison(person_a, person_b, score):
    """
    Shows who we are guessing has higher follower count and requests a guess
    """
    print(f"Compare A: {format_data(person_a)}")
    print(vs)
    print(f"Against B: {format_data(person_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    correct_guess = comparison(guess, person_a, person_b)
    if correct_guess:
        score += 1
        # Clear the screen and print the logo
        os.system('clear')
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        os.system('clear')
        print(f"Sorry, that's wrong. Final score: {score}")

    return correct_guess, score


def run_game():
    """
    Runs the higher-lower game
    """
    correct_guess = True
    index = 0
    score = 0

    while index < DATA_LENGTH and correct_guess:
        person_a, person_b = get_data(index)
        correct_guess, score = request_guess_and_make_comparison(
            person_a, person_b, score)
        index += 1
