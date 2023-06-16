class Game:
    def __init__(self, player_A, player_B):
        self.__player_A = player_A
        self.__player_B = player_B

        '''
        List of moves in the form:
        [
            [ move_A, move_B],
            ...
        ]
        '''
        self.__moves = []

    def play(self):
        move_A = self.__player_A.move(self)
        move_B = self.__player_B.move(self)

        if move_A == False and move_B == False:
            # Both defect - result is 2/2
            pass
        elif move_A == False and move_B == True:
            # A defects, B cooperates - result is 10/1
            pass
        elif move_A == True and move_B == False:
            # A cooperates, B defects - result is 1/10
            pass
        elif move_A == True and move_B == True:
            # Both cooperate - result is 3/3
            pass