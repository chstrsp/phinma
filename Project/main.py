import questionList


def main_menu():
    print("[1] Start ")
    print("[2] Exit ")


def start():
    game_start = input('Press G to begin ')
    lives = 5
    score = 0
    while game_start.lower() == "g":

        print("\nLives: ", lives)
        print("Score: ", score)
        sentence = questionList.get_random_question()
        print(sentence.get_question())
        print(sentence.get_clue())
        user_input = input("Enter your answer: ")

        if user_input.lower() == sentence.get_answer().lower():
            print("Correct! You collected a piece of trash from the water.")
            score += 1
        else:
            print("Incorrect! You lost a life")
            lives -= 1

        if lives == 0:
            print("GAME OVER")
            print('Your score is ', score, "\n")
            print('Press 1 to continue')
            print('Press 2 to exit ')
            game_over = int(input('Enter your choice: '))
            if game_over == 1:
                start()
            elif game_over == 2:
                break



print("###################")
print("#### AQUALORE #####")
print("###################")
main_menu()
option = int(input('Enter your option: '))
if option == 1:
    start()
elif option == 2:
    pass
else:
    print("Invalid option")
    main_menu()
    option = int(input('Enter your option: '))





