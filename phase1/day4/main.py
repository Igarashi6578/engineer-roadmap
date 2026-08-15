a=0
while a<=5:
    print(a)
    a+=1

a=0
while a<=10:
    print(a)
    a+=1

b=10
while b>=0:
    print(b)
    b=b-1

a=int(input("数字を入れてね"))
b=7
while a!=b:
    if a==b:
        print("正解です!")
    elif a<b:
        print("小さすぎます")
    else:
        print("大きすぎます") 
    a=int(input("数字を入れてね"))
print("正解です!")