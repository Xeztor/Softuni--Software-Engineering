clock_cycles = list(map(int, input().split(', ')))

job_wanted = clock_cycles[int(input())]
total_clock_cycles = 0

while not job_wanted == min(clock_cycles) or clock_cycles.count(job_wanted) > 1:
    total_clock_cycles += clock_cycles.pop(clock_cycles.index(min(clock_cycles)))

print(total_clock_cycles + job_wanted)
