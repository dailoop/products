products = []
while True:
	name = input("請輸入商品名稱: ")
	if name == "q":
		print("感謝您的使用")
		break
	price = input("請輸入商品價格: ")
	products.append([name, price])
for a in products:
	print(a[0], a[1])