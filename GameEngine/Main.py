####################################################################
#
####################################################################
from GameEngine.ProcessInput import ProcessInput
from GameEngine.UpdateGame import UpdateGame
from GameEngine.RenderGame import RenderGame
from sys import exit

class Main():

    def __init__(self):
        self.process_input = ProcessInput()
        self.update_game = UpdateGame()

        #kicks off the main menu
        self.update_game.game_state

        #starts the game loop
        self.main_loop()

    """Controls the main game loop."""
    def main_loop(self):

        #controlling the game loop
        game_loop = True

        while game_loop:
                #prompting the user for input
                answer = self.process_input.prompt_user()

                #Testing if response is quit
                game_loop = False if answer == False else game_loop == True





        self.user_quit()


    def user_quit(self):
        print("Thanks for playing! Goodbye!")
        exit()

if __name__ == '__main__':
    f = Main()