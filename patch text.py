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
# listfile=['0414']

bodem=0
bodem1=[]
bodem2=[]

# lay bang ma
a=[]
b=[]
	# Bang ma nguon so sanh
ab=['đ','ó','ò','ỏ','õ','ọ','ô','ố','ồ','ổ','ỗ','ộ','ơ','ớ','ờ','ở','ỡ','ợ','á','à','ả','ã','ạ','â','ấ','ầ','ẩ','ẫ','ậ','ă','ắ','ằ','ẳ','ẵ','ặ','ê','ế','ề','ể','ễ','ệ','é','è','ẻ','ẽ','ẹ','ú','ù','ủ','ũ','ụ','ư','ứ','ừ','ử','ữ','ự','í','ì','ỉ','ĩ','ị','ý','ỳ','ỷ','ỹ','ỵ','Đ','Ó','Ò','Ỏ','Õ','Ọ','Ô','Ố','Ồ','Ổ','Ỗ','Ộ','Ơ','Ớ','Ờ','Ở','Ỡ','Ợ','Á','À','Ả','Ã','Ạ','Â','Ấ','Ầ','Ẩ','Ẫ','Ậ','Ă','Ắ','Ằ','Ẳ','Ẵ','Ặ','Ê','Ế','Ề','Ể','Ễ','Ệ','É','È','Ẻ','Ẽ','Ẹ','Ú','Ù','Ủ','Ũ','Ụ','Ư','Ứ','Ừ','Ử','Ữ','Ự','Í','Ì','Ỉ','Ĩ','Ị','Ý','Ỳ','Ỷ','Ỹ','Ỵ']
	#Bang ma khong dau
bb=["d","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","e","e","e","e","e","e","e","e","e","e","e","u","u","u","u","u","u","u","u","u","u","u"," "," "," "," ","i","y","y","y","y","y","D","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","E","E","E","E","E","E","E","E","E","E","E","U","U","U","U","U","U","U","U","U","U","U","I","I","I","I","I","Y","Y","Y","Y","Y"]
	# Bang ma cho headername
f=open('bangma cho headername.txt','r',encoding="utf-16")
bd=f.read().split('\n')
f.close()

# Bang ma chuan
f=open('bangma.txt','r',encoding="utf-16")
lines=f.read().split('\n')
for t in lines:
	try:
		a=a+[str(t.split('\t')[0])]
		b=b+[str(t.split('\t')[1])]
	except:
		pass
f.close()
	# danganronpa word :)))
f=open('dangoword.txt','r',encoding="utf-16")
dangoword=f.read().split('\n')
f.close()





patchrldev='cd c: ;yes | cp -rf /cygdrive/z/CLANNAD/Seen.txt Seen.txt;'

