# # -*- coding: utf-8 -*-
#!/usr/bin/env python3
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
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

patchrldev='cd c: ;yes | cp -rf /cygdrive/z/CLANNAD/Seen.txt Seen.txt;'
bodem=0
bodem1=[]
bodem2=[]
a=[]
b=[]
	# Bảng mã nguồn để so sánh
ab=['đ','ó','ò','ỏ','õ','ọ','ô','ố','ồ','ổ','ỗ','ộ','ơ','ớ','ờ','ở','ỡ','ợ','á','à','ả','ã','ạ','â','ấ','ầ','ẩ','ẫ','ậ','ă','ắ','ằ','ẳ','ẵ','ặ','ê','ế','ề','ể','ễ','ệ','é','è','ẻ','ẽ','ẹ','ú','ù','ủ','ũ','ụ','ư','ứ','ừ','ử','ữ','ự','í','ì','ỉ','ĩ','ị','ý','ỳ','ỷ','ỹ','ỵ','Đ','Ó','Ò','Ỏ','Õ','Ọ','Ô','Ố','Ồ','Ổ','Ỗ','Ộ','Ơ','Ớ','Ờ','Ở','Ỡ','Ợ','Á','À','Ả','Ã','Ạ','Â','Ấ','Ầ','Ẩ','Ẫ','Ậ','Ă','Ắ','Ằ','Ẳ','Ẵ','Ặ','Ê','Ế','Ề','Ể','Ễ','Ệ','É','È','Ẻ','Ẽ','Ẹ','Ú','Ù','Ủ','Ũ','Ụ','Ư','Ứ','Ừ','Ử','Ữ','Ự','Í','Ì','Ỉ','Ĩ','Ị','Ý','Ỳ','Ỷ','Ỹ','Ỵ']
	#Bảng mã không dấu
bb=["d","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","e","e","e","e","e","e","e","e","e","e","e","u","u","u","u","u","u","u","u","u","u","u"," "," "," "," ","i","y","y","y","y","y","D","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","E","E","E","E","E","E","E","E","E","E","E","U","U","U","U","U","U","U","U","U","U","U","I","I","I","I","I","Y","Y","Y","Y","Y"]
	# Bảng mã cho headername (tên người nói trong script)
f=open('bangma cho headername.txt','r',encoding="utf-16")
bd=f.read().split('\n')
f.close()
# Lấy Bảng mã chuẩn
f=open('bangma new.txt','r',encoding="utf-16")
lines=f.read().split('\n')
for t in lines:
	try:
		a=a+[str(t.split('\t')[0])]
		b=b+[str(t.split('\t')[1])]
	except:
		pass
f.close()
# Lấy dangopedia word :))) ( chứa các từ dangopedia được dịch )
f=open('dangoword.txt','r',encoding="utf-16")
dangoword=f.read().split('\n')
dangoword = sorted(dangoword, key=len,reverse=True)
f.close()
# ------------------- Hết phần thiết lập các giá trị mặc định -----------------------------

# listfile=['0429']

