clothes_values = list(map(int, input().split()))
rack_cap = int(input())

stack_vals = []
while clothes_values:
    stack_vals.append(clothes_values.pop())

racks = [0]

while stack_vals:
    if stack_vals[-1] + racks[-1] <= rack_cap:
        racks[-1] += stack_vals.pop()
    else:
        racks.append(stack_vals.pop())

print(len(racks))
