import time
mulai_waktu = time.time()
print("Menghitung (Jumlah Perhitungan)")
y = raw_input("Masukan angka y : ")
a = raw_input("masukan angka a : ")
b = raw_input("Masukan angka b : ")

if y == 'satu':
	y=1
if y == 'dua':
	y=2
if y == 'tiga':
	y=3
if y == 'empat':
	y=4
if y == 'lima':
	y=5
if y == 'enam':
	y=6
if y == 'tujuh':
	y=7
if y == 'delapan':
	y=8
if y == 'sembilan':
	y=9
if y == 'nol':
	y=0

if a == 'satu':
	a=1
if a == 'dua':
	a=2
if a == 'tiga':
	a=3
if a == 'empat':
	a=4
if a == 'lima':
	a=5
if a == 'enam':
	a=6
if a == 'tujuh':
	a=7
if a == 'delapan':
	a=8
if a == 'sembilan':
	a=9
if a == 'nol':
	a=0

if b == 'satu':
	b=1
if b == 'dua':
	b=2
if b == 'tiga':
	b=3
if b == 'empat':
	b=4
if b == 'lima':
	b=5
if b == 'enam':
	b=6
if b == 'tujuh':
	b=7
if b == 'delapan':
	b=8
if b == 'sembilan':
	b=9
if b == 'nol':
	b=0

Jumlah = (y*a)+b
print("Jumlah Perhitungan", Jumlah)
print("Waktu Menghitung : %s detik " % (time.time() - mulai_waktu))
