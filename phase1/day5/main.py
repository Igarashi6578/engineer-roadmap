number=[10,20,30,40,50]
print(number)
print(number[1])
print(number[4])
print(number[-4])
number[1]=200
print(number)

number=[10,20,30]
number.append(40)
print(number)
number.insert(1,15)
print(number)
number.remove(20)
print(number)
number.pop()
print(number)
number=[10,20,30,40,50]
print(len(number))

name=["田中","山田","鈴木"]
for i in name:
    print(i)

score=[80,55,90,65,40]
for a in score:
    if a>=60:
        print(f"{a}点:合格")
    else:
        print(f"{a}点:不合格")

language=["Python","JavaScript","Ruby","Java","GO"]
for b in language:
    print(b)

score=[65,82,91,54,76,88,43]
for i in score:
    if i>=80:
        print(i)

number=[10,20,30,40,50]
a=0
for i in number:
    a+=i
print(a)

score=[80,92,73,88]
print(score)
for i in score:
    if i>=60:
        print(f"{i}点：合格")