def say_hello():
    print("Hello!")
say_hello()

def great(name):
    print(f"こんにちは{name}さん")
great("Hiroki")
great("Tanaka")

def add(a,b):
    return a+b
result=add(10,20)
print(result)

def multiply(a,b):
    return a*b
result=multiply(5,4)
print(result)

def is_even(number):
    if number%2==0:
        return True
    else:
        return False
print(is_even(20))

def calculate_average(score):
    return sum(score)/len(score)
score=[80,70,90,60]
average=calculate_average(score)
print(average)

def great(name="Guest"):
    print(f"Hello {name}")
great()
great("Hiroki")

def get_passed_scores(scores):
    passed=[]
    for score in scores:
        if score>=60:
            passed.append(score)
    return passed
scores=[45,80,92,55,76]
result=get_passed_scores(scores)
print(result)

def calculate_average(scores):
    return sum(scores)/len(scores)
def get_max_score(scores):
    return max(scores)
def get_min_score(scores):
    return min(scores)
def get_passed_scores(scores):
    return [score for score in scores if score>=60]
scores=[72,91,58,83,64,45,97,76]
a=calculate_average(scores)
b=get_max_score(scores)
c=get_min_score(scores)
d=get_passed_scores(scores)
print(a)
print(b)
print(c)
print(d)