s = input()

lower = sorted([letter for letter in s if letter.islower()])
upper = sorted([letter for letter in s if letter.isupper()])
digits = [int(symbol) for symbol in s if symbol.isdigit()]
even = sorted([str(digit) for digit in digits if digit % 2 == 0])
odd = sorted([str(digit) for digit in digits if not digit % 2 == 0])

print(''.join(lower) + ''.join(upper) + ''.join(odd) + ''.join(even))
