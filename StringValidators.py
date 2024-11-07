# String Validators in Python
if __name__ == '__main__':
    s = input()
    lst = list(s)

    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    for i in lst:
        if i.isalnum() == True:
            alnum = True
        if i.isalpha() == True:
            alpha = True
        if i.isdigit() == True:
            digit = True
        if i.islower() == True:
            lower = True
        if i.isupper() == True:
            upper = True

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
