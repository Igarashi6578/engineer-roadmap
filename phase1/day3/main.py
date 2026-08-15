for i in range(5):
    print(i)

for i in range(1,11):
    print(i)

total=0
for i in range(1,11):
    total=total+i
print(total)

total=0
for i in range(1,101):
    total=total+i
print(total)

for i in range(1,21):
    if i%2==0:
        print(i)

for i in range(1,101):
    if i % 3 == 0:
        print(i)

for i in range(1,10):
    for a in range(1,10):
        print(f"{i}×{a}={i*a}")