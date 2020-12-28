events = input().split("|")

energy = 100
coins = 100
possible_events = ["rest", "order"]
flag = True

for i in events:
    crnt_event, value = i.split("-")
    value = int(value)
    if crnt_event in possible_events:
        if crnt_event == "rest" and energy + value > 100:
            print(f"You gained 0 energy.")
            print(f"Current energy: {energy}.")
        elif crnt_event == "rest" and energy + value <= 100:
            energy += value
            print(f"You gained {value} energy.")
            print(f"Current energy: {energy}.")
        if crnt_event == "order" and energy - 30 >= 0:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        elif crnt_event == "order" and energy - 30 <= 0:
            energy += 50
            print("You had to rest!")
    else:
        if coins - value > 0:
            coins -= value
            print(f"You bought {crnt_event}.")
        else:
            print(f"Closed! Cannot afford {crnt_event}.")
            flag = False
            break

if flag:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
