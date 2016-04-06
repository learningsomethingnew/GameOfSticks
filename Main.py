from sys import exit
from os import system, name
from SticksGame import SticksGame
from SticksGameAI import SticksGameAI

class Main():
    def __init__(self):
        self.menu_banner = "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^"
        self.menu_divider = "---------------------------------------------------"
        self.greeting = ["Welcome to Styx",
                         "Please make a selection"]
        self.main_menu = ["1. Two Player Mode ",
                          "2. Player vs AI",
                          "R for rules",
                          "Q to Quit the game"]
        self.user_quit_list = ['Quit', 'quit', 'q', 'Q']
        self.error_message = ['Please enter one of the menu selections',
                              'Please select 1 - 3 player']

        self.rules = ["There is a pile of sticks on the table.",
                      "You can take 1-3 sticks per turn",
                      "The one that has has one stick at the end looses",
                      ]

        self.game_state = 0
        self.sticks_count = 20

        self.f = SticksGame()
        self.g = SticksGameAI()

        self.which_game_mode()


    def clear_screen(self):
        system('cls' if name == 'nt' else 'clear')


    def which_game_mode(self):
        # Print greeting

        self.clear_screen()

        print(self.menu_banner)
        print(self.menu_banner + '\n')
        for sent in self.greeting:
            print(sent)

        print(self.menu_divider + '\n')

        # print menu
        for menu in self.main_menu:
            print(menu)

        # get users response
        answer = int(self.get_user_response())
        if answer == False:
            self.user_quit()
        elif answer == 1:
            self.clear_screen()
            self.f.game_logic()
        elif answer == 2:
            self.clear_screen()
            self.g.game_logic()



    def user_quit(self):
        print("Thanks for playing! Goodbye!")
        exit()


    def get_user_response(self):
        return self.test_response(input(">>> "))


    def test_response(self, a_input):
        # Tests against each version of quit to see
        # if the user wants out
        for word in self.user_quit_list:
            if a_input == word:
                return False
            else:
                return a_input



if __name__ == '__main__':
    f = Main()
