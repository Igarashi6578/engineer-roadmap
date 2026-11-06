class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"私は{self.name}です。{self.age}です。"

a=Person("田中",20)
b=Person("佐藤",22)

print(a.introduce())
print(b.introduce())

class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
    def calculate_average(self):
        return sum(self.scores)/len(self.scores)
    def judge_score(self):
        ave=self.calculate_average()
        if ave>=60:
            return "合格"
        else:
            return "不合格"
    def finish(self):
        return f"{self.name}:平均{self.calculate_average()}点,{self.judge_score()}"

student1 = Student("田中", [80, 75, 92])
student2 = Student("佐藤", [55, 60, 48])

print(student1.finish())
print(student2.finish())


class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
    def calculate_average(self):
        return sum(self.scores)/len(self.scores)
    def judge_score(self):
        ave=self.calculate_average()
        if ave>=60:
            return "合格"
        else:
            return "不合格"
    def finish(self):
        return f"{self.name}:平均{self.calculate_average()}点,{self.judge_score()}"

def filter_student(students):
        result=[]
        for student in students:
            if student.judge_score()=="合格":
                result.append(student)
        return result
students=[
    Student("田中",[80,75,92]),
    Student("佐藤",[55,60,48]),
    Student("鈴木",[92,88,95]),
    Student("山田",[40,50,55])
]

a=filter_student(students)
for b in a:
    print(b.finish())


class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def calculate_tax(self):
        return self.price*1.1
    def is_available(self):
        if self.stock>=1:
            return True
        else:
            return False

def filter_available_products(products):
    result=[]
    for product in products:
        a=product.is_available()
        if a==True:
            result.append(product)
    return result

products=[
    Product("りんご",150,10),
    Product("みかん",100,0),
    Product("バナナ",200,5),
    Product("ぶどう",500,0)
]
b=filter_available_products(products)
for cd in b:
    n=cd.calculate_tax()
    l=cd.name
    print(f"{l}:{n}円")