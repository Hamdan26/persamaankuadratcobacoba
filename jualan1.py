print('\x1bc')
#IMPORT MODULE
import time
#ALAT
def k():
	print('kode : a. tambah; s. kali; l. lanjut')
	
def res():
	print('\x1bc')
	print('Uang masuk sejumlah ',masuk)
def res1():
	print('\x1bc')
	print('Uang keluar sejumlah ',keluar)
def res2():
	print('\x1bc')
	print('Cashback sejumlah ',cb)

awal=1
while awal>0:
	masuk=int(input('MASUKKAN UANG MASUK\n'))
	k()
	#UANG MASUK
	hit=1
	while hit>0:
		pencet=input('')
		if pencet=='a':
			masuk1=int(input())
			masuk=masuk+masuk1
			res()
			hit=hit+1
			k()
		elif pencet=='s':
			masuk1=int(input())
			masuk=masuk*masuk1
			res()
			hit=hit+1
			k()
		elif pencet=='l':
			print('tunggu...')
			time.sleep(1)
			#UANG KELUAR
			print('\x1bc')
			keluar=int(input('MASUKKAN UANG KELUAR\n'))
			k()
			hit2=1
			while hit2>0:
				pencet=input('')
				if pencet=='a':
					keluar1=int(input())
					keluar=keluar+keluar1
					res1()
					hit2=hit2+1
					k()
				elif pencet=='s':
					keluar1=int(input())
					keluar=keluar*keluar1
					res1()
					hit2=hit2+1
					k()
				elif pencet=='l':
					print('tunggu...')
					time.sleep(1)
					#CASHBACK
					print('\x1bc')
					cb=int(input('MASUKKAN CASHBACK\n'))
					k()
					hit3=1
					while hit3>0:
						pencet=input('')
						if pencet=='a':
							cb1=int(input())
							cb=cb+cb1
							res2()
							hit3=hit3+1
							k()
						elif pencet=='s':
							cb1=int(input())
							cb=cb*cb1
							res2()
							hit3=hit3+1
							k()
						elif pencet=='l':
							print('tunggu...')
							time.sleep(1)
							#OPERASI HITUNG
							print('\x1bc')
							print('\nJADI,\nUang masuk = ',masuk,'\nUang keluar = ',keluar,'\nCashback = ',cb)
							print('\nMAKA,\nPendapatan = ', masuk+cb,'\nPengeluaran = ', keluar,'\nUntung = ', masuk+cb-keluar,'\n')
							#AKHIRI/ULANGI SESI
							aoru=1
							while aoru>0:
								aus=input('Akhiri atau ulangi sesi?\nKode : n. Ulangi; m. Akhiri')
								if aus=='n':
									awal=awal+1
								elif aus=='m':
									break
								else:
									aoru=aoru+1
						
						else:
							res2()
							k()
							hit3=hit3+1
				
				else:
					res1()
					k()
					hit2=hit2+1
		
		else:
			res()
			k()
			hit=hit+1
