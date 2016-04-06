
class SticksGame():

    def __init__(self, a_max = 20):
        self.sticks_count = a_max
        self.player_state = 1
        self.game_run = True

    def game_logic(self):

        while self.game_run == True:
            self.print_current_game_status(self.sticks_count, self.player_state)
            if self.sticks_count > 1 and self.player_state in {1,2}:

                user_response = self.test_user_input()

                self.dec_sticks(user_response)
                print(self.sticks_count)

                if self.player_state == 1:
                    self.player_state = 2
                elif self.player_state == 2:
                    self.player_state = 1

            elif self.sticks_count == 1 and self.player_state == 1:
                self.game_run = self.winner(self.player_state)
            elif self.sticks_count == 1 and self.player_state == 2:
                self.game_run = self.winner(self.player_state)
            elif self.sticks_count == 0 and self.player_state == 1:
                self.player_state = 2
                self.game_run = self.winner(self.player_state)
            elif self.sticks_count == 0 and self.player_state == 2:
                self.player_state = 1
                self.game_run = self.winner(self.player_state)
            else:
                raise UnknownGameState("A game state was not built in")

    def print_current_game_status(self, a_stick_count, a_player_state):
        print("There are %i sticks on the table" % a_stick_count)
        print("Player %i: How many do you take? 1, 2, or 3?" % a_player_state)

    """Decrement stick count"""
    def dec_sticks(self, a_num):
        self.sticks_count -= a_num

    def test_user_input(self):
        valid = True
        while (True):
            a_response = input(">>> ")
            if a_response not in {1, 2, 3}:
                return int(a_response)
            else:
                print("Please enter a valid response")

    def winner(self, a_winning_player):
        print("%s Wins!" %self.player_state)
        return False

class UnknownGameState(Exception):
    pass

if __name__ == '__main__':
    f = SticksGame()
    f.game_logic()