import random
import math

class player:
    def __init__(self,letter):
        #letter is x or o
        self.letter=letter

    #we want all players to get their next move given a game 
    def get_move(self,game):
        pass

class RandimComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)      

        def get_move(self,game):
            pass
class HummanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
         pass     

