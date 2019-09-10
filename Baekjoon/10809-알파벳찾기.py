alpabet = [chr(i) for i in range(97, 123)]
_str = ""
check = input()
for a in alpabet:
    if a in check:
        _str += "{} ".format(check.index(a))
    else:
        _str += "-1 "

print(_str)
