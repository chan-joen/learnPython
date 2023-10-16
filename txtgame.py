import random
        
def RSP():
    i=input("가위 바위 보: ")
    j=random.randint(1,3)
    
    if j==1:
        if i=="가위":
            print("비겼습니다")
            return 1000
        elif i=="바위":
            print("이겼습니다")
            return 2000
        elif i=="보":
            print("졌습니다")
            return 0
    elif j==2:
        if i=="가위":
            print("졌습니다")
            return 0
        elif i=="바위":
            print("비겼습니다")
            return 1000
        elif i=="보":
            print("이겼습니다")
            return 2000
    elif j==3:
        if i=="가위":
            print("졌습니다")
            return 0
        elif i=="바위":
            print("이겼습니다")
            return 2000
        elif i=="보":
            print("비겼습니다")
            return 1000

def UD():
    print("1~100까지의 숫자중 하나를 맞추시오")
    j=random.randint(1,100)
    k=0
    i=0
    while i!=j:
        i=int(input("숫자입력:"))
        if i<j:
            print("업")
        elif i>j:
            print("다운")
        k=k+1
    print(k,"번 만에 맞춤")
    if k==1:
        print("+40000")
        return 40000
    elif k<=3:
        print("+10000")
        return 10000
    elif k<=5:
        print("+2000")
        return 2000
    else:
        print("+1000")
        return 1000

def rotto():
    print("6개의 숫자 입력")
    i=[0,0,0,0,0,0]
    j=[0,0,0,0,0,0]
    l=0
    k=0

    while k!=6:
        print(k+1,"번째 숫자 입력:")
        i[k]=int(input())
        if i[k]<=0 or i[k]>45:
                print("범위를 넘어간 숫자는 입력 할 수 없습니다")
                continue
        for a in range(k):
            if i[k]==i[a]:
                print("같은숫자는 입력 할 수 없습니다")
                k=k-1
                continue
        k=k+1
        
    k=0    
    while k!=6:
        j[k]=random.randint(1,45)
        for a in range(k):
            if j[k]==j[a]:
                k=k-1
                continue
        k=k+1
    
    for k in range(6):
        for a in range(6):
            if i[k]==j[a]:
                l=l+1
    print("추첨")
    for k in range(6):
        print(j[k])
    print("내 번호")
    for k in range(6):
        print(i[k])
    
    if l==6:
        print("1등입니다!")
        return 1000000000
    elif l==5:
        print("2등입니다!")
        return 6000000
    elif l==4:
        print("3등입니다!")
        return 100000
    elif l==3:
        print("4등입니다!")
        return 7000
    elif l==2:
        print("5등입니다!")
        return 4000
    elif l==1:
        print("6등입니다!")
        return 2000;
    else:
        print("꽝!!")
        return 0;

def GB():
    i=int(input("도박 금액 입력:"))
    j=random.randint(1,1000)
    if j==576:
        print("5배! +",i*4)
        return i*4
    elif j%2==0:
        print("잃었습니다 -",i)
        return -i
    elif j%2==1:
        if j%9==0:
            print("3배! +",i*2)
            return i*2
        elif j%6==0:
            print("2배! +",i)
            return i
        else:
            print("1배! + 0")
            return 0

def end(Money):
    f=open("money.data","w")
    f.write(str(Money))
    f.close()

    
try:
    f = open('money.data','r')
except FileNotFoundError:
    Money=10000
else:
    a=f.read()
    f.close()
    Money=int(a)
while True:
    print("현재금액:",Money)
    choose=input("무엇을 할지 고르시오 | 가위바위보 | 업다운| 로또 | 도박 | 종료 |:")
    if choose=="가위바위보":
        if Money<1000:
            print("돈이 부족합니다")
            continue
        Money-=1000
        a=RSP()
        Money+=a
    elif choose=="업다운":
        a=UD()
        Money+=a
    elif choose=="로또":
        if Money<2000:
            print("돈이 부족합니다")
            continue
        Money-=2000
        a=rotto()
        Money+=a
    elif choose=="도박":
        if Money==0:
            print("돈이 부족합니다")
            continue
        a=GB()
        Money+=a
    elif choose=="종료":
        end(Money)
        break
