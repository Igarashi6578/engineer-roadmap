def new(number):
    new_number=[]
    for num in number:
        if num%2==0:
            new_number.append(num)
    return new_number
number=[1,2,3,4,5,6]
a=new(number)
print(a)

def judge(products):
    pro=[]
    for product in products:
        if product["price"]>=150:
             pro.append(product)
    return pro
products = [
    {"name": "りんご", "price": 120},
    {"name": "バナナ", "price": 150},
    {"name": "みかん", "price": 100},
    {"name": "ぶどう", "price": 300}
]
print(judge(products))


def judge(a):
    if a>=70:
        return "合格"  
def ave(score):
    return sum(score)/len(score)
students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": [55, 60, 48]},
    {"name": "鈴木", "score": [92, 88, 95]},
    {"name": "山田", "score": [68, 70, 65]}
]
name=[]
score=[]
for student in students:
    name=student["name"]
    score=student["score"]
    a=ave(score)
    b=judge(a)
    if b=="合格":
        print(name)

def avg(score):
    return sum(score)/len(score)
def filter_students(students):
    name=[]
    for student in students:
        score=student["score"]
        a=avg(score)
        if a>=70:
            name.append(student["name"])
    return name
def count_students(students):
    stu=filter_students(students)
    av=len(stu)
    return av
students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": [55, 60, 48]},
    {"name": "鈴木", "score": [92, 88, 95]},
    {"name": "山田", "score": [68, 70, 65]}
]
score=[]
name=[]
sv=filter_students(students)
av=count_students(students)
print(f"平均点70点以上：{sv} 人数：{av}人")

def avg(score):
    return sum(score)/len(score)
def filter_students(students):
    result=[]
    for stu in students:
        score=stu["score"]
        ad=avg(score)
        if ad>=70:
            result.append(stu)
    return result
def count_students(students):
    ac=filter_students(students)
    return len(ac)

students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": [55, 60, 48]},
    {"name": "鈴木", "score": [92, 88, 95]},
    {"name": "山田", "score": [68, 70, 65]}
]
name=[]
ak=filter_students(students)
for al in ak:
    name.append(al["name"])
Kt=count_students(students)
print(f"平均70点以上:{name} 人数：{Kt}人")