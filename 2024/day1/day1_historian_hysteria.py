# https://adventofcode.com/2024/day/1

import os
from collections import Counter


def get_list_pairs() -> list[tuple[int, int]]:
    pairs = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input')

    with open(input_path) as input_file:
        for line in input_file:
            pair = line.split()
            pairs.append(tuple(map(int, pair)))
    return pairs


def separate_pairs(pairs: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    return list(zip(*pairs))


def calculate_total_distance(l1: list[int], l2: list[int]) -> int:
    distance = 0
    for n1, n2 in zip(sorted(l1), sorted(l2)):
        distance += abs(n1 - n2)
    return distance


# part1
pairs = get_list_pairs()
l1, l2 = separate_pairs(pairs)
distance = calculate_total_distance(l1, l2)
print(f"distance: {distance}")  # 3574690


def get_counter(l: list[int]) -> Counter[int]:
    return Counter(l)


def calculate_similarity(l: list[int], c: Counter[int]) -> int:
    similarity = 0
    for n in l:
        similarity += n * c.get(n, 0)
    return similarity


# part2
c = get_counter(l2)
similarity = calculate_similarity(l1, c)
print(f"similarity: {similarity}")  # 22565391
