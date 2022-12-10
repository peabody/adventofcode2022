ROCK_SCORE=1
PAPER_SCORE=2
SCISSORS_SCORE=3

WIN_SCORE=6
DRAW_SCORE=3
LOSE_SCORE=0

DRAWS=("A X", "B Y", "C Z")
WINS=("A Y", "B Z", "C X")

# x is 'must lose'
# y is 'must draw'
# z is 'must win'

# translate A X = A Z
# translate B X = B X
# translate C X = C Y

# translate A Y = A X
# translate B Y = B Y
# translate C Y = C Z

# translate A Z = A Y
# translate B Z = B Z
# translate C Z = C X

t = {
        "A X" : "A Z",
        "B X" : "B X",
        "C X" : "C Y",
        "A Y" : "A X",
        "B Y" : "B Y",
        "C Y" : "C Z",
        "A Z" : "A Y",
        "B Z" : "B Z",
        "C Z" : "C X"

}

with open("p2.txt") as data:
    total_score = 0
    for line in data:
        line = line.strip()
        line = t[line]
        total_score += int("X" in line)*1
        total_score += int("Y" in line)*2
        total_score += int("Z" in line)*3
        total_score += int(line in WINS)*6
        total_score += int(line in DRAWS)*3
    print(total_score)


