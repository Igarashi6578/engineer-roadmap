def score_sum(score):
    return sum(score)
def score_judge(sumscore):
    if sumscore>=300:
        return "クリア"
    else:
        return "失敗"
players = [
    {"name": "Hiroki", "scores": [120, 80, 150]},
    {"name": "Tanaka", "scores": [90, 110, 70]},
    {"name": "Sato", "scores": [200, 180, 160]},
    {"name": "Yamada", "scores": [50, 80, 60]}
]
best_score=0
best_player=0
for player in players:
    name=player["name"]
    score=player["scores"]
    sumscore=score_sum(score)
    judge=score_judge(sumscore)
    print(f"{name}:合計{sumscore},{judge}")
    if sumscore>best_score:
        best_score=sumscore
        best_player=player["name"]
print(f"最高点プレイヤー:{best_player}")