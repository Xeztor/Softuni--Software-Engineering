words = input().split()

for i in range(len(words)):
    crnt_word = list(words[i])
    special_chr = int("".join([i for i in crnt_word if i.isnumeric()]))
    del crnt_word[:len(list(str(special_chr)))]
    crnt_word.insert(0, chr(special_chr))
    crnt_word[1], crnt_word[-1] = crnt_word[-1], crnt_word[1]
    words[i] = "".join(crnt_word)

print(" ".join(words))
