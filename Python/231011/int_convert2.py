a = input("a: ")
b = input("b: ")

try:
    int_a = int(a)
    int_b = int(b)

    print("합:",int_a+int_b)
    print("곱:",int_a*int_b)
    print("차:",abs(int_a-int_b))
    print("문자열",a+b)
except:
    print("a 또는 b를 int형으로 바꿀 수 없습니다.")
    