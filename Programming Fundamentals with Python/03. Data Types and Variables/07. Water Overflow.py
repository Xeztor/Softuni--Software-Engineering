refills = int(input())

cap = 255
liters_in_tank = 0

for i in range(refills):
    refill = int(input())
    if liters_in_tank + refill > cap:
        print("Insufficient capacity!")
    else:
        liters_in_tank += refill

print(liters_in_tank)
