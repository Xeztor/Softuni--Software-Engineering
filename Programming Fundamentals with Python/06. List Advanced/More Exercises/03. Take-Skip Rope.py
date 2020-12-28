def decrypt(encrypted_msg):
    nums = list(reversed([int(encrypted_msg.pop(encrypted_msg.index(i))) for i in encrypted_msg[::-1]
                          if i.isnumeric()]))
    encrypted = []
    for i in range(0, len(nums), 2):
        encrypted += encrypted_msg[:nums[i]]
        del encrypted_msg[:nums[i] + nums[i + 1]]

    return "".join(encrypted)


given_encrypted = list(input())
print(decrypt(given_encrypted))
