n = int(input())
arr = map(int, input().split())

num_list = list(arr)
max_score = max(num_list)
occur = num_list.count(max_score)
for _ in range(occur):
    num_list.remove(max_score)

print(max(num_list))