for indexlistfile in range(len(listfile)):
	done=True

	# Lay du lieu
	f=open('seens\\SEEN'+listfile[indexlistfile]+' - Copy.utf','r',encoding="utf-8")
	dataraw=f.read().split('\n')
	f.close()
	f=open('seenviet\\SEEN'+listfile[indexlistfile]+'.txt','r',encoding="utf-16")
	data=f.read().split('\n')
	dataviet=[]				# Các line đã dịch
	dataviet = [ t for t in data if re.match("^<[0-9][0-9][0-9][0-9]>", t) is not None]
	# Lọc các lỗi dataviet: không cho chút thích vào patch text; 
	for d in range(len(dataviet)):
		dataviet[d]= re.sub(r'^(<[0-9]{4}>[^\n\/]*)(\/\/[^\n]*)$',r'\g<1>',dataviet[d])
		dataviet[d]= re.sub(r'^(<[0-9]{4}> \\\{\\\w{0,1}\{(A|B)\}\}) ',r'\g<1>',dataviet[d])
		dataviet[d]= re.sub(r'^(<[0-9]{4}> \\\{[^\{]{,20}\}) ',r'\g<1>',dataviet[d])
		dataviet[d]= re.sub(r'^(<[0-9]{4}> [^\n<]*)<',r'\g<1>\\<',dataviet[d])
		dataviet[d]= dataviet[d].replace('\\n','')
	f.close()
	f=open('seens\\SEEN'+listfile[indexlistfile]+' - Copy.org','r',encoding="utf-8")
	dataorg=f.read().split('\n') # Các line trong file .org ( file script chỉ cách hiển thị )
	f.close()
	f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','w',encoding="utf-8")
	f.write('\n'.join(dataorg)) # Reset file .org
	f.close()

	#  Xem bản HD và dịch có hợp nhau không. Nếu không, skip file đó
	datarawline=[]
	datarawline = [ t[:6] for t in dataraw if re.match("^<[0-9][0-9][0-9][0-9]>", t) is not None]
	if not datarawline==[t[:6] for t in dataviet]:
		done=False
		print("!!!LỖI!!!: File {} không trùng line giữa 2 bản HD: {} và việt: {}, số line lệch là: {}".format(listfile[indexlistfile],str(len(datarawline)),str(len(dataviet)),str(abs(len(dataviet)-len(datarawline)))))
		continue

	# Lấy các line chứa dangopedia trong file .org
	dangoline=[]
	for i in range(len(dataorg)):
		if "farcall_with(9820, 3" in dataorg[i]:
			dangoline+=[[dataorg[i-1][4:],dataorg[i][23:-2]]] # Mảng 2 chiều [so line trong utf, từ dangopedia trong file org]

	# Tìm các line select trong file .org (lựa chọn trong khi chơi)
	select_org=[]
	for t in dataorg:
		if 'select(' in t: 
			g=re.findall( r'\#res\<[0-9][0-9][0-9][0-9]\>', t)
			for i in range(len(g)):
				g[i]=g[i][5:-1]
			select_org=select_org+[g] 		# Mảng 2 chiều, chứa các line select

	# Tìm các line select_s trong file .org (chơi xỏ Fuuko pupupupuuuu... )
	fuko_org=[]
	for t in dataorg:
		if 'select_s(' in t: 
			g=re.findall( r'\#res\<[0-9][0-9][0-9][0-9]\>', t)
			for i in range(len(g)):
				g[i]=g[i][5:-1]
			fuko_org=fuko_org+[g] 		# Mảng 2 chiều, chứa các line select

	def xulyselect(selectline):
		# Lay cac lua chon cua ham select
		cacluachon=[]
		for t in select_org[[bla[0] for bla in select_org].index(selectline)]:
			for ib in range(len(dataviet)):
				try:
					if t == dataviet[ib][1:5]:
						cacluachon=cacluachon+[dataviet[ib]]
				except:
					pass
		# Viết các lựa chọn ảo <9xxx> trong file .utf (Kết quả trả về giá trị của hàm)
		writedau='<9'+selectline[1:]+'> '
		for t in cacluachon:
			c=t[7:]
			if len(c)<40:
				c+=' '*(40-len(c))
			for i in range(len(a)):
				c=c.replace(a[i],b[i])
			writedau=writedau+c+r'\r'
		writedau=writedau[:-2]+r'\mvy{-'+str(46*(len(cacluachon)+1))+'}\\r\\r'
		# Viết lại các line chứa lựa chọn thực (Kết quả đổ vào biến dataviet)
		for t in cacluachon:
			the=t[:9]+" "*(int(t[1:5])%5)
			for i in range(len(ab)):
				the=the.replace(ab[i],bb[i])			# Các lựa chọn thực cần viết không dấu
			dataviet[dataviet.index(t)]=the
		# Xử lý file org ( thêm #res<9xxx> để hiển thị các lựa chọn ảo)
		f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','r',encoding="utf-8")
		temporg=f.read().split('\n')
		f.close()
		for i in range(len(temporg)): 							# Lấy index dòng chứa select(#res<xxxx>, #res<xxxx>)
			if 'select(#res<'+selectline+'>,' in temporg[i]: 
				idong = i
		temporg.insert(idong,'#res<9'+selectline[1:]+'>')
		writeorg='\n'.join(temporg)
		f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','w',encoding="utf-8")
		f.write(writeorg)
		f.close()
		return writedau

	write=[]
	for t in dataraw:
		# skip các line trống không
		if len(t)==0: 
			write=write+['']
			continue

		if re.match(r"<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
			# Test xem có phải ngày tháng không -->Format: April 26 (Sat.)
			for g in dataviet: 
				if t[:6] in g: x=g
			if re.search(r"[a-zA-z]+ [0-9]+ \([a-zA-z]{3}\.\)", t):
				for i in range(len(ab)):
					x=x.replace(ab[i],bb[i])
				write=write+[x]
				continue

			# # Test xem có phải chơi xỏ Fuko không (select_s) CÁCH PATCH CŨ
			# if t[1:5] in [ fuko_org[i][0] for i in range(len(fuko_org))]:
			# 	fukoindex = [ fuko_org[i][0] for i in range(len(fuko_org))].index(t[1:5])
			# 	fukochoice=[]					# Chứa các lựa chọn chơi xỏ fuko
			# 	for fu in fuko_org[fukoindex]:
			# 		fukochoice+=[[g for g in dataviet if '<'+fu+'>' == g[:6] ][0]]
			# 		dataviet[dataviet.index(fukochoice[-1])] = [g for g in dataraw if '<'+fu+'>' == g[:6] ][0]
			# 		for q in range(len(a)):
			# 			fukochoice[-1]=fukochoice[-1].replace(a[q],b[q])
			# 	# viết lựa chọn thực vào phần trước
			# 	realchoice = ' \\n\\mv{159,-582}'
			# 	for ifu in range(len(fukochoice)):
			# 		realchoice+=fukochoice[ifu][7:]
			# 		if ifu < len(fukochoice)-1:
			# 			realchoice+='\\n\\mv{'+str(183+ifu*24)+',26}'
			# 	write[-1]=write[-1]+realchoice
			# 	# Chỉnh lại file 9070.org để patch Lv1 -Lv2 - Master
			# 	f=open('seens\\SEEN9070 - Copy.org','r',encoding="utf-8")
			# 	temporg=f.read()
			# 	temporg=temporg.replace("strS[1011] = 'Make her drink juice with her nose       '\nstrS[1012] = 'Put her around somewhere                 '\nstrS[1013] = 'Switch the person she\\'s talking to       '\nstrS[1014] = 'Switch the carving she\\'s holding         '","strS[1011] = '                                         '\nstrS[1012] = '                                         '\nstrS[1013] = '                                          '\nstrS[1014] = '                                          '")
			# 	f.close()
			# 	f=open('seens\\SEEN9070.org','w',encoding="utf-8")
			# 	f.write(temporg)
			# 	f.close()
			# 	# Thêm code patch file 9070.org
			# 	patchrldev+="cd c: ;yes | cp -rf /cygdrive/z/CLANNAD/Seen.txt Seen.txt; yes | cp -rf /cygdrive/z/CLANNAD/seens/SEEN9070.org SEEN9070.org;rlc -i /cygdrive/z/CLANNAD/GAMEEXEbbb.ini -f 1.5 -e utf8 SEEN9070.org; kprl -k Seen.txt 9070; kprl -a Seen.txt SEEN9070.TXT;rm /cygdrive/z/CLANNAD/Seen.txt; yes | cp -rf Seen.txt /cygdrive/z/CLANNAD;"

			# Test xem có phải chơi xỏ Fuko không (select_s) CÁCH MỚI
			if t[1:5] in [ fuko_org[i][0] for i in range(len(fuko_org))]:
				ifuko = [ fuko_org[i][0] for i in range(len(fuko_org))].index(t[1:5])
				for fu in fuko_org[ifuko]:
					iviet = [r[1:5] for r in dataviet].index(fu)
					dataviet[iviet]=[g for g in dataraw if g[1:5]==fu][0]
					dataviet[iviet]=dataviet[iviet].replace('<0013> Just leave it','<0013> Bo cuoc')
					dataviet[iviet]=dataviet[iviet].replace('<0005> Just leave it','<0005> Bo cuoc#s16###x22##?#s24###x90###y16##.#s28###x87###y2##^')
					dataviet[iviet]=dataviet[iviet].replace('<0010> Feed her Sanae-san\'s bread','<0010> Bat con be an banh m  cua Sanae-san #s28###x14###y-4##´#y2###x18##`#x15##´#x150###y1##´#y2###x188##`#x185##´#x252###y1##´#s27###x342###y8##l#s28###x343###y1##`#x397###y-17##,')
				# Chỉnh file org để patch chữ floating :)
				f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','r',encoding="utf-8")
				temporg=f.read()
				temporg=temporg.replace('You have mastered the "Make Fuko drink juice with her nose" skill!',"#x150Thanh thuc ky nang 『Uong nuoc ep bang lo mui』!#x180##い#x270###y4##ぇ#x330##げ#y0###x375##え#x480##ぉ#x488###y-4##ぃ#y0###x563###y-13##,#x578###y-13##,#x565###y-2##´#y0###x615##ぃ#x675##え#x673###y-4##い#x749###y0##ぉ#x748###y-4##う#y0###x792##う")
				temporg=temporg.replace('You have mastered the "Put Fuko somewhere randomly" skill!',"#x150##Thanh thuc ky nang 『Hoan doi vi tr 』!#x180##い#x270###y4##ぇ#x330##げ#y0###x375##え#x495##ぃ#x544###s20###y-4##-#y0###s###x555##ぉ#x557###y-4##ぅ#y4###x614##ぇ#y0###x675##お#x675##ぃ")
				temporg=temporg.replace('You have mastered the "Switch the person Fuko\\\'s talking to" skill!',"#x195##Thanh thuc ky nang 『Trao doi nguoi noi』!#s24###x226###y1##`#x319###y12##.#x378###y0##~#x420###y1##`#x418##´#x537###y0##´#x601###y2##^#x683###y-13##,#x698###y-13##,#x688###y-2##`#x746###y-1##´  #s24###x608###y-17##,#x588###y-3##-")
				temporg=temporg.replace('You have mastered the "Switch the carving Fuko\\\'s holding" skill!',"#x195##Thanh thuc ky nang 『Trao mieng go khac』!#s24###x226###y1##`#x319###y12##.#x378###y0##~#x420###y1##`#x418##´#x537###y0##´#x617###y1##^#x618###y-1##´#x692###y2##^#x693###y-3##~#x747###y1##´")
				temporg=temporg.replace('You have become a "Fuko User"!',"#x270##Da phong cap 『Fuuko Summoner』!#s24###x266###y2##-#x287###y1##~#x421###y2##^#x421###y1##´")
				f.close()
				f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','w',encoding="utf-8")
				f.write(temporg)
				f.close()
				# Chỉnh lại file 9070.org để patch Lv1 -Lv2 - Master
				f=open('seens\\SEEN9070 - Copy.org','r',encoding="utf-8")
				temporg=f.read()
				temporg=temporg.replace("strS[1011] = 'Make her drink juice with her nose       '\nstrS[1012] = 'Put her around somewhere                 '\nstrS[1013] = 'Switch the person she\\'s talking to       '\nstrS[1014] = 'Switch the carving she\\'s holding         '","strS[1011] = 'Uong nuoc bang mui#s28###x19###y3##^#x19###y-1##´#x114###y-13##,#x119###y-2##´#x130###y-13##,#x186###y-5##`#x186###y2##`#x183##´#x274###y3##~#x0###s###y0##                                         '\nstrS[1012] = 'Loi di#s28###x19###y2##^#x71###y-6##-#x0#s###y0##                                         '\nstrS[1013] = 'Doi nguoi noi chuyen#s24###x-2###y5##-#x120###y1##`#x311###y16##.#s28###x25###y-20##,#x18###y2##^#x112###y-13##,#x129##,#x184###y1##´#x308###y2##^#s###y0###x0##                                         '\nstrS[1014] = 'Trao mieng go khac#s28###x31###y1##´#x121###y2##^#x120###y-1##´#x207###y-2##~#x207###y3##^#x269###y1##´#s###y0###x0##                                         '")
				f.close()
				f=open('seens\\SEEN9070.org','w',encoding="utf-8")
				f.write(temporg)
				f.close()
				# Thêm code patch file 9070.org
				patchrldev+="cd c: ;yes | cp -rf /cygdrive/z/CLANNAD/Seen.txt Seen.txt; yes | cp -rf /cygdrive/z/CLANNAD/seens/SEEN9070.org SEEN9070.org;rlc -i /cygdrive/z/CLANNAD/GAMEEXEbbb.ini -f 1.5 -e utf8 SEEN9070.org; kprl -k Seen.txt 9070; kprl -a Seen.txt SEEN9070.TXT;rm /cygdrive/z/CLANNAD/Seen.txt; yes | cp -rf Seen.txt /cygdrive/z/CLANNAD;"

			# Test xem có phải lựa chọn không
			if t[1:5] in [ select_org[i][0] for i in range(len(select_org))]:
				write=write+[xulyselect(t[1:5])]
				for g in dataviet: 
					if t[:6] in g: x=g
				write=write+[x]
				continue
			# Thế lại bản dịch vào x (do dataviet đã thay đổi)
			for g in dataviet: 
				if t[:6] in g: x=g

			# Test xem có chữ to nhỏ trong hội thoại không
			m= re.findall( r'\\size{[^\{]+}', x)
			if len(m)!=0:
				m=m[0][6:-1]
				if '\\size{}' in x:
					text=max(re.findall( r'\\size{[^\{]+}(.*)\\size{}', x))
					temptext=text
					for i in range(len(a)):
						text=text.replace(a[i],b[i])
					text=text.replace(u'\xa0',' ')
					text=text.replace('18',m+'/2')
					x=x.replace(temptext,text)
				else:
					text=x[x.find(m)+1+len(m):]
					temptext=text
					for i in range(len(a)):
						text=text.replace(a[i],b[i])
					text=text.replace(u'\xa0',' ')
					text=text.replace('18',m+'/2')
					x=x.replace(temptext,text)


			# Xử lý dangopedia
			if t[:6] in [bla[0] for bla in dangoline]:
				idango=[bla[0] for bla in dangoline].index(t[:6])
				# Xét xem có tag \g , \c chưa
				if not ('\\g' in x or r'\\c' in x):
					# Nếu dịch có từ trong dangoword hoặc trong file org thì đặt tag g cho nó
					if any(k in x for k in dangoword+[dangoline[idango][1]]):
						for dan in (dangoword+[dangoline[idango][1]]):
							if not ('\\g' in x or 'intG[1806]' in x):
								x=x.replace(dan,'\\g{'+dan+r'}={tag danh tu dong}')
					else:
					# Nếu không có thì chép từ file org sang và in để cảnh báo lỗi
						print('Có thể lỗi dango\tSEEN'+listfile[indexlistfile]+'\t'+x+'\t'+dangoline[idango][1])
						if '\\ \\' in x[-5:]:
							x=x[:-3]+' '
						x=x+'\\g{'+dangoline[idango][1]+r'}={tag danh tu dong}'
				# Nếu cuối dòng có dấu cách và dòng sau đó không có dấu cách thì bảo vệ nó
				if x[-1]==' ' and dataviet[[p[:6] for p in dataviet].index(t[:6])+1][6:9] != ' \\ ':
					x=x[:-1]+"\\ \\"
				# Xóa tất cả từ dangopedia trong file org
				f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','r',encoding="utf-8")
				temporg=f.read().split('\n')
				for bla in range(len(temporg)):
					if re.search(r'^farcall_with\(9820, 3, \'[^\']+\'\)$', temporg[bla]):
						temporg[bla]="farcall_with(9820, 3, '')"
				writeorg='\n'.join(temporg)
				f=open('seens\\SEEN'+listfile[indexlistfile]+'.org','w',encoding="utf-8")
				f.write(writeorg)
				f.close()

			# # Bỏ tag \size = Bỏ chữ to nhỏ
			# x=re.sub(r"\\size{[^\!]{0,11}}", "", x)

			# Patch tagname / headername
			m= re.findall( r'\\{[^\{]+}', x)
			if len(m)!=0:
				m=m[0][2:-1]					# Chứa tag name
				if any(word in m for word in ab):
					lch=len(m)
							### Cách tính căn lề mới
					if lch<11:
						mvx=6-30 + 15*4 - 15*lch//2
					elif lch%2==0:
						mvx=6-30 + 15*4 - 15*10//2
					elif lch%2==1:
						mvx=6-30 + 15*4 - 15*10//2+7
					mv=''.join([mao+'\\mvx{1}' for mao in m])
							### Cách tính căn lề cũ
					# if lch<9: 
					# 	mvx=int(27-7.5*(lch-1))	# Tính căn lề trái
					# else:
					# 	if lch%2==0: 
					# 		mvx=int(27-8*8)
					# 	else: 
					# 		mvx=int(27-8*8+8)
					# mv=m
					for im in range(len(ab)):
						mv=mv.replace(ab[im],bd[im])
					x=x.replace('\\{'+m+'}','\\{'+' '*lch+'}'+'\\mv{'+str(mvx)+', -78}\\size{30}'+mv+'\\size{}\\mvx{'+str(0-mvx)+'}\\mvy{32}\\r')

			





			# Hightlight cho tag \g
			x=re.sub(r"\\g{([^}]+)}={[^}]+}", r"\\c{intG[1806]}\1\\c{}", x)

			# print(x)

			# Chuyen dau theo rulset vao x
			for i in range(len(a)):
				x=x.replace(a[i],b[i])
			x=x.replace(u'\xa0',' ')
			write=write+[str(x)]
 
		else:
			write=write+[t]
		# print(write[-1])
	write='\n'.join(write)

	# Ghi file
	f=open('seens\\SEEN'+listfile[indexlistfile]+'.utf','w',encoding="utf-8")
	f.write(write)
	f.close()

	# Ghi ra man hinh lenh patch rldev
	if done:
		patchrldev+='yes | cp -rf /cygdrive/z/CLANNAD/seens/SEEN'+listfile[indexlistfile]+r'.utf SEEN'+listfile[indexlistfile]+r'.utf;'
		patchrldev+='yes | cp -rf /cygdrive/z/CLANNAD/seens/SEEN'+listfile[indexlistfile]+r'.org SEEN'+listfile[indexlistfile]+r'.org;'
		patchrldev+='rlc -i /cygdrive/z/CLANNAD/GAMEEXEbbb.ini -f 1.6 -e utf8 SEEN'+listfile[indexlistfile]+r'.org;'
		patchrldev+='kprl -k Seen.txt '+listfile[indexlistfile]+';'
		patchrldev+='kprl -a Seen.txt SEEN'+listfile[indexlistfile]+r'.TXT;'
	


	patchrldev+='rm /cygdrive/z/CLANNAD/Seen.txt; yes | cp -rf Seen.txt /cygdrive/z/CLANNAD;'

print(patchrldev)

#copy lenh patch rledv vao clipboard (Neu da cai pyperclip) 
try:
	import pyperclip
	pyperclip.copy(patchrldev)
except:
	print('pyperclip not installed')
