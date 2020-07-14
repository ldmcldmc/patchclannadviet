import re
from os import listdir
from os.path import isfile, join
import time
import sys
patha=sys.argv[0]
patha=patha[:0-len(patha.split('.')[-1])-14]
print(sys.argv[0])
print(patha)
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
	print('done '+ file)
print('done')




















# import re
# from os import listdir
# from os.path import isfile, join
# import time
# import sys
# patha=sys.argv[0]
# patha=patha[:0-len(patha.split('.')[-1])-14]
# files = [f for f in listdir(patha) if isfile(join(patha, f)) and f[-4:].lower()=='.txt']
# files=['SEEN0415.txt']
# for file in files:
# 	f=open(file,'r',encoding='utf-16')
# 	content = f.read().split('\n')
# 	f.close()
# 	res=[]
# 	ress=[]
# 	for i in range(len(content)):
# 		if re.match(r"<[0-9][0-9][0-9][0-9]>", content[i]) is not None:
# 			res+=[content[i]]
# 		if len(content[i])>1:
# 			if content[i][0]=='<':
# 				ress+=[content[i]]

# for i in range(len(ress)):
# 	try:
# 		print(res[i]+'\t'+ress[i])
# 	except:
# 		print('\t'+ress[i])





