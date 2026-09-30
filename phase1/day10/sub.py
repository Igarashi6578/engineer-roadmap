def avg(score):
    return sum(score)/len(score)
def border(average):
    if average>=65:
        return "合格"
    else:
        return "不合格"
students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": [55, 60, 48]},
    {"name": "鈴木", "score": [92, 88, 95]},
    {"name": "山田", "score": [68, 70, 65]}
]
ok=0
for student in students:
    name=student["name"]
    score=student["score"]
    average=avg(score)
    avera=border(average)
    if avera=="合格":
        ok+=1
        print(f"{name}:平均:{average},判定:{avera}")
print(ok)