for indexlistfile in range(len(listfile)):
	done=True

	# Lay du lieu
	f=open('seens\\SEEN'+listfile[indexlistfile]+' - Copy.utf','r',encoding="utf-8")
	dataraw=f.read().split('\n')
	f.close()
	f=open('seenviet\\SEEN'+listfile[indexlistfile]+'.txt','r',encoding="utf-16")
	data=f.read().split('\n')
	dataviet=[]
	for t in data:
		if len(t)==0: continue
		if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
			dataviet=dataviet+[t]
	f.close()
	f=open('seens\\SEEN'+listfile[indexlistfile]+' - Copy.org','r',encoding="utf-8")
	dataorg=f.read().split('\n')
	f.close()

	#xet su trung nhau 2 file
	datarawline=[]
	for t in dataraw:
		if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
			datarawline+=[t[:6]]
	if not datarawline==[t[:6] for t in dataviet]:
		done=False
		print("!!!LOI!!!: File "+listfile[indexlistfile]+' khong trung line   so line: HD:'+str(len(datarawline))+', viet:'+str(len(dataviet)))
		continue

	# Tim cac line dangopedia
	dangoline=[]
	dangow=[]
	for i in range(len(dataorg)):
		if "farcall_with(9820, 3" in dataorg[i]:
			dangow+=[dataorg[i]]
			dangoline+=[dataorg[i-1][4:]]

	# Tim cac line select
	indexorg=[]
	org=[]
	for t in dataorg:
		if 'select(' in t: 
			g=re.findall( r'\#res\<[0-9][0-9][0-9][0-9]\>', t)
			for i in range(len(g)):
				g[i]=g[i][5:-1]
			indexorg=indexorg+[dataorg.index(t)]
			org=org+[g]

	def xulyselect(st,dong):
		cacluachon=[]
		for i in range(len(org)):
			if st == org[i][0]:
				# Lay cac lua chon cua ham select
				for t in org[i]:
					for ib in range(len(dataviet)):
						try:
							if t == dataviet[ib][1:5]:
								cacluachon=cacluachon+[dataviet[ib]]
						except:
							pass
				# Them dong <9xxx> vao file org
				if not dataorg[indexorg[i]-1]=='#res<9'+st[1:]+'>':
					indexorg[i]=indexorg[i]+i
					dataorg.insert(indexorg[i],'#res<9'+st[1:]+'>')

		# Viet vao file org
		f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','w',encoding="utf-8")
		writeorg='\n'.join(dataorg)
		writeorg = re.sub(r'farcall_with\(9820, 3, \'[A-Za-z ]+\'\)', "farcall_with(9820, 3, '')", writeorg)
		f.write(writeorg)
		f.close()

		# Viet cac lua chon vao <9xxx>
		writedau='<9'+st[1:]+r'> '
		for t in cacluachon:
			c=t[7:]
			if len(c)<40:
				c+=' '*(40-len(c))
			for i in range(len(a)):
				c=c.replace(a[i],b[i])
			writedau=writedau+c+r'\n'
		writedau=writedau[:-2]+r'\mvy{-'+str(46*(len(cacluachon)+1))+'}\\r\\r'

		# Viet dau cach vao cac lua chon thuc
		for t in cacluachon:
			the=t[:8]+" "*(len(t)-7)
			for i in range(len(ab)):
				the=the.replace(ab[i],bb[i])
			dataviet[dataviet.index(t)]=the
		return writedau


	#Main
	# so sanh va the chu
	write=[]
	for t in dataraw:
		# skip line trong khong
		if len(t)==0: 
			write=write+['']
			continue

		if re.match(r"<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
			# test xem co phai ngay thang hay khong -->Format: April 26 (Sat.)
			for g in dataviet: 
				if t[:6] in g: x=g
			if re.search(r"[a-zA-z]+ [0-9]+ \([a-zA-z]{3}\.\)", t):
				for i in range(len(ab)):
					x=x.replace(ab[i],bb[i])
				write=write+[x]
				continue

			# test xem co phai select khong
			if t[1:5] in [ org[i][0] for i in range(len(org))]:
				write=write+[xulyselect(t[1:5],t)]
				for g in dataviet: 
					if t[:6] in g: x=g
				write=write+[x]
				continue

			# Tim dong tu dataviet thay vao x
			for g in dataviet: 
				if t[:6] in g: x=g

			# Bo tag \size = Bo chu to nho
			x=re.sub(r"\\size{[^\!]+}", "", x)

			# Patch tagname / headername
			m= re.findall( r'\\{[^\{]+}', x)
			if len(m)!=0:
				m=m[0][2:-1]
				if any(word in m for word in ab):
					lch=len(m)
					if lch<9: 
						mvx=int(27-7.5*(lch-1))
					else:
						if lch%2==0: 
							mvx=int(27-8*8)
						else: 
							mvx=int(27-8*8+8)
					mv=m
					for im in range(len(ab)):
						mv=mv.replace(ab[im],bd[im])
					x=x.replace('\\{'+m+'}','\\{'+' '*(lch)+'}'+'\\mv{'+str(mvx)+', -78}\\size{30}'+mv+'\\size{}\\mvx{'+str(0-mvx)+'}\\mvy{32}\\n')

			# Boi mau cho tag \g
			x=re.sub(r"\\g{([^\{]+)}={[^\{]+}", "zzzazzgzzc\{intG[1806]}\\1zzzazzgzzc{}", x)
			x=x.replace('zzzazzgzz','\\')
			# Xu ly dangopedia
			if t[:6] in dangoline:
				for word in dangoword:
					x=x.replace(word,r'\c{intG[1806]}'+word+r'\c{}')
				if r'\c{intG[1806]}' not in x:
					# print(listfile[indexlistfile]+'\t'+dangow[dangoline.index(t[:6])]+'\t'+x)
					word = dangow[dangoline.index(t[:6])].replace("farcall_with(9820, 3, '","")[:-2]
					x=x+r'\c{intG[1806]}'+word+r'\c{}'

			# Chuyen dau theo rulset vao x
			for i in range(len(a)):
				x=x.replace(a[i],b[i])
			x=x.replace(u'\xa0',' ')
			write=write+[str(x)]
		else:
			write=write+[t]
	write='\n'.join(write)

	# Ghi file
	f=open('seens\\SEEN'+listfile[indexlistfile]+'.utf','w',encoding="utf-8")
	f.write(write)
	f.close()

	# Ghi ra man hinh lenh patch rldev
	if done:
		patchrldev+=' yes | cp -rf /cygdrive/z/CLANNAD/seens/SEEN'+listfile[indexlistfile]+r'.utf SEEN'+listfile[indexlistfile]+r'.utf; yes | cp -rf /cygdrive/z/Games/CLANNAD.HD.Edition/CLANNAD.HD.Edition/seens/SEEN'+listfile[indexlistfile]+r'.org SEEN'+listfile[indexlistfile]+r'.org;rlc -i /cygdrive/z/Games/CLANNAD.HD.Edition/CLANNAD.HD.Edition/GAMEEXEbbb.ini -f 1.5 -e utf8 SEEN'+listfile[indexlistfile]+r'.org; kprl -k Seen.txt '+listfile[indexlistfile]+r'; kprl -a Seen.txt SEEN'+listfile[indexlistfile]+r'.TXT;'
	patchrldev+='rm /cygdrive/z/CLANNAD/Seen.txt; yes | cp -rf Seen.txt /cygdrive/z/CLANNAD;'
print(patchrldev)

#copy lenh patch rledv vao clipboard (Neu da cai pyperclip) 
try:
	import pyperclip
	pyperclip.copy(patchrldev)
except:
	pass