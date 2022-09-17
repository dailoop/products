import os
products = []
if os.path.isfile("products.csv"):#檢查檔案在不再
	print("yes")
	#讀取檔案
	with open("products.csv", "r", encoding="utf-8") as g:
		for line in g:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
else:
	print("no")
print(products)


#讓使用輸入
while True:
	name = input("請輸入商品名稱: ")
	if name == "q":
		print("感謝您的使用")
		break
	price = input("請輸入商品價格: ")
	products.append([name, price])
for a in products:
	print(a[0], a[1])
#寫入檔案
with open("products.csv", "w" , encoding="utf-8") as g:
	g.write("商品,價格\n")
	for p in products:
		g.write(p[0] + "," + p[1] + "\n")