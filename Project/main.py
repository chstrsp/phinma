import questionList

main_menu = {
    1: 'Start',
    2: 'Exit'
}
score = 0
lives = 5
def print_menu():
    for key in main_menu.keys():
        print(key, '--', main_menu[key])

def start():
    global score
    global lives
    game_start = input('press g to begin ')
    if game_start.lower() == "g":
        print("\nLives: ", lives)
        print("Score: ", score)
        sentence = questionList.get_random_question()
        print(sentence.get_question())
        print(sentence.get_clue())
        user_input = input("Enter your answer: ")

        if user_input.lower() == sentence.get_answer().lower():
            score += 1
        else:
            score -= 1


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            start()
        elif option == 2:
            exit()
        else:
            print('Invalid user input')
