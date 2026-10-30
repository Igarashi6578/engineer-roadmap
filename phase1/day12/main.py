try:
    a=int(input("整数を入力してください"))
    b=100/a
    print(f"結果：{b}")
except ZeroDivisionError:
    print("0ではわれません")
except ValueError:
    print("数字を入力してください")

def calculate_average(scores):
    if not scores:
        raise ValueError("点数がありません")
    return sum(scores)/len(scores)
scores=[]
try:
    a=calculate_average(scores)
    print(f"平均点：{a}")
except ValueError as e:
    print(e)

def calculate_average(scores):
    if not scores:
        raise ValueError("点数がありません")
    return sum(scores)/len(scores)
def judge_score(average):
    if average>=60:
        return "合格"
    else:
        return "不合格"
def analyze_student(student):
    name=student["name"]
    scores=student["score"]
    average=calculate_average(scores)
    b=judge_score(average)
    return name,average,b
students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": []},
    {"name": "鈴木", "score": [92, 88, 95]},
    {"name": "山田", "score": [40, 50, 55]}
]
for student in students:
    try:
        c=analyze_student(student)
        print(f"{c[0]}平均{c[1]}点、{c[2]}")
    except ValueError as e:
        print(e)