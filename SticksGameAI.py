from AIPlayer import AIPlayer
class SticksGameAI():

    def __init__(self, a_max = 10):
        self.sticks_count = a_max
        self.player_state = 1
        self.game_run = True
        self.f = AIPlayer()


    def game_logic(self):

        while self.game_run == True:

            #player turn
            if self.sticks_count > 1 and self.player_state == 1:

                self.print_current_game_status()
                user_response = self.test_user_input()
                self.dec_sticks(user_response)
                self.player_state = 2

            #AI Turn
            elif self.sticks_count > 1 and self.player_state == 2:
                #setting AI's stick count
                print("There are {} sticks on the table".format(self.sticks_count))
                self.f.set_cur_sticks(self.sticks_count)
                self.dec_sticks(self.f.get_guess())
                self.player_state = 1

            elif self.sticks_count == 1 and self.player_state == 2:
                self.game_run = self.f.ai_lost()
            elif self.sticks_count == 1 and self.player_state == 1:
                self.game_run = self.f.ai_won()
            elif self.sticks_count == 0 and self.player_state == 1:
                self.game_run = self.f.ai_lost()
            elif self.sticks_count == 0 and self.player_state == 2:
                self.game_run = self.f.ai_won()
            else:
                raise UnknownGameState("A player entered too many")

        #storing the smart AI
        self.f.store_win_dict()

    def print_current_game_status(self):
        print("There are {} sticks on the table".format(self.sticks_count))
        print("Player {}: How many do you take? 1, 2, or 3?".format(self.player_state))

    """Decrement stick count"""
    def dec_sticks(self, a_num):
        self.sticks_count -= a_num

    def test_user_input(self):
        valid = True
        while (True):
            a_response = int(input(">>> "))
            if a_response in {1, 2, 3}:
                return int(a_response)
            else:
                print("Please enter a valid response")

    def winner(self, a_winning_player):
        print("%s Wins!" %self.player_state)
        return False

class UnknownGameState(Exception):
    pass

if __name__ == '__main__':
    f = SticksGameAI()
    f.game_logic()