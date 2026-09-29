def get_passed_scores(scores):
    return [score for score in scores if score>=60]
scores=[45,82,91,55,76,63,39]
result=get_passed_scores(scores)
print(result)

def print_passed_students(students):
    for student in students:
        if student["score"]>=60:
            print(f"{student["name"]}, {student["score"]}")
students = [
    {"name": "田中", "score": 80},
    {"name": "佐藤", "score": 55},
    {"name": "鈴木", "score": 92},
    {"name": "山田", "score": 68}
]
print_passed_students(students)

def calculate_average(students):
    ave=[student["score"] for student in students]
    return sum(ave)/len(ave)
students=[
    {"name":"田中","score":80},
    {"name":"佐藤","score":60},
    {"name":"鈴木","score":100}
]
result=calculate_average(students)
print(result)

def calculate_average(scores):
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
    judge=judge_score(average)
    return f"{name}:平均:{average},判定:{judge}"
students=[
    {"name":"田中","score":[80,75,92]},
    {"name":"佐藤","score":[55,60,48]},
    {"name":"鈴木","score":[92,88,95]},
    {"name":"山田","score":[68,70,65]}
]
for student in students:
    result=analyze_student(student)
    print(result)

def caluclate_average(score):
    return sum(score)/len(score)
def judge_student(average):
    if average>=60:
        return "合格"
    else:
        return "不合格"
def analyze_student(student):
    name=student["name"]
    score=student["score"]
    average=caluclate_average(score)
    judge=judge_student(average)
    if judge=="合格":
        return f"{name}:平均:{average},判定:{judge}"
students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": [55, 60, 48]},
    {"name": "鈴木", "score": [92, 88, 95]},
    {"name": "山田", "score": [68, 70, 65]}
]
count=0
for student in students:
    result=analyze_student(student)
    if result!=None:
        count+=1
        print(result)
print(f"合格者数：{count}")