raw_data = input()
water = int(input())

cells = raw_data.split("#")

total_fire = 0
effort = 0
putted_out_cells = []

for i in cells:
    crnt_cell = i.split(" = ")
    crnt_value = int(crnt_cell[1])
    if ((crnt_cell[0] == "Low" and 1 <= crnt_value <= 50) or \
        (crnt_cell[0] == "Medium" and 51 <= crnt_value <= 80) or \
        (crnt_cell[0] == "High" and 81 <= crnt_value <= 125)) and \
        water - crnt_value >= 0:
        water -= crnt_value
        effort += 0.25 * crnt_value
        total_fire += crnt_value
        putted_out_cells.append(crnt_value)

print("Cells:")
for i in putted_out_cells:
    print(f" - {i}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
