# Algorithm:
# First Scan:
# Find starting x, y of number strings. Save in a dictionary
# Second Scan:
# Search for symbols. If we find one, check radially and see if any numbers in range. If they are, add to result

# Another idea (using this):
# scan for symbols. If we find one, check directly above and below. Scan left and right. Then, if not directly above, check diagonals and scan left/right.
# note: need to keep track of found numbers

# table = [[cols]rows]
input_txt = open('day3.txt', mode='r')
lines = input_txt.readlines()
table = [[char for char in line.rstrip()] for line in lines]
# found = [[0 for _ in range(len(table[0]))] for __ in range(len(table))]

# def scan_left(x, y):
#     result = ""
#     if found[y][x]:
#         return ""
#     for col in range(x, -1, -1):
#         found[y][col] = 1
#         if table[y][col].isnumeric():
#             result = table[y][col] + result
#         else:
#             return result
#     return result

# def scan_right(x, y):
#     result = ""
#     if found[y][x]:
#         return ""
#     for col in range(x, len(table[0])):
#         found[y][col] = 1
#         if table[y][col].isnumeric():
#             result += table[y][col]
#         else:
#             return result
#     return result

# def scan_left_right(x, y):
#     if not found[y][x]:
#         found[y][x] = 1
#         return scan_left(x-1, y) + table[y][x] + scan_right(x+1, y)
#     return "0"

result = 0

## Part 1
# for y in range(len(table)):
#     for x in range(len(table[y])):
#         # found symbol
#         if not table[y][x].isnumeric() and table[y][x] != '.':
#             # check top
#             if y > 0 and table[y-1][x].isnumeric():
#                 added = int(scan_left_right(x, y-1))
#                 # print(added)
#                 result += added
#             # check top left/right diagonals
#             else:
#                 if y > 0 and x > 0 and table[y-1][x-1].isnumeric():
#                     added = int(scan_left(x-1, y-1))
#                     # print(added)
#                     result += added
#                 if y > 0 and x < len(table[0]) - 1 and table[y-1][x+1].isnumeric():
#                     added = int(scan_right(x+1, y-1))
#                     # print(added)
#                     result += added
#             # check bottom
#             if y < len(table) - 1 and table[y+1][x].isnumeric():
#                 added = int(scan_left_right(x, y+1))
#                 # print(added)
#                 result += added
#             else:
#                 if y < len(table) - 1 and x > 0 and table[y+1][x-1].isnumeric():
#                     added = int(scan_left(x-1, y+1))
#                     # print(added)
#                     result += added
#                 if y < len(table) - 1 and x < len(table[0]) - 1 and table[y+1][x+1].isnumeric():
#                     added = int(scan_right(x+1, y+1))
#                     # print(added)
#                     result += added
#             # scan left
#             if x > 0 and table[y][x-1].isnumeric():
#                     added = int(scan_left(x-1, y))
#                     # print(added)
#                     result += added
#             # scan right
#             if x < len(table[0]) - 1 and table[y][x+1].isnumeric():
#                     added = int(scan_right(x+1, y))
#                     # print(added)
#                     result += added

## Part 2

def scan_left(x, y):
    result = ""
    for col in range(x, -1, -1):
        if table[y][col].isnumeric():
            result = table[y][col] + result
        else:
            return result
    return result

def scan_right(x, y):
    result = ""
    for col in range(x, len(table[0])):
        if table[y][col].isnumeric():
            result += table[y][col]
        else:
            return result
    return result

def scan_left_right(x, y):
    return scan_left(x-1, y) + table[y][x] + scan_right(x+1, y)

for y in range(len(table)):
    for x in range(len(table[y])):
        # found gear
        if table[y][x] == '*':
            found_nums = []
            # check top
            if y > 0 and table[y-1][x].isnumeric():
                added = int(scan_left_right(x, y-1))
                found_nums.append(added)
            # check top left/right diagonals
            else:
                if y > 0 and x > 0 and table[y-1][x-1].isnumeric():
                    added = int(scan_left(x-1, y-1))
                    found_nums.append(added)
                if y > 0 and x < len(table[0]) - 1 and table[y-1][x+1].isnumeric():
                    added = int(scan_right(x+1, y-1))
                    found_nums.append(added)
            # check bottom
            if y < len(table) - 1 and table[y+1][x].isnumeric():
                added = int(scan_left_right(x, y+1))
                found_nums.append(added)
            else:
                if y < len(table) - 1 and x > 0 and table[y+1][x-1].isnumeric():
                    added = int(scan_left(x-1, y+1))
                    found_nums.append(added)
                if y < len(table) - 1 and x < len(table[0]) - 1 and table[y+1][x+1].isnumeric():
                    added = int(scan_right(x+1, y+1))
                    found_nums.append(added)
            # scan left
            if x > 0 and table[y][x-1].isnumeric():
                    added = int(scan_left(x-1, y))
                    found_nums.append(added)
            # scan right
            if x < len(table[0]) - 1 and table[y][x+1].isnumeric():
                    added = int(scan_right(x+1, y))
                    found_nums.append(added)
            if len(found_nums) == 2:
                result += found_nums[0]*found_nums[1]
print(result)