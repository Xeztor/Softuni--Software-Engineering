animals = input()

herd = animals.split(", ")

for i in range(len(herd)-1, -1, -1):
    if herd[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif herd[i] == "wolf":
        print(f"Oi! Sheep number {len(herd)-1 - i}! You are about to be eaten by a wolf!")