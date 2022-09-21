import os
#讀取檔案
def read_file(file_name):
	with open(file_name, "r", encoding="utf-8") as g:
		products = []
		for line in g:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])	
	print(products)
	return products
#讓使用輸入
def inputo(products):
	while True:
		name = input("請輸入商品名稱: ")
		if name == "q":
			print("感謝您的使用")
			break
		price = input("請輸入商品價格: ")
		products.append([name, price])
	return products
#印出清單
def print_products(products):
	for a in products:
		print(a[0], a[1])
#寫入檔案
def write(file_name, products):
	with open(file_name, "w" , encoding="utf-8") as g:
		g.write("商品,價格\n")
		for p in products:
			g.write(p[0] + "," + p[1] + "\n")

def main(file_name):
	if os.path.isfile(file_name):
		print("yes")
		products =  read_file("products.txt")
		products = inputo(products)
		print_products(products)
		write("products.txt", products)
	else:
		print("no")
h = input("檔名: ")
main(h)