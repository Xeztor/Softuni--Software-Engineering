def sum_time(time_for_step):
    total_time = 0
    for i in time_for_step:
        if not i == 0:
            total_time += i
        else:
            total_time *= 0.8

    return total_time


nums = input().split()
nums = list(map(int, nums))

left = nums[:(len(nums) // 2)]
right = nums[-1:(len(nums) // 2):-1]

time_both = [sum_time(left), sum_time(right)]

if min(time_both) == time_both[0]:
    print(f"The winner is left with total time: {time_both[0]:.1f}")
elif min(time_both) == time_both[1]:
    print(f"The winner is right with total time: {time_both[1]:.1f}")
