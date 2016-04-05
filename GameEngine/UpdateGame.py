####################################################################
# Runs the logic of the game
####################################################################

class UpdateGame():

    def __init__(self):
        self.game_state = 0

    def set_game_state(self):
        self.game_state = 0

    def get_game_state(self):
        return self.game_state

    def game_state(self):
        #get currents state of game
        current_state = self.game_state

        if current_state == 0:
            self.main_menu()
        if current_state == 1:
            self.player_vs_player()

    def main_menu(self):
        pass

    def player_vs_player(self):
        pass

