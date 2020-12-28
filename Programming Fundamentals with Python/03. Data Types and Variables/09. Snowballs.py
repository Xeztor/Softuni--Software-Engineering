n_sb = int(input())

max_value = 0

for i in range(n_sb):
    snow = int(input())
    time = int(input())
    quality = int(input())
    if int((snow / time)) ** quality > max_value:
        max_value = int((snow / time)) ** quality
        max_snow = snow
        max_time = time
        max_quality = quality
    if i == n_sb - 1:
        print(f"{max_snow} : {max_time} = {max_value} ({max_quality})")
