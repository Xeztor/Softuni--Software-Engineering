height, width = input().split()
height = int(height)
width = int(width)

chr = ".|."

for i in range(0, (height - 1) // 2):
        print((chr*i).rjust((width-2) // 2, "-")+chr+(chr*i).ljust((width-2) // 2, "-"))

print("WELCOME".center(width, "-"))

for i in range((height - 2) // 2, -1, -1):
    print((chr * i).rjust((width - 2) // 2, "-") + chr + (chr * i).ljust((width - 2) // 2, "-"))