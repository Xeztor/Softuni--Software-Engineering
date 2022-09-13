def return_set_from_range(range_str):
    range_list = list(map(int, range_str.split(',')))
    return set(range(min(range_list), max(range_list) + 1))


lines = int(input())

longest = {'len': 0, 'intersection_set': set()}

for _ in range(lines):
    ranges = input().split('-')
    intersection = return_set_from_range(ranges[0]).intersection(return_set_from_range(ranges[1]))
    if len(intersection) > longest['len']:
        longest['len'] = len(intersection)
        longest['intersection_set'] = intersection

print(f"Longest intersection is", sorted(list(longest['intersection_set'])), f"with length {longest['len']}")


