def next_ver(ver):
    ver = list(map(int, ver))
    if ver[2] + 1 > 9:
        ver[1] += 1
        ver[2] = 0
        if ver[1] > 9:
            ver[0] += 1
            ver[1] = 0
    else:
        ver[2] += 1

    return list(map(str, ver))


crnt_v = input().split(".")
print(".".join(next_ver(crnt_v)))
