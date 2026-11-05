import math_utils

a=math_utils.add(10,5)
b=math_utils.multiply(10,5)
print(a,b)

from math_utils import add,multiply

a=add(10,5)
b=multiply(10,5)
print(a,b)

import analyzer
students = [
    {"name": "田中", "score": [80, 75, 92]},
    {"name": "佐藤", "score": [55, 60, 48]},
    {"name": "鈴木", "score": [92, 88, 95]}
]
for student in students:
    a,b,c=analyzer.analyze_student(student)
    print(f"{a}:平均{b}点,{c}")


import greeting
a="佐藤"
b=greeting.greet(a)
print(b)