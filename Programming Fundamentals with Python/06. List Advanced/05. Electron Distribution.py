def fill_shields(electrons):
    shields = []
    while 2*(len(shields) + 1)**2 <= electrons:
        electrons -= 2*(len(shields) + 1)**2
        shields.append(2*(len(shields) + 1)**2)
    else:
        shields.append(electrons)
    return shields


electrons_given = int(input())

shields_filled = fill_shields(electrons_given)
print(shields_filled)
