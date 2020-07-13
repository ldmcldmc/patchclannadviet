import sys
sys.stdout.reconfigure(encoding='utf-8')



# import re
# #Lay list file
# from os import listdir
# from os.path import isfile, join
# listfile = [f for f in listdir('seenviet') if isfile(join('seenviet', f) )]
# for i in range(len(listfile)):
# 	listfile[i]=listfile[i][4:-4]

# for file in listfile:
# 	# Lay du lieu so sanh
# 	f=open('seens\\SEEN'+file+' - Copy.utf','r',encoding="utf-8")
# 	dataraw=f.read().split('\n')
# 	f.close()
# 	f=open('seenviet\\SEEN'+file+'.txt','r',encoding="utf-16")
# 	data=f.read().split('\n')
# 	dataviet=[]
# 	for t in data:
# 		if len(t)==0: continue
# 		if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
# 			dataviet=dataviet+[t]
# 	del data
# 	f.close()
# 	# loc stt du lieu
# 	raw =[]
# 	for t in dataraw:
# 		if re.search(r"<[0-9][0-9][0-9][0-9]>", t):
# 			raw = raw + [t[:6]]
# 	viet =[]
# 	for t in dataviet:
# 		if re.search(r"^<[0-9][0-9][0-9][0-9]>", t):
# 			viet = viet + [t[:6]]
# 	# so sanh
# 	result = True 
# 	# if not len(raw)==len(viet): 
# 	# 	result= False
# 	# else:
# 	# 	for i in range(len(raw)):
# 	# 		if not raw[i]==viet[i]:
# 	# 			result=False
# 	if not viet==raw: result=False
# 	if result: print(file)







# 	# Lay tat ca file seen từ Baka-tsuki theo route
# route='0' # Sửa Rote ở đây, thích route nào thì đánh số thứ tự đầu của route đó
# import re, requests
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# # driver = webdriver.Firefox()
# # Lay list file
# from os import listdir
# from os.path import isfile, join
# listfile = [f for f in listdir('seens') if isfile(join('seens', f) )]
# listfile = [f for f in listfile if f[-1]=='g' and f[4]==str(route) and 'Copy' not in f]
# for i in range(len(listfile)):
# 	listfile[i]=listfile[i][4:-4]
# listfile=list(set(listfile))
# for file in listfile:
# 	# if file!='7600':continue
# 	# Lay du lieu qua mang
# 	try:
# 		# link=driver.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file)
# 		# soup=BeautifulSoup(driver.page_source,'lxml')
# 		link = requests.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file)
# 		soup=BeautifulSoup(link.content,'lxml')
# 		data=soup.find('pre').text.split('\n')
# 	except :
# 		try:
# 			print(file)
# 			link = requests.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file+'P1')
# 			soup=BeautifulSoup(link.content,'lxml')
# 			data=soup.find('pre').text.split('\n')
# 			try:
# 				idriver=2
# 				while True:
# 					link = requests.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file+'P'+str(idriver))
# 					soup=BeautifulSoup(link.content,'lxml')
# 					data+=soup.find('pre').text.split('\n')
# 					idriver+=1
# 			except:
# 				pass
# 		except:
# 			print(file+'       !!!!!!!!')
# 			data=[]
# 			continue
# 	f=open('seenviet\\SEEN'+file+'.txt','w',encoding='utf-16')
# 	f.write('\n'.join(data))
# 	f.close()






















# 	# Thong ke tat ca ca line seen cho tester
# import re
# #Lay list file
# from os import listdir
# from os.path import isfile, join
# listfile = [f for f in listdir('seenviet') if isfile(join('seenviet', f) )]
# listfile = [f for f in listfile if 'SEEN' in f ]
# for i in range(len(listfile)):
# 	listfile[i]=listfile[i][4:-4]

# ia=1
# for file in listfile:
# 	f=open('seenviet\\SEEN'+file+'.txt','r',encoding="utf-16")
# 	data=f.read().split('\n')
# 	for i in range(len(data)):
# 		if re.match("<[0-9][0-9][0-9][0-9]>", data[i]) is not None:
# 			print(str(ia)+'\t'+file+'\t'+data[i])
# 			ia+=1



