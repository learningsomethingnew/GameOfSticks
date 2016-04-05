

class MainMenu():

    def __init__(self):
        self.menu_banner = "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^"

    """Greeting prints the rules, banners, and calls draw menu"""
    def greeting(self):

        self.greeting = ["Welcome to Styx",
                         "There is a pile of sticks on the table.",
                         "You can take 1-3 sticks per turn",
                         "The one that has has one stick at the end looses",
                         "Which mode would you like to play?"]

        print(self.menu_banner)
        print(self.menu_banner + "\n")
        for sentence in self.greeting:
            print(sentence + '\n')

        self.draw_main_menu()

    def draw_main_menu(self):
        main_menu = ['1. 2 Player Mode ', 'Q to Quit the game']
        for menu_selection in main_menu:
            print(menu_selection)