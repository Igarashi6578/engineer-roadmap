huma={
    "name":"田中",
    "age":"20",
    "score":"85"
}
print(huma)
print(huma["name"])
print(huma["age"])
print(huma["score"])
huma["score"]=90
print(huma)
huma["univer"]="度個科荷大学"
print(huma)
del huma["age"]
print(huma)

studen={
    "name":"田中",
    "age":20,
}
for key in studen:
    print(key)
for key, value in studen.items():
    print(key,value)

man={
    "呼び方":"山田",
    "年齢":"21",
    "大学":"川大学",
    "学年":3
}
for key,value in man.items():
    print(f"{key}は{value}")

score={
    "田中":80,
    "佐藤":55,
    "鈴木":92,
    "山田":68
}

for key, value in score.items():
    if value>=60:
        print(key,value)

price={
    "apple":150,
    "banana":100
}
new=0
for value in price.values():
    new+=value
print(new)

student={
    "name":"田中",
    "age":20,
    "scores":[80,75,92,88]
}
new=[]
print(student["name"])
print(student["age"])
print(f"全科目の点数{student["scores"]}")
for i in student["scores"]:
    new.append(i)
a=sum(new)
b=len(new)
avg=a/b
print(avg)
print(max(new))
print(min(new))