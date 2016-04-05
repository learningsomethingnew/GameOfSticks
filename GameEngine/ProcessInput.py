####################################################################
#
####################################################################

class ProcessInput():

    def __init__(self):
        self.user_quit_list = ['Quit', 'quit', 'q', 'Q']

    def prompt_user(self):
        return self.test_response(input(">>> "))

    def test_response(self, a_input):
        #Tests against each version of quit to see
        # if the user wants out
        for word in self.user_quit_list:
            if a_input == word:
                return False
        else:
            return a_input