import random

class Participant:
    '''
    POSSIBLE STRATEGIES
   * Always cooperate
   * Always defect
   * Tit for tat
   * Random
   * Tit For Two Tats: Cooperates on the first move, and defects only when the opponent defects two times in a row.
   * Firm But Fair: Cooperates on the first move, and continues to cooperate until the other side defects. Then, it will try to cooperate again after (D|D).
   * Generous Tit for Tat: Same as Tit For Tat, except that it cooperates with a 10% probability when the opponent defects.
   * Soft Majority: Cooperates on the first move, and cooperates as long as the number of times the opponent has cooperated is greater than or equal to the number of times it has defected, else it defects.
   * Hard Tit for Tat: Cooperates on the first move, and defects if the opponent has defected on any of the previous 3 moves, else cooperates.
   * Two Tits for Tat: Same as Tit For Tat except that it defects 2x whenever the opponent defects.
    Gradual: Cooperates on the first move, and cooperates as long as the opponent cooperates. After the first defection of the other player, it defects 1x and cooperates 2x. After the Nth defection it reacts with N consecutive defections and then calms down its opponent with two cooperations, in order to reset them if they are also forgiving.
   * Soft Grudger: Cooperates, until the opponent defects, then punishes them with D, D, D, D, C, C.
   * Grim trigger: Cooperates, until the opponent defects, and thereafter always defects.
   * Suspicious Tit for Tat: Same as Tit For Tat, except that it defects on the first move.
    Hard Majority: Defects on the first move, and defects if the number of defections of the opponent is greater than or equal to the number of times it has cooperated, else cooperates.
   * Reverse Tit for Tat: It does the reverse of TFT. It defects on the first move, then plays the reverse of the opponent’s last move.
    Prober
    Handshake: Defects on the first move and cooperates on the second move. If the opponent plays the same moves, it always cooperates. Otherwise, it always defects.
    Naive Prober: Like Tit for Tat, but occasionally defects with a small probability. The probing, in this case, is to occasionally test for an overly-forgiving strategy.
    Remorseful Prober: Like Naive Prober, but it tries to break the series of mutual defections after defecting. In effect, probing for forgiveness.
    Adaptive: Starts with C, C, C, C, C, C, D, D, D, D, D and then takes choices which have given the best average score re-calculated after every move.
    Pavlov: Plays Tit For Tat in the first six moves and identifies the opponent by means of a rule-based mechanism. The strategies of the opponent are categorized into four groups: Tit For Tat, Always Defect, Suspicious Tit For Tat, and Random. If the other player doesn’t start defecting, it is identified to be cooperative and will behave as Tit For Tat. If the other player defects more than four times in six consecutive moves, it is identified as an Always Defect type and will always defect. If the opponent just defects three times in six moves, it is identified as Suspicious Tit For Tat type and will adopt Tit For Two Tats in order to recover mutual cooperation. Any strategy that does not belong to the former three categories will be identified as a random type. In this situation, Pavlov will play Always Defect. In order to deal with the situations in which the opponents may change their actions, the average payoff is computed every six rounds. If it is lower than a threshold, the process of opponent identification may restart.
    Fortress3: Like Handshake, it tries to recognize kin members by playing D, D, C. If the opponent plays the same sequence of D, D, C, it cooperates until the opponent defects. Otherwise, it defects until the opponent defects on continuous two moves, and then it cooperates on the following move.
    Fortress4: Same as Fortress3 except that it plays D, D, D, C in recognizing kin members. If the opponent plays the same sequence of D, D, D, C, it cooperates until the opponent defects. Otherwise, it defects until the opponent defects on continuous three moves, and then it cooperates on the following move.
    Collective strategy: Plays C and D in the first and second move. If the opponent has played the same moves, plays Tit For Tat. Otherwise, plays Always Defect.
    Southampton Group strategies: A group of strategies are designed to recognize each other through a predetermined sequence of 5–10 moves at the start. Once two of these strategies recognize each other, they will act as a ‘master’ or ‘slave’ role — a master will always defect while a slave will always cooperate in order for the master to win the maximum points. If the opponent is recognized as not being a SGS, it will immediately defect to minimize the score of the opponent.
    '''

    '''
    List of moves in the form:
    [
        [move_A, move_B],
        ...
    ]
    '''
    def __init__(self):
        self.strategies = [
            self.random,
            self.always_cooperate,
            self.always_defect,
            self.tit_for_tat,
            self.tit_for_2_tats,
            self.firm_but_fair,
            self.generous_tit_for_tat,
            self.soft_majority,
            self.hard_tit_for_tat,
            self.two_tits_for_tat,
            self.grim_trigger,
            self.suspicious_tit_for_tat,
            self.reverse_tit_for_tat,
            self.soft_grudger,
            self.hard_marjority
        ]
        self.__temp_vars = {}

    def random(self, moves=None):
        return random.random() < 0.5

    def always_cooperate(self, moves=None):
        return True

    def always_defect(self, moves=None):
        return False

    def tit_for_tat(self, moves):
        # Start by cooperating, then copy whatever the other player did last move.
        if len(moves) == 0:
            return True
        else:
            return moves[-1][1]

    def tit_for_2_tats(self, moves):
        # Cooperates on the first move, and defects only when the opponent defects two times in a row.
        if len(moves) < 2:
            return True
        else:
            if moves[-1][1] == moves[-2][1] == False:
                return False
            else:
                return True

    def firm_but_fair(self, moves):
        # Cooperates on the first move, and continues to cooperate until the other side defects. Then, it will try to cooperate again after (D|D).
        if len(moves) == 0:
            return True
        else:
            if moves[-1][1] == False:
                return False
            else:
                return True

    def generous_tit_for_tat(self, moves):
        # Same as Tit For Tat, except that it cooperates with a 10% probability when the opponent defects.
        if len(moves) == 0:
            return True
        else:
            if moves[-1][1] == False:
                return random.random() < 0.1
            else:
                return True

    def soft_majority(self, moves):
        # Cooperates on the first move, and cooperates as long as the number of times the opponent has cooperated is greater than or equal to the number of times it has defected, else it defects.
        if len(moves) == 0:
            return True

        num_times_opponent_cooperated = 0
        num_times_opponent_defected = 0
        for move in moves:
            if move[1] == True:
                num_times_opponent_cooperated += 1
            else:
                num_times_opponent_defected += 1

        if num_times_opponent_cooperated >= num_times_opponent_defected:
            return True
        else:
            return False

    def hard_tit_for_tat(self, moves):
        # Cooperates on the first move, and defects if the opponent has defected on any of the previous 3 moves, else cooperates.
        if len(moves) < 3:
            return True
        if moves[-1][1] == moves[-2][1] == moves[-3][1] == False:
            return False
        else:
            return True

    def two_tits_for_tat(self, moves):
        # Same as Tit For Tat except that it defects 2x whenever the opponent defects.
        if len(moves) == 0:
            return True
        elif len(moves) == 1:
            if moves[-1][1] == False:
                return False
            else:
                return True
        else:
            if moves[-1][1] or moves[-2][1] == False:
                # We want to defect on the next 2 moves
                return False
            else:
                return True

    def grim_trigger(self, moves):
        # Cooperates, until the opponent defects, and thereafter always defects.
        # Use the temp variable opponent_has_defected to store if the opponent defected,
        # rather than iterating through all of the moves again
        if len(self.__temp_vars) == 0:
            if len(moves) == 0:
                return True
            # Check did the opponent defect in the last move
            elif moves[-1][1] == False:
                self.__temp_vars['opponent_has_defected'] = True
                return False
            else:
                return True
        elif self.__temp_vars['opponent_has_defected'] == True:
            return False
        else:
            raise Exception

    def suspicious_tit_for_tat(self, moves):
        # Same as Tit For Tat, except that it defects on the first move.
        # Start by cooperating, then copy whatever the other player did last move.
        if len(moves) == 0:
            return False
        else:
            return moves[-1][1]

    def reverse_tit_for_tat(self, moves):
        # It does the reverse of TFT. It defects on the first move, then plays the reverse of the opponent’s last move.
        # Start by cooperating, then copy whatever the other player did last move.
        if len(moves) == 0:
            return False
        else:
            return not moves[-1][1]

    def soft_grudger(self, moves):
        # Cooperates, until the opponent defects, then punishes them with D, D, D, D, C, C.
        # Lets call the DDDDCC the move set
        move_set = [False, False, False, False, True, True]
        # Is the move set already in play? - if so, ignore the opponents last play
        if len(self.__temp_vars) > 0:
            # Make the move
            move = move_set[self.__temp_vars['move_index']]
            # AFTER each move, increment and see if the cycle is over
            if self.__temp_vars['move_index'] == (len(move_set) - 1):
                self.__temp_vars = {}
            else:
                self.__temp_vars['move_index'] += 1

            return move
        else:
            if len(moves) == 0:
                return True
            # Did the opponent defect on the last move?
            if moves[-1][1] == False:
                self.__temp_vars['move_index'] = 1
                return move_set[0]
            else:
                # Otherwise, cooperate
                return True

    def hard_marjority(self, moves):
        # Defects on the first move,
        # and defects if the number of defections of the opponent is greater than or equal to the number of times it has cooperated,
        # else cooperates.
        if len(moves) == 0:
            return False
        else:
            # Update the move totals
            if len(self.__temp_vars) == 0:
                self.__temp_vars[True] = 0
                self.__temp_vars[False] = 0

            self.__temp_vars[moves[-1][1]] += 1

            # Now decide on the move
            if self.__temp_vars[False] >= self.__temp_vars[True]:
                return False
            else:
                return True

