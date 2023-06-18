from Opponent import Opponent


class Game:
    num_rounds = 8
    def __init__(self, player):
        self.__player = player
        self.__opponent = Opponent()

        '''
        List of moves in the form:
        [
            [ move_A, move_B],
            ...
        ]
        '''
        self.__moves = []

    def play(self):
        for i in range(0, Game.num_rounds):
            move_A = self.__player.make_move(self.__moves)
            move_B = self.__opponent.make_move()

            if move_A == False and move_B == False:
                # Both defect - result is 2/2
                self.__player.add_points(2)
                self.__opponent.add_points(2)
            elif move_A == False and move_B == True:
                # A defects, B cooperates - result is 10/1
                self.__player.add_points(10)
                self.__opponent.add_points(1)
            elif move_A == True and move_B == False:
                # A cooperates, B defects - result is 1/10
                self.__player.add_points(10)
                self.__opponent.add_points(1)
            elif move_A == True and move_B == True:
                # Both cooperate - result is 3/3
                self.__player.add_points(3)
                self.__opponent.add_points(3)
            else:
                raise Exception

            self.__moves.append([move_A, move_B])



