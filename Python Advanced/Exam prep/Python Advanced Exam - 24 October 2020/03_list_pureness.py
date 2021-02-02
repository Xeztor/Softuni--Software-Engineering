def best_list_pureness(nums, k):
    rotations = 0
    best_pureness = 0
    best_pureness_rot = 0

    for _ in range(k + 1):
        combination_pureness = 0

        for i in range(len(nums)):
            combination_pureness += nums[i] * i

        if combination_pureness > best_pureness:
            best_pureness = combination_pureness
            best_pureness_rot = rotations

        nums.insert(0, nums.pop())
        rotations += 1

    return f'Best pureness {best_pureness} after {best_pureness_rot} rotations'


