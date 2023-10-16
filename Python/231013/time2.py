import datetime

now = datetime.datetime.now()

h=int(now.hour)
m=int(now.minute)
s=int(now.second)

five="*****"
two="*   *"
r1 = "    *"
l1="*    "
for1_1 = "  *  "
for1_2 = " **  "
colon = " * "
colon2 = "   "
middle = "  "

dictionaly = {
    0:[five,two,two,two,five],
    1:[for1_1,for1_2,for1_1,for1_1,five],
    2:[five,r1,five,l1,five],
    3:[five,r1,five,r1,five],
    4:[two,two,five,r1,r1],
    5:[five,l1,five,r1,five],
    6:[l1,l1,five,two,five],
    7:[five,two,r1,r1,r1],
    8:[five,two,five,two,five],
    9:[five,two,five,r1,r1],
    ":":[colon2,colon,colon2,colon,colon2],
    "mid":[middle],
}

if h>12:
    h1 = 0
    h2 = h-12
elif h<10:
    h1 = 0
    h2 = h
else:
    h1 = 1
    h2 = h-10

if m>10:
    m1 = int(m/10)
    m2 = int(m%10)
else:
    m1 = 0
    m2 = m

if s>10:
    s1 = int(s/10)
    s2 = int(s%10)
else:
    s1 = 0
    s2 = s
'''
for i in range(0,12):
    for j in range(0,5):
        if i == 10:
            print(dictionaly[":"][j])
        elif i == 11:
            print(dictionaly["mid"][0])
        else:
            print(dictionaly[i][j])
'''

for i in range(0,5):
    print(dictionaly[h1][i],end="")
    print(dictionaly["mid"][0],end="")
    print(dictionaly[h2][i],end="")
    print(dictionaly[":"][i],end="")
    print(dictionaly[m1][i],end="")
    print(dictionaly["mid"][0],end="")
    print(dictionaly[m2][i],end="")
    print(dictionaly[":"][i],end="")
    print(dictionaly[s1][i],end="")
    print(dictionaly["mid"][0],end="")
    print(dictionaly[s2][i],end="")
    print("")
