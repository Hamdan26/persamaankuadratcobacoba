print('MENCARI AKAR AKAR PERSAMAAN KUADRAT')
import time
print('please wait...')
time.sleep(2)
print('\x1bc')
import math
count=1
while count >0 :
	print('\x1bc')
	print('Masukkan angka')
	a=float(input('a = '))
	b=float(input('b = '))
	c=float(input('c = '))
	D=a*c*4
	plusmin= math.sqrt ( b**2 - D)
	xsatu=(-b+plusmin)/(2*a)
	xdua=(-b-plusmin)/(2*a)
	print('maka,') ; print ('diskriminan = ', D)
	print('akar akar persamaan = ', xsatu , ' atau ' , xdua)
	penentu=input('Lagi? Y/N? ')
	if penentu=='N':
		break
	elif penentu=='Y':
		count=count+1
	else :
		print('\x1bc')
		print('JAWAB YANG BENER WOI')
		time.sleep (2)
		print('Dahlah, males...., ngodingnya lama')
		time.sleep(1)
		break
