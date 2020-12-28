def palindrome_checker(list_nums):
    nums_list = list_nums.split(", ")
    for i in range(len(nums_list)):
        crnt_num = list(nums_list[i])
        rev_list = list(nums_list[i])
        rev_list.reverse()
        if crnt_num == rev_list:
            print(True)
        else:
            print(False)


raw_data = input()

palindrome_checker(raw_data)
