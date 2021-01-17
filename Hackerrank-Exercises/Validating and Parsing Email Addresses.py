import email.utils
import re

for _ in range(int(input())):
    name, email_inp = input().split()
    email_inp = email_inp[1:-1]
    if re.fullmatch(r'[A-Za-z][0-9A-Za-z_.-]+@[A-Za-z]+\.[A-Za-z]{1,3}', email_inp):
        print(email.utils.formataddr((name, email_inp)))
