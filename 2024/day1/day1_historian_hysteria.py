# https://adventofcode.com/2024/day/1

from collections import Counter

def get_list_pairs():
    pairs = []
    with open('input') as input_file:
        for line in input_file:   
            pair = line.split()
            pairs.append(tuple(map(int, pair)))
    return pairs

def separate_pairs(pairs):
    return list(zip(*pairs))

def calculate_total_distance(l1, l2):
    distance = 0
    for n1, n2 in zip(sorted(l1), sorted(l2)):
        distance += abs(n1-n2)
    return distance

pairs = get_list_pairs()
l1, l2 = separate_pairs(pairs)
distance = calculate_total_distance(l1, l2)

# part1
print(f'distance: {distance}') # 3574690


def get_counter(l):
    return Counter(l)
    
def calculate_similarity(l, c):
    similarity = 0
    for n in l:
        similarity += (n * c.get(n, 0))
    return similarity

c = get_counter(l2)
similarity = calculate_similarity(l1, c)

# part2
print(f'similarity: {similarity}')
