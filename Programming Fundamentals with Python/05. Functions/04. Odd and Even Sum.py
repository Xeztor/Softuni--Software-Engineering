def odd_even_sum(x):
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(str(x)):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return [odd_sum, even_sum]


number = int(input())

result_odd_even_sum = odd_even_sum(number)
print(f"Odd sum = {result_odd_even_sum[0]}, Even sum = {result_odd_even_sum[1]}")
