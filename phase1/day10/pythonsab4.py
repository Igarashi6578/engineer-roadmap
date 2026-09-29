def sum_items(item):
    return sum(item)
def judge_heigh_order(sum_item):
    if sum_item>=3000:
        return "高額注文"
def average_order(heig_orders):
    return sum(heig_orders)/len(heig_orders)
orders = [
    {"customer": "田中", "items": [1200, 800, 1500]},
    {"customer": "佐藤", "items": [3000, 2500]},
    {"customer": "鈴木", "items": [500, 700, 900, 1200]},
    {"customer": "山田", "items": [5000]}
]
high_orders=[]
max_price=0
max_customer=None
for order in orders:
    item=order["items"]
    customer=order["customer"]
    sum_item=sum_items(item)
    judge_item=judge_heigh_order(sum_item)
    print(f"{customer}:{sum_item},{judge_item}")
    if judge_item=="高額注文":
        high_orders.append(sum_item)
    if sum_item>max_price:
        max_price=sum_item
        max_customer=customer
avg_order=average_order(high_orders)

print(f"最高額注文者 {max_customer},{max_price}円")