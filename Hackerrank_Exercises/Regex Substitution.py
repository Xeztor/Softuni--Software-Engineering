import re

lines = [input() for _ in range(int(input()))]
outp = """
a = 1;
b = input();
if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides."""
outp_l = []
for l in lines:
    l = re.sub(r' (&&) ', ' and ', l)
    l = re.sub(r' (\|\|) ', ' or ', l)
    outp_l.append(l)

[print(line) for line in outp_l]
