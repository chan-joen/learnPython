a = input('입력: ')

sa=a.split(',')

f = sa[2].find("(")
b = sa[2][1:f]
format_a = "{},{}".format(sa[0],b)
print(format_a)