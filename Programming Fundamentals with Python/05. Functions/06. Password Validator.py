def pw_validator(pw):
    warnings = []
    digits = 0
    if not 6 <= len(pw) <= 10:
        warnings.append("Password must be between 6 and 10 characters")
    for i in pw:
        if not 97 <= ord(i) <= 122 and \
                not 65 <= ord(i) <= 90 and \
                not 48 <= ord(i) <= 57:
            if "Password must consist only of letters and digits" not in warnings:
                warnings.append("Password must consist only of letters and digits")
        elif i.isnumeric():
            digits += 1
    if not digits >= 2:
        warnings.append("Password must have at least 2 digits")
    return warnings


user_pw = input()
warns = pw_validator(user_pw)
if warns:
    for j in warns:
        print(j)
else:
    print("Password is valid")
