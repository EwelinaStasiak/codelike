import random


def generate_boss_number():

    number_list = [0,1,2,3,4,5,6,7,8,9]

    guess_numbers = []
    while len(guess_numbers) < 3:

        number = random.choice(number_list)
        guess_numbers.append(str(number))
        number_list.remove(number)

    return guess_numbers


def get_player_input():
    while True:
        player_input = input('Please write 3-digit number: ')
        if player_input.isdigit() and len(player_input) == 3 and len(set(player_input)) == len(player_input):
            break
        else:
            print('Number should be 3-digit!')
    return list(player_input)


def compare_user_answer(guess, correct_answer):
    hints = []
    for i in range(len(guess)):
        if guess[i] == correct_answer[i]:
            hints.insert(0, 'hot')
        elif guess[i] in correct_answer:
            hints.append('warm')
    if not hints:
        hints = ['cold']
    return hints


def play_a_game():
    player_guesses = 10
    correct_answer = generate_boss_number()
    print(correct_answer)
    while player_guesses > 0:
        user_input = get_player_input()
        feedback = compare_user_answer(user_input, correct_answer)
        print(feedback)
        if feedback == ['hot', 'hot', 'hot']:
            print("You won!")
            break
        player_guesses -= 1


