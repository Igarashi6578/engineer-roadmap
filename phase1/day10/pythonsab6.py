def calculate_balance(transactions):
    return sum(transactions)
def judge_balance(balance):
    if balance<10000:
        return "注意"
    else:
        return "余裕あり"
accounts = [
    {
        "name": "田中",
        "transactions": [10000, -3000, 5000, -2000]
    },
    {
        "name": "佐藤",
        "transactions": [20000, -5000, -3000]
    },
    {
        "name": "鈴木",
        "transactions": [5000, 3000, -1000, 2000]
    },
    {
        "name": "山田",
        "transactions": [30000, -10000, -5000]
    }
]
dengerous=[]
many_many_name=None
many_many_transactions=0

for account in accounts:
    name=account["name"]
    transactions=account["transactions"]
    balance=calculate_balance(transactions)
    judge_balance_way=judge_balance(balance)
    print(f"{name}:残高{balance},{judge_balance_way}")
    if judge_balance_way=="注意":
        dengerous.append(name)
    if balance>many_many_transactions:
        many_many_transactions=balance
        many_many_name=name
print(f"注意が必要な人:{dengerous}")
print(f"最高残高:{many_many_name}{many_many_transactions}")