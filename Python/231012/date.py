import datetime

now = datetime.datetime.now()

print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

if now.hour <12:
    print("현재 시각은 {}시로 오전입니다".format(now.hour))

if now.hour>=12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

if 6<= now.month <=8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))

if now.month == 12 or 1 <= now.month<=2:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))