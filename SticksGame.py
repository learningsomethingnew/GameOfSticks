
class SticksGame():

    def __init__(self, a_max = 20):
        self.sticks_count = a_max
        self.player_state = 1
        self.game_run = True

    def game_logic(self):

        while self.game_run == True:
            self.print_current_game_status(self.sticks_count, self.player_state)
            if self.sticks_count > 1 and \
                            self.player_state == 1 or \
                            self.player_state == 2:

                user_response = user_response()


                self.sticks_count -= answer
                print(self.sticks_count)

                if pvp_state == 1:
                    pvp_state = 2
                elif pvp_state == 2:
                    pvp_state = 1

            elif self.sticks_count == 1 and pvp_state == 1:
                winner(pvp_state)
                game_run = False
            elif self.sticks_count == 1 and pvp_state == 2:
                winner(pvp_state)
            elif self.sticks_count == 0 and pvp_state == 1:
                pvp_state = 2
                winner(pvp_state)
            elif self.sticks_count == 0 and pvp_state == 2:
                pvp_state = 1
                winner(pvp_state)
            else:
                pass

    def print_current_game_status(self, a_stick_count, a_player_state):
        print("There are %i sticks on the table" % a_stick_count)
        print("Player %i: How many do you take? 1, 2, or 3?" % a_player_state)

    """Decrement stick count"""
    def dec_sticks(self, a_num):
        self.sticks_count -= a_num

    def user_input(self):

