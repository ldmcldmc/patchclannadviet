	# Lay tat ca file seen từ Baka-tsuki theo route
route='5' # Sửa Rote ở đây, thích route nào thì đánh số thứ tự đầu của route đó
import re, requests
from bs4 import BeautifulSoup
# Lay list file
from os import listdir
from os.path import isfile, join
listfile = [f for f in listdir('seens') if isfile(join('seens', f) )]
listfile = [f for f in listfile if f[-1]=='g' and f[4]==str(route) and 'Copy' not in f]
for i in range(len(listfile)):
	listfile[i]=listfile[i][4:-4]
listfile=list(set(listfile))
for file in listfile:
	# if file!='7600':continue
	# Lay du lieu qua mang
	try:
		link = requests.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file)
		soup=BeautifulSoup(link.content,'lxml')
		data=soup.find('pre').text.split('\n')
	except :
		try:
			print(file)
			link = requests.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file+'P1')
			soup=BeautifulSoup(link.content,'lxml')
			data=soup.find('pre').text.split('\n')
			try:
				idriver=2
				while True:
					link = requests.get('https://www.baka-tsuki.org/project/index.php?title=Clannad_VN:SEEN'+file+'P'+str(idriver))
					soup=BeautifulSoup(link.content,'lxml')
					data+=soup.find('pre').text.split('\n')
					idriver+=1
			except:
				pass
		except:
			print(file+'       !!!!!!!!')
			data=[]
			continue
	f=open('seenviet\\SEEN'+file+'.txt','w',encoding='utf-16')
	f.write('\n'.join(data))
	f.close()