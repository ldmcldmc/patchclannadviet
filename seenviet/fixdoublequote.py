import re
def findch(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
#Lay list file
from os import listdir
from os.path import isfile, join
listfile = [f for f in listdir('../seenviet') if isfile(join('../seenviet', f) )]
listfile = [f for f in listfile if 'SEEN' in f ]
for i in range(len(listfile)):
	listfile[i]=listfile[i][4:-4]
# listfile=['0414']

a=[]
b=[]

f=open('replace.txt','r',encoding="utf-16")
lines=f.read().split('\n')
for t in lines:
	a+=[str(t.split('\t')[0])]
	b+=[str(t.split('\t')[1])]
f.close()
dapatch=[]

printscr=[]

patchrldev='yes | cp -rf /cygdrive/z/Games/CLANNAD.HD.Edition/CLANNAD.HD.Edition/Seen.txt Seen.txt;'
for indexlistfile in range(len(listfile)):
	# if indexlistfile in [1,2,3,5]:continue
	# Lay du lieu so sanh
	f=open('../seenviet\\SEEN'+listfile[indexlistfile]+'.txt','r',encoding="utf-16")
	data=f.read().split('\n')
	datavgoc=[]
	for t in data:
		if len(t)==0: continue
		if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
			datavgoc+=[t]
	f.close()
	datav=[]
	for t in datavgoc:
		x=t
		# Replace cac file dac biet
		for m in range(len(a)):
			if b[m] in x:
				x=x.replace(b[m],a[m])
				dapatch+=[b[m]+'\t'+a[m]]
		if not len(re.findall(r'\"',x))==0:
			if (len(re.findall(r'\"',x))%2==0):
				ngd=findch(x,'\"')
				for i in range(len(ngd)):
					if i%2==0:
						x=x[:ngd[i]]+'『'+x[ngd[i]+1:]
					else:
						x=x[:ngd[i]]+'』'+x[ngd[i]+1:]
			else:
				printscr+=[listfile[indexlistfile]+'\t'+x]
		if not len(re.findall(r'\'',x))==0:
			if (len(re.findall(r'\'',x))%2==0):
				ngd=findch(x,'\'')
				for i in range(len(ngd)):
					if i%2==0:
						x=x[:ngd[i]]+'「'+x[ngd[i]+1:]
					else:
						x=x[:ngd[i]]+'」'+x[ngd[i]+1:]
			else:
				print(listfile[indexlistfile]+'\t'+x)
		x=x.replace("You「re Rollin」","You're Rolling")
		datav+=[x]
	if len(datav)!=len(datavgoc): print(len(datav))
	data='\n'.join(data)
	for i in range(len(datav)):
		data=data.replace(datavgoc[i],datav[i])
	# Ghi file
	f=open('../seenviet\\SEEN'+listfile[indexlistfile]+'.txt','w',encoding="utf-16")
	f.write(data)
	f.close()


# print('aaaaaaaaaaaaa')
# for t in dapatch:
# 	b.remove(t.split('\t')[0])
# print(len(dapatch))
# for t in b:
# 	print(t)








printscr=list(set(printscr))

for t in printscr:
	print(t)



































# import re, distance
# def findch(s, ch):
#     return [i for i, ltr in enumerate(s) if ltr == ch]
# #Lay list file
# from os import listdir
# from os.path import isfile, join
# listfile = [f for f in listdir('../seenviet') if isfile(join('../seenviet', f) )]
# listfile = [f for f in listfile if 'SEEN' in f ]
# for i in range(len(listfile)):
# 	listfile[i]=listfile[i][4:-4]
# # listfile=['0414']

# a=[]
# b=[]

# f=open('replace.txt','r',encoding="utf-16")
# lines=f.read().split('\n')
# for t in lines:
# 	a+=[str(t.split('\t')[0])]
# 	b+=[str(t.split('\t')[1])]
# f.close()
# dapatch=[]

# datavgoc=[]
# patchrldev='yes | cp -rf /cygdrive/z/Games/CLANNAD.HD.Edition/CLANNAD.HD.Edition/Seen.txt Seen.txt;'
# for indexlistfile in range(len(listfile)):
# 	# if indexlistfile in [1,2,3,5]:continue
# 	# Lay du lieu so sanh
# 	f=open('../seenviet\\SEEN'+listfile[indexlistfile]+'.txt','r',encoding="utf-16")
# 	data=f.read().split('\n')
# 	datavgoc=[]
# 	for t in data:
# 		if len(t)==0: continue
# 		if re.match("<[0-9][0-9][0-9][0-9]>", t[:6]) is not None:
# 			datavgoc+=[[t[1:5],t]]
# 	f.close()

# result=[]
# for t in a:
# 	res=[100000,'0000','']
# 	for g in datavgoc:
# 		r=distance.levenshtein(t, g[1])
# 		if r<=res[0]:
# 			res=[r]+g
# 			print('change')
# 	result+=[res]
# 	print('done'+t+str(g))

# for t in result:
# 	print('\t'.join(t))