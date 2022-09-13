def pos_neg_zero(nums):
    if 0 in nums:
        return "zero"
    elif len([i for i in nums if i < 0]) % 2 == 0:
        return "positive"
    else:
        return "negative"


nums = [int(input()) for _ in range(3)]

print(pos_neg_zero(nums))