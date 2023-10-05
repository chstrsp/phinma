import questionList
#update
main_menu = {
    1: 'Start',
    2: 'Exit'
}
score = 0
def print_menu():
    for key in main_menu.keys():
        print(key, '--', main_menu[key])

def start():
    global score
    print()
    game_start = input('press g to begin')
    if game_start == "g":
        sentence = questionList.get_random_question()
        print(sentence.get_question())
        print()
        user_input = input("Type the word above : ")
        print()
        if user_input == sentence.get_answer():
            score += 1
            print("Score :", score)
        else:
            score -= 1
            print("Score :", score)


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
