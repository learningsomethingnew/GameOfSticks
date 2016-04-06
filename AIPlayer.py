from random import randint
from SupportClasses.FileActions import FileActions
from os import path

class AIPlayer():

    def __init__(self, a_num_of_sticks_in_game = 10):
        #init the unused dictionary
        self.init_dic = {n: list(range(1,4)) for n in range(1,a_num_of_sticks_in_game)}

        #init the winning dictionary that we will use to manage

        self.temp_dic = {}

        #current sticks in play
        self.cur_sticks_in_game = a_num_of_sticks_in_game

        self.f = FileActions()

        self.win_dic = self.test_file_exists("win_dic")

    """Gen a random int based on the len of the balls per hat"""
    def get_random_int(self, a_max):
        return randint(1, a_max)

    """Returns the guess as int"""
    def get_guess(self):
        list_of_key = self.win_dic[self.cur_sticks_in_game]
        print("The current sticks in game is %i" %self.cur_sticks_in_game)
        guess = self.get_random_int(len(list_of_key))
        print(guess)
        guess = list_of_key[guess-1]
        print("The guess is %i" %guess)
        self.reserve_hat_number(guess)
        return guess

    """gets the current game stick count"""
    def get_cur_sticks(self):
        return self.cur_sticks_in_game

    """sets the current game stick count"""
    def set_cur_sticks(self, a_num):
        self.cur_sticks_in_game = a_num

    """holds the guesses that the AI placed.
    If a win condition, it will add the guess
    to the correct hat in the win_dict"""
    def reserve_hat_number(self, a_guess_num):
        self.temp_dic[self.cur_sticks_in_game] = a_guess_num
        print("AI guess = {}".format(a_guess_num))
        print("Reserving Hat {} and Ball {}"
              .format(self.cur_sticks_in_game, a_guess_num))


    def ai_won(self):
        for key in self.temp_dic:
            self.append_into_win_dict(key, self.temp_dic[key])
            print("Inserting Hat {} and Ball {}"
                  .format(key, self.temp_dic[key]))
            print("The AI Win_Dict is ")
            print(self.win_dic)
        self.sort_dict_values()

    def ai_lost(self):
        print("AI Has Lost")
        for key in self.temp_dic:
            print("The WIN Dic is comprised of")
            print(self.win_dic)
            self.remove_from_win_dict(key, self.temp_dic[key])
        print("Clearing temp dic")
        print(self.temp_dic)
        self.temp_dic.clear()

    def store_win_dict(self):
        self.f.save_to_pickle_file(self.win_dic, "win_dic")

    def retrieve_win_dict(self):
        return self.f.retrieve_pickled_file("win_dic")

    def append_into_win_dict(self, a_key, a_value):
        self.win_dic[a_key].append(a_value)

    def remove_from_win_dict(self, a_key, a_value):
        if len(self.win_dic[a_key]) > 1:
            print("Removing {} {} from win_dict".format(a_key, a_value))
            self.win_dic[a_key].remove(a_value)

    def sort_dict_values(self):
        for key in self.win_dic:
            self.win_dic[key].sort()
        print("list sorted")

    def test_file_exists(self, a_file_name):
        if path.isfile(a_file_name+".p"):
            print("file exists. opening")
            print()
            return self.retrieve_win_dict()
        else:

            return self.init_dic


if __name__ == "__main__":

    f = AIPlayer()
    f.set_cur_sticks(9)
    guess = f.get_guess()
    f.set_cur_sticks(4)
    guess = f.get_guess()
    f.set_cur_sticks(2)
    guess = f.get_guess()
    f.ai_won()
    print("+++++++++++++++++++++++++++++++++++")
    f.set_cur_sticks(10)
    guess = f.get_guess()
    f.set_cur_sticks(5)
    guess = f.get_guess()
    f.set_cur_sticks(3)
    guess = f.get_guess()
    f.ai_won()
    print("+++++++++++++++++++++++++++++++++++")
    f = AIPlayer()
    f.set_cur_sticks(8)
    guess = f.get_guess()
    f.set_cur_sticks(7)
    guess = f.get_guess()
    f.set_cur_sticks(3)
    guess = f.get_guess()
    f.ai_lost()
    print("+++++++++++++++++++++++++++++++++++")
    f.set_cur_sticks(10)
    guess = f.get_guess()
    f.set_cur_sticks(4)
    guess = f.get_guess()
    f.set_cur_sticks(1)
    guess = f.get_guess()
    f.ai_won()
    print("+++++++++++++++++++++++++++++++++++")
    f.store_win_dict()
    print("The file contains ")
    print(f.win_dic)


