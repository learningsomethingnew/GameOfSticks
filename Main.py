from sys import exit
from os import system, name
from time import sleep
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
        self.user_quit_list = {'Quit', 'quit', 'q', 'Q'}
        self.error_message = ['Please enter one of the menu selections',
                              'Please select 1 - 3 player']

        self.rules = ["There is a pile of sticks on the table.",
                      "You can take 1-3 sticks per turn",
                      "The one that has no sticks at the end wins",
                      ]

        self.game_state = 0
        self.sticks_count = 20




        self.which_game_mode()


    def clear_screen(self):
        system('cls' if name == 'nt' else 'clear')


    def which_game_mode(self):
        mainTrue = True
        while mainTrue == True:
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
            answer = self.get_user_response()
            if answer in self.user_quit_list:
                self.user_quit()
            elif answer in {'R', 'r'}:
                for rule in self.rules:
                    print(rule)
                sleep(5)
            elif int(answer) == 1:
                self.clear_screen()
                self.f = SticksGame()
                self.f.game_logic()
            elif int(answer) == 2:
                self.clear_screen()
                self.g = SticksGameAI()
                self.g.game_logic()
            else:
                del self.f
                del self.g


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
