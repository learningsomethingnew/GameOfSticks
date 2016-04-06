from random import randint

class AIPlayer():

    def __init__(self, a_num_of_sticks = 10):
        #init the unused dictionary
        self.init_dic = {n: list(range(1,4)) for n in range(1,11)}

        #init the winning dictionary that we will use to manage the
        self.win_dic = self.init_dic

        self.num_of_sticks = a_num_of_sticks

    """Gen a random int based on the len of the balls per stick"""
    def gen_random_int(self, a_max):
        return randint(1, a_max)

if __name__ == "__main__":
    f = AIPlayer()
    print(f.init_dic)