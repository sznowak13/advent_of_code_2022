"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock
Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each
simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected:
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round
instead ends in a draw.
"""
ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

win_map = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}

lose_map = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

symbol_to_number_map_part1 = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}


def get_input():
    with open('inputs/day2.txt') as f:
        processed_inpt = [s.split() for s in f.read().split('\n')]
    return processed_inpt


def part1():
    """
    Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they
    say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper,
    and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

    The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
    Winning every time would be suspicious, so the responses must have been carefully chosen.

    The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores
    for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and
    3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you
    won).

    Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get
    if you were to follow the strategy guide.

    For example, suppose you were given the following strategy guide:

    A Y
    B X
    C Z

    This strategy guide predicts and recommends the following:

        In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for
        you with a score of 8 (2 because you chose Paper + 6 because you won).
        In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss
        for you with a score of 1 (1 + 0).
        The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

    In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
    """
    inpt = get_input()

    sum_pts = 0
    for turn in inpt:
        pts = 0
        enemy_move = symbol_to_number_map_part1[turn[0]]
        player_move = symbol_to_number_map_part1[turn[1]]
        if win_map[player_move] == enemy_move:
            pts += WIN + player_move
        elif player_move == enemy_move:
            pts += DRAW + player_move
        else:
            pts += LOSE + player_move
        sum_pts += pts

    return sum_pts


def part2():
    """
    --- Part Two ---

    By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

    To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

    In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

    """
    inpt = get_input()

    sum_pts = 0
    for turn in inpt:
        pts = 0
        enemy_move = symbol_to_number_map_part1[turn[0]]
        scenario = turn[1]
        if scenario == "X":  # lose
            player_move = win_map[enemy_move]
            pts = LOSE + player_move
        elif scenario == "Z":  # win
            player_move = lose_map[enemy_move]
            pts = WIN + player_move
        else:  # 'Y' otherwise - draw
            player_move = enemy_move
            pts += DRAW + player_move
        sum_pts += pts

    return sum_pts


if __name__ == '__main__':
    print(part1())
    print(part2())
