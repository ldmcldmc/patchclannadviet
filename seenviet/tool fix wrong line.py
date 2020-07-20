# # -*- coding: utf-8 -*-
from os import listdir
import re, sys, time, os
sys.stdout.reconfigure(encoding='utf-8')
from terminaltables import AsciiTable
clear = lambda: os.system('cls')
import pyperclip

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

def wrap(string, length=25):
	s = [string[0+i:length+i] for i in range(0, len(string), length)]
	if len(s)>3: s=s[:3]
	s='\n'.join(s)
	return s

def chinhstt():
	patha=sys.argv[0]
	patha=patha[:0-len(patha.split('.')[-1])-21]
	files = [f for f in listdir(patha) if isfile(join(patha, f)) and f[-4:].lower()=='.txt']
	for file in files:
		with open(file,'r',encoding='utf-16') as f:
			content = f.readlines()
		f.close()
		i=0
		result=[]
		for a in range(len(content)):
			if re.match(r"<[0-9][0-9][0-9][0-9]>", content[a]) is not None:
				content[a]='<'+f'{i:04}'+'>'+content[a][6:]
				result=result+[content[a]]
				i=i+1
			else:
				result+=[content[a]]
		fa=open(file,'w',encoding='utf-16')
		for row in result:
			fa.writelines(row)
		fa.close()

def findch(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def thongkeloi(file):
	result=[['Line','Loi','HD1','HD2','Viet1','Viet2']]
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
				result+=[[lineviet1[1:5],'dangopedia',wrap(lineraw1),wrap(lineraw2),wrap(lineviet1),wrap(lineviet2)]]
			elif "\\g" in lineviet1:
				result+=[[lineviet1[1:5],'tag g',wrap(lineraw1),wrap(lineraw2),wrap(lineviet1),wrap(lineviet2)]]
			else:
				result+=[[lineviet1[1:5],'',wrap(lineraw1),wrap(lineraw2),wrap(lineviet1),wrap(lineviet2)]]
	for t in seenviet:
		if re.match(r"<[0-9][0-9][0-9][0-9]>", t[:6]) is not None and '\\size{}' in t:
			for g in range(len(seenraw)):
				try:
					if seenraw[g][:6] == t[:6]: ra = g
				except:
					pass
			result+=[[t[1:5],'cỡ chữ', wrap(seenraw[ra+1]) , wrap(seenraw[ra+2]) , wrap(t) , wrap(seenviet[seenviet.index(t)+1]) ]]
	for t in seenviet:
		if re.match(r"<[0-9][0-9][0-9][0-9]>", t[:6]) is not None and re.match(r"^<[0-9]{4}> .{3,}\\[A-Za-z]{0,1}\{[A-Za-z]\}", t) is not None:
			for g in range(len(seenraw)):
				try:
					if seenraw[g][:6] == t[:6]: ra = g
				except:
					pass
			result+=[[t[1:5],'name', wrap(seenraw[ra+1]) , wrap(seenraw[ra+2]) , wrap(t) , wrap(seenviet[seenviet.index(t)+1]) ]]
	
	result=[result[0]]+sorted(result[1:], key=lambda x: int(x[0]))
	table = AsciiTable(result)
	print(table.table)
	while True:
		laydulieu(file)
		if '<0000>' in [g[:6] for g in seenviet][1:] or checkline(file):
			break
		else:
			time.sleep(1)
	clear()
	checkfile(file)


def checkfile(file):
	laydulieu(file)
	if not checkline(file):
		a=demsoline(file)
		print('File {} không trùng số line giữa 2 bản HD: {} và Việt: {}. Số line lệch: {}'.format(file,a[1],a[0],abs(int(a[1]-int(a[0])))))
		chinhstt()
		print('Cac line co the gap loi la:')
		pyperclip.copy('\n<0000> ')
		thongkeloi(file)


for file in listfile:
	checkfile(file)



# ^(\/\/|<[0-9]{4}>) .{3,}\\[A-Za-z]{0,1}\{[A-Za-z]\}