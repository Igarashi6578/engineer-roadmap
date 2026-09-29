def calculate_stock_value(price,stock):
    return price*stock
products = [
    {"name": "キーボード", "price": 8000, "stock": 3},
    {"name": "マウス", "price": 3000, "stock": 10},
    {"name": "モニター", "price": 25000, "stock": 2},
    {"name": "USBケーブル", "price": 1200, "stock": 20}
]
count=0
max_value=0
max_name=None
for product in products:
    name=product["name"]
    price=product["price"]
    stock=product["stock"]
    stck_value=calculate_stock_value(price,stock)
    print(f"{name}:{price}円")
    if stock<=5:
        print("在庫少")
    else:
        pass
    count+=stck_value
    if product["price"]>max_value:
        max_value=product["price"]
        max_name=product["name"]
    else:
        pass
print(f"在庫合計金額:{count}円")
print(f"最高価格の商品:{max_name},{max_value}円")