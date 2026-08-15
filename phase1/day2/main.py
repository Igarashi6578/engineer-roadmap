age=20
if age>=20:
    print("成人です")

age=18
if age>=20:
    print("成人です")
else:
    print("未成年です")

score=75
if score>=90:
    print("A")
elif score>=70:
    print("B")
elif score>=60:
    print("C")
else:
    print("D")

a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

age=20
has_ticket=True
if age>=18 and has_ticket:
    print("入場できます")

is_student=True
is_employe=False
if is_student or is_employe:
    print("対象者です")

score=90
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("D")

age=3
if 0<=age<=12:
    print("子供")
elif 13<=age<=17:
    print("中高生")
elif 18<=age<=22:
    print("大学生")
else:
    print("大人")

age=20
has_ticket=True
if age>=20 and has_ticket:
    print("可能")
else:
    print("不可能")

score=int(input("点数を入力してください"))
if 90<=score<=100:
    print("Excellent")
elif 80<=score<=89:
    print("Great")
elif 70<=score<=79:
    print("Good")
elif 60<=score<=69:
    print("Pass")
else:
    print("Fail")

name=int(input("名前を入力して"))
age=int(input("年齢を入力して"))
print(f"{name}さんは{age}歳です")
if age>=21:
    print("成人です")
else:
    print("未成年です")

