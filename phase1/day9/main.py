def calculate(a,b):
    sum=a+b
    hiku=a-b
    kake=a*b
    waru=a/b
    return sum,hiku,kake,waru
result=calculate(10,2)
print(result)

def get_average(scores):
    return sum(scores)/len(scores)
def judge_score(scores):
    result=get_average(scores)
    if result>=60:
        return("合格")
    elif result<60:
        return("不合格")
scores=[34,55,27,85,88,99,76,89,98,88,99,99,99,99,99,99,99,99,97]
a=judge_score(scores)
print(a)

def calculate_average(scores):
    average_A=sum(scores)/len(scores)
    return average_A
def judge_score(average):
    if average>=60:
        return("合格")
    elif average<60:
        return("不合格")
def analyze_student(student):
    name=student["name"]
    scores=student["scores"]
    average=calculate_average(scores)
    return(f"{name},平均:{average},判定:{judge_score(average)}")
students=[
    {"name":"田中","scores":[80,75,92]},
    {"name":"佐藤","scores":[55,60,48]},
    {"name":"鈴木","scores":[92,88,95]},
    {"name":"山田","scores":[68,70,65]}
]
for student in students:
    result=analyze_student(student)
    print(result)