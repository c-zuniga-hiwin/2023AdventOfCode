input_txt = open('day4.txt', mode='r')
lines = input_txt.readlines()

# Part One

# result = 0

# for line in lines:
#     game_info = line.split(":")
#     winning_nums = game_info[1].split("|")[0].split()
#     card_nums = game_info[1].split("|")[1].split()
#     matches = list(filter(lambda x: x in winning_nums, card_nums))
#     if matches:
#         result += 2**(len(matches)-1)
# print(result)

# Part Two
# Algorithm: Memoization

cards = {}
for line in lines:
    game_info = line.split(":")
    game_num = int(game_info[0].split()[1])
    winning_nums = game_info[1].split("|")[0].split()
    card_nums = game_info[1].split("|")[1].split()
    cards[game_num] = {'Winning Nums': [], 'Card Nums': []}
    cards[game_num]['Winning Nums'] = winning_nums
    cards[game_num]['Card Nums'] = card_nums

num_winnings = {}
def calculate_winnings(num):
    if num in num_winnings:
        return num_winnings[num]
    matches = list(filter(lambda x: x in cards[num]['Winning Nums'], cards[num]['Card Nums']))
    result = min(len(cards.keys()) - num, len(matches))
    num_winnings[num] = result
    return result

card_worths = {}
def calculate_worth(card_num):
    if card_num in card_worths:
        return card_worths[card_num]
    winnings = calculate_winnings(card_num)
    amount = 1
    for i in range(card_num+1, card_num+winnings+1):
        amount += calculate_worth(i)
    return amount

result = 0
for game in range(len(cards.keys()), 0, -1):
    result += calculate_worth(game)

print(result)