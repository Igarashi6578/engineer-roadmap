import calculator

def judge_score(average):
    if average>=60:
        return "合格"
    else:
        return "不合格"


def analyze_student(student):
    score=student["score"]
    name=student["name"]
    average=calculator.calculate_average(score)
    b=judge_score(average)
    return name,average,b


score=[]
name=""