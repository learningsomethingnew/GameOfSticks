from sys import exit
from os import system, name

menu_banner = "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^"
menu_divider = "---------------------------------------------------"
greeting = ["Welcome to Styx",
            "Please make a selection"]
main_menu = ['1. 2 Player Mode ', 'R for rules', 'Q to Quit the game']
user_quit_list = ['Quit', 'quit', 'q', 'Q']
error_message = ['Please enter one of the menu selections', 'Please select 1 - 3 player']

rules = ["There is a pile of sticks on the table.",
         "You can take 1-3 sticks per turn",
         "The one that has has one stick at the end looses",
         ]

game_state = 0
sticks_count = 20


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def which_game_mode():
    # Print greeting

    clear_screen()

    print(menu_banner)
    print(menu_banner + '\n')
    for sent in greeting:
        print(sent)

    print(menu_divider + '\n')

    # print menu
    for menu in main_menu:
        print(menu)

    # get users response
    answer = int(get_user_response())
    if answer == False:
        user_quit()
    elif answer == 1 and game_state == 0:
        clear_screen()
        pvp_game()


def user_quit():
    print("Thanks for playing! Goodbye!")
    exit()


def get_user_response():
    return test_response(input(">>> "))


def test_response(a_input):
    # Tests against each version of quit to see
    # if the user wants out
    for word in user_quit_list:
        if a_input == word:
            return False
        else:
            return a_input


def test_response_in_game(a_input):
    a_input = int(a_input)

    # Tests against each version of quit to see
    # if the user wants out
    for word in user_quit_list:
        if a_input == word:
            return False
        elif a_input > 3:
            pass
        else:
            return a_input


def test_player_input(a_user_input):
    if a_user_input == 1 or a_user_input == 2 or a_user_input == 3:
        return a_user_input
    else:
        pass


def print_current_game_state(a_pvp_state, a_sticks_count):
    print("There are %i sticks on the table" % a_sticks_count)
    print("Player %i: How many do you take? 1, 2, or 3?" % a_pvp_state)


def remove_sticks(a_number):
    sticks_count -= a_number
    print(sticks_count)
    return sticks_count


def winner(a_pvp_state):
    print("%s Wins!" % (a_pvp_state))
    which_game_mode()


def pvp_game():
    pvp_sticks_count = 20

    print("in game")
    pvp_state = 1
    game_run = True



    while game_run == True:

        print_current_game_state(pvp_state, pvp_sticks_count)

        if pvp_sticks_count > 1:
            user_response = test_response_in_game(input(">>> "))
            answer = (int(user_response))
            pvp_sticks_count -= answer
            print(pvp_sticks_count)

            if pvp_state == 1:
                pvp_state = 2
            elif pvp_state == 2:
                pvp_state = 1

        elif pvp_sticks_count == 1 and pvp_state == 1:
            winner(pvp_state)
            game_run = False
        elif pvp_sticks_count == 1 and pvp_state == 2:
            winner(pvp_state)
        elif pvp_sticks_count == 0 and pvp_state == 1:
            pvp_state = 2
            winner(pvp_state)
        elif pvp_sticks_count == 0 and pvp_state == 2:
            pvp_state = 1
            winner(pvp_state)
        else:
            pass

    print("Out of Loop")






which_game_mode()
