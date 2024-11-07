cubes = {"red": 12, "green": 13, "blue": 14}

input_txt = open('day2.txt', mode='r')
lines = input_txt.readlines()

result = 0

def valid(ball_info):
    for key, val in ball_info.items():
        if cubes[key] < int(val):
            return False
    return True

for line in lines:
    game_info = line.split(":")
    game_num = int(game_info[0].split(" ")[1])
    check_round = game_info[1].split(";")

    is_valid = []
    for round in check_round:
        balls_shown = round.split(",")
        ball_info = {}
        for balls in balls_shown:
            stripped = balls.strip()
            num, color = stripped.split(" ")
            ball_info[color] = num
        is_valid.append(valid(ball_info))
    if False not in is_valid:
        result += game_num

print(result)

## Part Two
