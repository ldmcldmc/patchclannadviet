# # -*- coding: utf-8 -*-
import re, sys, time, os
sys.stdout.reconfigure(encoding='utf-8')
from terminaltables import AsciiTable
clear = lambda: os.system('cls')

#Lay list file
from os import listdir
from os.path import isfile, join
listfile = [f for f in listdir('..\\seenviet') if isfile(join('..\\seenviet', f) )]
listfile = [f for f in listfile if 'SEEN' in f ]
for i in range(len(listfile)):
	listfile[i]=listfile[i][4:-4]


# Lay du lieu
def laydulieu(file):
	global seenraw
	global seenviet
	global orgraw
	f=open('..\\seens\\SEEN'+file+' - Copy.utf','r',encoding="utf-8")
	seenraw=f.read().split('\n')
	f.close()
	f=open('..\\seenviet\\SEEN'+file+'.txt','r',encoding="utf-16")
	data=f.read().split('\n')
	seenviet = [t for t in data if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None ]
	f.close()
	f=open('..\\seens\\SEEN'+file+' - Copy.org','r',encoding="utf-8")
	orgraw=f.read().split('\n')
	f.close()


#xet su trung nhau 2 file
def checkline(file):
	datarawline=[t[:6] for t in seenraw if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None]
	if not datarawline==[t[:6] for t in seenviet]:
		return False 
	else:
		return True

def demsoline(file):
	datarawline=[t[:6] for t in seenraw if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None]
	return [len(seenviet),len(datarawline)]


def findch(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def thongkeloi(file):
	result=[]
	for i in range(len(orgraw)):
		if "farcall_with(9820, 3," in orgraw[i] or "timeExC" in orgraw[i]:
			res=orgraw[i-1][5:]
			res2=orgraw[i+1][5:]
			for v in seenviet:
				if res in v: lineviet1=v
			for v in seenviet:
				if res2 in v: lineviet2=v
			for u in seenraw:
				if res in u: lineraw1=u
			for u in seenraw:
				if res2 in u: lineraw2=u
			# Line So / Loai Loi / Ban HD 1 / Ban HD 2 / Ban Viet 1/ Ban viet 2]
			if orgraw[i][23:-2] in lineviet1:
				result+=[[lineviet1[1:5],'dangopedia',lineraw1,lineraw2,lineviet1,lineviet2]]
			elif "\\g" in lineviet1:
				result+=[[lineviet1[1:5],'tag g',lineraw1,lineraw2,lineviet1,lineviet2]]
			else:
				result+=[[lineviet1[1:5],'',lineraw1,lineraw2,lineviet1,lineviet2]]
	for t in seenviet:
		if re.match(r"<[0-9][0-9][0-9][0-9]>", t[:6]) is not None and '\\size{}' in t:
			result+=[[t[:6],'cỡ chữ', '', '' , t , '' ]]
	
	table = AsciiTable(result)
	print(table.table)
	time.sleep(5)
	clear()
	checkfile(file)










def checkfile(file):
	laydulieu(file)
	if not checkline(file):
		a=demsoline(file)
		print('File {} khong trung so line giua 2 ban HD ({}) va ban Viet ({})'.format(file,a[1],a[0]))
		print('Cac line co the gap loi la:')
		thongkeloi(file)


for file in listfile:
	checkfile(file)