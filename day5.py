input_txt = open('day5.txt', mode='r')
lines = input_txt.readlines()

seeds = [int(x) for x in lines[0].split(":")[1].split()]
map_lines = lines[2:]
categories = ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", "humidity-to-location map"]

def convert_maps(input, map):
    output = []
    for item in input:
        appended = item
        for range in map:
            # [destination start, source range start, range length]
            if item >= range[1] and item <= range[1] + range[2]:
                appended = range[0] + item - range[1]
                break
        output.append(appended)
    return output
        

i = 0
maps = {}
for line in map_lines:
    if line == '\n':
        i += 1
    elif categories[i] in line:
        maps[categories[i]] = []
    else:
        maps[categories[i]].append([int(x) for x in line.split()])

result = seeds
for category in categories:
    result = convert_maps(result, maps[category])

print(result)
print(min(result))