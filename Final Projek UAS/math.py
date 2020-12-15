menu = input()
if (menu=="1"):
	alas = float(input())
	b = float(input())
	c = float(input())
	tinggi = float(input())
	luas_segitiga = 1/2*(alas*tinggi)
	keliling_segitiga = alas+b+c
	print("luas segitiga adalah",luas_segitiga,"cm dan keliling segitiga adalah",keliling_segitiga,"cm")
elif (menu=="2"):
	r = float(input())
	luas = 3.14*r*r
	keliling = 3.14*2*r
	print("luas lingkaran adalah",luas,"cm dan keliling lingkaran adalah",keliling,"cm")
elif (menu=="3"):
	sisi = float(input())
	luas_persegi = sisi*sisi
	keliling_persegi = sisi+sisi+sisi
	print("luas persegi adalah",luas_persegi,"cm dan keliling persegi adalah",keliling_persegi,"cm")
else:
	print("selesai")
pilihan=input()
# File yang berada di node
