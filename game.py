from fraction import Fraction

class Game(init_year, decision_dict):

    def __init__():
        self.init_year = init_year
        self.end_year = 2100
        self.decision_dict = decision_dict

        self.fraction = Fraction(init_year)
    


    def play(self):
        for year in range(self.init_year, self.end_year):
            pass


decision_dict_1 = {'powerplant':'yes'}
decision_dict_2 = {'powerplant':'no'}
init_year = 2019


game = Game(init_year, decision_dict_1)
game.play()