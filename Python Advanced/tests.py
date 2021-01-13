from datetime import time, timedelta

start = timedelta(hours=8, minutes=0, seconds=0)
for i in range(100):
    print(start + timedelta(seconds=i))
