activity = input()

cafe = 0

events = ["coding", "dog", "cat", "movie"]
while activity != "END":
    for i in range(len(events)):
        if activity == events[i]:
            cafe += 1
        elif activity == events[i].upper():
            cafe += 2
    activity = input()
if cafe <= 5:
    print(cafe)
else:
    print("You need extra sleep")