# 	# lay character cua cac file trong seenviet
# import re
# #Lay list file
# from os import listdir
# from os.path import isfile, join
# listfile = [f for f in listdir('seenviet') if isfile(join('seenviet', f) )]
# listfile = [f for f in listfile if f[-1]=='t' and 'SEEN' in f and 'Copy' not in f]
# chr=[]
# for file in listfile:
# 	f=open('seenviet/'+file,'r',encoding='utf-16')
# 	a=f.read().split('\n')
# 	f.close()
# 	for t in a:
# 		if re.match(r"<[0-9][0-9][0-9][0-9]>", t):
# 			m= re.findall( r'\\{[^\{]+}', t)
# 			if len(m)!=0:chr+=[m[0]]
# chr=list(set(chr))
# for t in chr:
# 	print(t[2:-1])







# d=[r"\{       }\mvx{-17}\mvy{-80}Ba\size{20}\mv{-18,3}´\mv{-2,-3}\size{}c ga\size{20}\mv{-18,3}´\mv{-2,-3}\size{}i\mvy{34}\n\mvx{-17}",r"\{               }\mvx{-17}\mvy{-80}Ba\size{20}\mv{-11,19}.\mv{2,-19}\size{}n cu\size{20}\mv{-14,3}`\mv{5,-3}\size{}ng lo\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}p\mvy{34}\n\mvx{-17}",r"\{       }\mvx{-17}\mvy{-80}Ca\size{15}\mv{-12,0}?\mv{3,0}\size{} lo\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}p\mvy{34}\n\mvx{-17}",r"\{      }\mvx{-17}\mvy{-80}Ca\size{20}\mv{-11,19}.\mv{-11,-17}^\mv{3,-2}\size{}u be\size{20}\mv{-18,3}´\mv{-2,-3}\size{}\mvy{34}\n\mvx{-17}",r"\{                      }\mvx{-17}\mvy{-80}Chi\size{20}\mv{-12,19}.\mv{3,-19}\size{} em Fujibayashi\mvy{34}\n\mvx{-17}",r"\{       }\mvx{-17}\mvy{-80}Co\size{20}\mv{-13,2}^\mv{4,-2}\size{} be\size{20}\mv{-18,3}´\mv{-2,-3}\size{}\mvy{34}\n\mvx{-17}",r"\{      }\mvx{-17}\mvy{-80}Co\size{20}\mv{-13,2}^\mv{4,-2}\size{} ga\size{20}\mv{-18,3}´\mv{-2,-3}\size{}i\mvy{34}\n\mvx{-17}",r"\{                               }\mvx{-17}\mvy{-80}Gia\size{20}\mv{-18,3}´\mv{-2,-3}\size{}o vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n chu\size{20}\mv{-12,-10},\mv{2,10}\size{} nhie\size{20}\mv{-11,19}.\mv{-11,-17}^\mv{3,-2}\size{}m lo\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}p A\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Gio\size{20}\mv{-11,19}.\mv{2,-19}\size{}ng no\size{20}\mv{-18,3}´\mv{-2,-3}\size{}i\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Ho\size{20}\mv{-11,19}.\mv{2,-19}\size{}c sinh 1\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Ho\size{20}\mv{-11,19}.\mv{2,-19}\size{}c sinh 2\mvy{34}\n\mvx{-17}",r"\{  }\mvx{-17}\mvy{-80}Me\size{20}\mv{-11,19}.\mv{2,-19}\size{}\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Mo\size{20}\mv{-11,19}.\mv{2,-19}\size{}i ngu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-15,2}`\size{28}\mv{-2,-15},\mv{-6,13}\size{}i\mvy{34}\n\mvx{-17}",r"\{                  }\mvx{-17}\mvy{-80}Ngu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-15,2}`\size{28}\mv{-2,-15},\mv{-6,13}\size{}i ba\size{20}\mv{-18,3}´\mv{-2,-3}\size{}n ha\size{20}\mv{-14,3}`\mv{5,-3}\size{}ng\mvy{34}\n\mvx{-17}",r"\{                 }\mvx{-17}\mvy{-80}Ngu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-15,2}`\size{28}\mv{-2,-15},\mv{-6,13}\size{}i d\size{20}\mv{-10,-2}-\mv{2,2}\size{}a\size{20}\mv{-14,3}`\mv{5,-3}\size{}n o\size{20}\mv{-13,2}^\mv{4,-2}\size{}ng\mvy{34}\n\mvx{-17}",r"\{            }\mvx{-17}\mvy{-80}Nha\size{20}\mv{-13,2}^\mv{4,-2}\size{}n vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Nu\size{20}\mv{-12,-1}~\size{28}\mv{-4,-12},\mv{-5,13}\size{} sinh 1\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Nu\size{20}\mv{-12,-1}~\size{28}\mv{-4,-12},\mv{-5,13}\size{} sinh 3\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Nu\size{20}\mv{-12,-1}~\size{28}\mv{-4,-12},\mv{-5,13}\size{} sinh A\mvy{34}\n\mvx{-17}",r"\{             }\mvx{-17}\mvy{-80}Nu\size{20}\mv{-12,-1}~\size{28}\mv{-4,-12},\mv{-5,13}\size{} sinh B\mvy{34}\n\mvx{-17}",r"\{           }\mvx{-17}\mvy{-80}Qua\size{15}\mv{-12,0}?\mv{3,0}\size{}n thu\size{28}\mv{-6,-13},\mv{-5,13}\size{}\mvy{34}\n\mvx{-17}",r"\{      }\mvx{-17}\mvy{-80}Ta\size{20}\mv{-14,3}`\mv{5,-3}\size{}i xe\size{20}\mv{-13,3}^\mv{-7,-4}´\mv{-8,1}\size{}\mvy{34}\n\mvx{-17}",r"\{                    }\mvx{-17}\mvy{-80}Ta\size{20}\mv{-13,3}^\mv{-7,-4}´\mv{-8,1}\size{}t ca\size{15}\mv{-12,0}?\mv{3,0}\size{} tha\size{20}\mv{-14,3}`\mv{5,-3}\size{}nh vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n\mvy{34}\n\mvx{-17}",r"\{                         }\mvx{-17}\mvy{-80}Tha\size{20}\mv{-14,3}`\mv{5,-3}\size{}nh vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n ho\size{20}\mv{-10,19}.\size{28}\mv{-6,-32},\mv{-6,13}\size{}p xu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}ng\mvy{34}\n\mvx{-17}",r"\{                           }\mvx{-17}\mvy{-80}Tha\size{20}\mv{-14,3}`\mv{5,-3}\size{}nh vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n ho\size{20}\mv{-10,19}.\size{28}\mv{-6,-32},\mv{-6,13}\size{}p xu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}ng 2\mvy{34}\n\mvx{-17}",r"\{                                }\mvx{-17}\mvy{-80}Tha\size{20}\mv{-14,3}`\mv{5,-3}\size{}nh vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n ho\size{20}\mv{-10,19}.\size{28}\mv{-6,-32},\mv{-6,13}\size{}p xu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}ng 2 & 3\mvy{34}\n\mvx{-17}",r"\{                           }\mvx{-17}\mvy{-80}Tha\size{20}\mv{-14,3}`\mv{5,-3}\size{}nh vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n ho\size{20}\mv{-10,19}.\size{28}\mv{-6,-32},\mv{-6,13}\size{}p xu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}ng 3\mvy{34}\n\mvx{-17}",r"\{            }\mvx{-17}\mvy{-80}Th\size{27}\mv{2,8}l\size{20}\mv{-15,-5}´\mv{-2,-3}\size{}nh gia\size{15}\mv{-12,0}?\mv{3,0}\size{}\mvy{34}\n\mvx{-17}",r"\{               }\mvx{-17}\mvy{-80}Th\size{27}\mv{2,8}l\size{20}\mv{-15,-5}´\mv{-2,-3}\size{}nh gia\size{15}\mv{-12,0}?\mv{3,0}\size{} 1\mvy{34}\n\mvx{-17}",r"\{               }\mvx{-17}\mvy{-80}Th\size{27}\mv{2,8}l\size{20}\mv{-15,-5}´\mv{-2,-3}\size{}nh gia\size{15}\mv{-12,0}?\mv{3,0}\size{} 2\mvy{34}\n\mvx{-17}",r"\{               }\mvx{-17}\mvy{-80}Th\size{27}\mv{2,8}l\size{20}\mv{-15,-5}´\mv{-2,-3}\size{}nh gia\size{15}\mv{-12,0}?\mv{3,0}\size{} 3\mvy{34}\n\mvx{-17}",r"\{                           }\mvx{-17}\mvy{-80}Toa\size{20}\mv{-14,3}`\mv{5,-3}\size{}n bo\size{20}\mv{-11,19}.\mv{-10,-17}^\mv{2,-2}\size{} kha\size{20}\mv{-18,3}´\mv{-2,-3}\size{}n th\size{27}\mv{2,8}l\size{20}\mv{-15,-5}´\mv{-2,-3}\size{}nh gia\size{15}\mv{-12,0}?\mv{3,0}\size{}\mvy{34}\n\mvx{-17}",r"\{                                   }\mvx{-17}\mvy{-80}Toa\size{20}\mv{-14,3}`\mv{5,-3}\size{}n the\size{20}\mv{-9,-15},\mv{-13,17}^\mv{3,-2}\size{} tha\size{20}\mv{-14,3}`\mv{5,-3}\size{}nh vie\size{20}\mv{-13,2}^\mv{4,-2}\size{}n ho\size{20}\mv{-10,19}.\size{28}\mv{-6,-32},\mv{-6,13}\size{}p xu\size{28}\mv{-6,-13},\mv{-5,13}\size{}o\size{20}\mv{-20,0}´\size{28}\mv{-7,-13},\mv{-6,13}\size{}ng\mvy{34}\n\mvx{-17}"]

