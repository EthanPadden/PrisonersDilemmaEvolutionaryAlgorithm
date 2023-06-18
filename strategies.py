'''
POSSIBLE STRATEGIES
Always cooperate
Always defect
Tit for tat
Tit For Two Tats: Cooperates on the first move, and defects only when the opponent defects two times in a row.
Firm But Fair: Cooperates on the first move, and continues to cooperate until the other side defects. Then, it will try to cooperate again after (D|D).
Generous Tit for Tat: Same as Tit For Tat, except that it cooperates with a 10% probability when the opponent defects.
Soft Majority: Cooperates on the first move, and cooperates as long as the number of times the opponent has cooperated is greater than or equal to the number of times it has defected, else it defects.
Hard Tit for Tat: Cooperates on the first move, and defects if the opponent has defected on any of the previous 3 moves, else cooperates.
Two Tits for Tat: Same as Tit For Tat except that it defects 2x whenever the opponent defects.
Gradual: Cooperates on the first move, and cooperates as long as the opponent cooperates. After the first defection of the other player, it defects 1x and cooperates 2x. After the Nth defection it reacts with N consecutive defections and then calms down its opponent with two cooperations, in order to reset them if they are also forgiving.
Soft Grudger: Cooperates, until the opponent defects, then punishes them with D, D, D, D, C, C.
Grim trigger: Cooperates, until the opponent defects, and thereafter always defects.
Suspicious Tit for Tat: Same as Tit For Tat, except that it defects on the first move.
Hard Majority: Defects on the first move, and defects if the number of defections of the opponent is greater than or equal to the number of times it has cooperated, else cooperates.
Reverse Tit for Tat: It does the reverse of TFT. It defects on the first move, then plays the reverse of the opponent’s last move.
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

def always_cooperate(moves=None):
    return True

def always_defect(moves=None):
    return False

def tit_for_tat(moves):
    # Start by cooperating, then copy whatever the other player did last move.
    if len(moves) == 0:
        return True
    else:
        return moves[-1]

def tit_for_2_tats(moves):
    # Cooperates on the first move, and defects only when the opponent defects two times in a row.
    if len(moves) < 2:
        return True
    else:
        if moves[-1][1] == moves[-2][1] == False:
            return False
        else:
            return True

def firm_but_fair(moves):
    # Cooperates on the first move, and continues to cooperate until the other side defects. Then, it will try to cooperate again after (D|D).
    if len(moves) == 0:
        return True
    else:
        if moves[-1][1] == False:
            return False
        else:
            return True


strategies = [
    always_cooperate,
    always_defect,
    tit_for_tat,
    tit_for_2_tats,
    firm_but_fair
]