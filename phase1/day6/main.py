number=[10,20,30,40,50]
print(number[1:4])

name="Pyton"
print(name[0])
print(name[1])
print(len(name))

text="Pyton,Java,Go,TypeScript"
languag=text.split(",")
print(languag)

score=[45,82,91,63,55,78]
passed=[]
for a in score:
    if a>=60:
        passed.append(a)
print(passed)

number=[12,30,7,18,21,4]
new_list=[]
for i in number:
    if i>=10:
        new_list.append(i)
print(new_list)

a=[10,25,30,45,50]
f=[]
b=sum(a)
c=len(a)
avg=b/c
print(b)
print(avg)
for i in a:
    if i <= 60:
        f.append(i)
print(len(f))
print(type(avg))

score=[72,91,58,83,64,45,97,76]
num=[]
sk="="*20
print(sk)
print("成績")
print(sk)
for i in score:
    if i>=60:
        num.append(score)
a=sum(score)
b=len(score)
c=a/b
print(f"平均点：{c}")
f=max(score)
print(f"最高点：{f}")
for j in score:
    if j>=60:
        print(j)
print(f"合格者数：{len(num)}")