# i=0
# for t in d:
# 	print('<'+f"{i:04d}"+'>\\{O'+t[3:]+' abc')
# 	i+=1

























	# Lay cac tu dangopedia va cac line to nho
import re
def findch(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
#Lay list file
from os import listdir
from os.path import isfile, join
listfile = [f for f in listdir('seenviet') if isfile(join('seenviet', f) )]
listfile = [f for f in listfile if 'SEEN' in f ]
for i in range(len(listfile)):
	listfile[i]=listfile[i][4:-4]

result=[]
for file in listfile:
	f=open('seens/SEEN'+file+' - Copy.org','r',encoding='utf-8')
	org=f.read().split('\n')
	f.close()
	f=open('seenviet/SEEN'+file+'.txt','r',encoding='utf-16')
	vn=f.read().split('\n')
	f.close()
	f=open('seens/SEEN'+file+' - Copy.utf','r',encoding='utf-8')
	utf=f.read().split('\n')
	f.close()
	for t in vn:
		if re.match(r"<[0-9][0-9][0-9][0-9]>", t[:6]) is not None and '\\size{}' in t:
			result+=[file+'\t'+t]
	for i in range(len(org)):
		if "farcall_with(9820, 3," in org[i] or "timeExC" in org[i]:
			res=org[i-1][4:]
			res2=org[i+1][4:]
			for v in vn:
				if res in v: vn1=v
			for v in vn:
				if res2 in v: vn2=v
			for u in utf:
				if res in u: utf1=u
			for u in utf:
				if res2 in u: utf2=u
			if org[i][23:-2] in vn1:
				print(file+'\t'+org[i]+'\t'+'dangopedia'+'\t'+vn1[:6]+'\t'+vn1+'\t'+vn2+'\t'+utf1+'\t'+utf2)
			elif "\\g" in vn1:
				print(file+'\t'+org[i]+'\t'+'tag g'+'\t'+vn1[:6]+'\t'+vn1+'\t'+vn2+'\t'+utf1+'\t'+utf2)
			else:
				print(file+'\t'+org[i]+'\t'+'\t'+vn1[:6]+'\t'+vn1+'\t'+vn2+'\t'+utf1+'\t'+utf2)


for t in result:
	print(t)














# import re
# writeorg="farcall_with(9820, 3, 'red string of fate')"
# writeorg = re.sub(r'farcall_with\(9820, 3, \'[A-Za-z ]+\'\)', "farcall_with(9820, 3, '')", writeorg)
# print(writeorg)






















# import re
# from itertools import groupby
# from operator import itemgetter
# def findch(s, ch):
#     return [i for i, ltr in enumerate(s) if ltr == ch]
# #Lay list file
# from os import listdir
# from os.path import isfile, join
# listfile = [f for f in listdir('seenviet') if isfile(join('seenviet', f) )]
# listfile = [f for f in listfile if 'SEEN' in f ]
# for i in range(len(listfile)):
# 	listfile[i]=listfile[i][4:-4]
# # listfile=['0414']

# for indexlistfile in range(len(listfile)):
# 	# Lay du lieu so sanh
# 	f=open('seens\\SEEN'+listfile[indexlistfile]+' - Copy.utf','r',encoding="utf-8")
# 	dataraw=f.read().split('\n')
# 	f.close()
# 	f=open('seenviet\\SEEN'+listfile[indexlistfile]+'.txt','r',encoding="utf-16")
# 	data=f.read().split('\n')
# 	dataviet=[]
# 	for t in data:
# 		if len(t)==0: continue
# 		if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
# 			dataviet=dataviet+[t]
# 	f.close()
# 	# Lay du lieu select va su ly
# 	f=open('seens\\SEEN'+listfile[indexlistfile]+' - Copy.org','r',encoding="utf-8")
# 	dataorg=f.read().split('\n')
# 	f.close()
# 	indexorg=[]
# 	org=[]
# 	# Thay dau "" bang dau  『』 , dau '' bang dau 「」
# 	dxl=[]
# 	for i in range(len(dataorg)):
# 		if "farcall_with(9820, 3" in dataorg[i]:
# 			if '#res<' in dataorg[i-1] and '#res<' in dataorg[i+1]:
# 				# for t in dataviet: 
# 				# 	if '<'+dataorg[i-1][5:9]+'>' in t: 
# 				# 		dxl+=[t]
# 				dxl+=[int(dataorg[i-1][5:9])]
# 				dxl+=[int(dataorg[i+1][5:9])]
# 			else:
# 				pass
# 	for i in range(len(dataorg)):
# 		if "farcall_with(9820, 3," in dataorg[i]:
# 			if '#res<' in dataorg[i-1] and '#res<' in dataorg[i+1]:
# 				dxl+=[int(dataorg[i-1][5:9])]
# 				dxl+=[int(dataorg[i+1][5:9])]
# 			else:
# 				pass
# 		if "timeExC(" in dataorg[i]:
# 			if '#res<' in dataorg[i-1] and '#res<' in dataorg[i+1]:
# 				dxl+=[int(dataorg[i-1][5:9])]
# 				dxl+=[int(dataorg[i+1][5:9])]
# 			else:
# 				pass
# 		# if "farcall_with(9820, 3," in dataorg[i]:
# 		# 	if '#res<' in dataorg[i-1] and '#res<' in dataorg[i+1]:
# 		# 		dxl+=[int(dataorg[i-1][5:9])]
# 		# 		dxl+=[int(dataorg[i+1][5:9])]
# 		# 	else:
# 		# 		pass
# 	dxlt=[]
# 	dxl=list(set(dxl))
# 	for k,g in groupby(enumerate(dxl),lambda x:x[0]-x[1]):
# 		group = (map(itemgetter(1),g))
# 		group = list(map(int,group))
# 		dxlt.append((group[0],group[-1]))
# 	def tdatav(taolao):
# 		for t in dataviet: 
# 			if '<'+'{0:04d}'.format(int(taolao))+'>' in t: 
# 				return t
# 	# print(dxl)
# 	for t in dxlt:
# 		t=list(t)
# 		for g in t:
# 			print(tdatav(g))
# 		print()