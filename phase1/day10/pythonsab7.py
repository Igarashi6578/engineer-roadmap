def avg_team(score):
    return sum(score)/len(score)
def judge_score(avg):
    if avg>=80:
        return "好成績"
    else:
        return "要強化"

teams = [
    {
        "name": "Aチーム",
        "players": [
            {"name": "田中", "score": 80},
            {"name": "佐藤", "score": 95},
            {"name": "鈴木", "score": 70}
        ]
    },
    {
        "name": "Bチーム",
        "players": [
            {"name": "山田", "score": 88},
            {"name": "高橋", "score": 92}
        ]
    },
    {
        "name": "Cチーム",
        "players": [
            {"name": "伊藤", "score": 60},
            {"name": "渡辺", "score": 75},
            {"name": "中村", "score": 85}
        ]
    }
]

high_player=""
high_score=0
low_player=[]
name=[]

for i in teams:
    names=i["name"]
    print(names)
    score=[]
    for j in i["players"]:
        name.append(j["name"])
        score.append(j["score"])
        n=j["name"]
        s=j["score"]
        print(f"{n}:{s}点")
        if high_score<s:
            high_player=n
            high_score=s
        if s<=80:
            low_player.append(n)
    avg=avg_team(score)
    judge=judge_score(avg)
    print(f"平均点：{avg}点")
    print(judge)

print(f"最高得点:{high_player}{high_score}点")
print(f"要強化選手：{low_player}")