english_count = int(input())
english_users = set(input().split())

french_count = int(input())
french_users = set(input().split())

print(len(english_users.symmetric_difference(french_users)))
