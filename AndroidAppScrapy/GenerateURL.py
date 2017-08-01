# -*- coding: utf-8 -*-. 
import sys
import pandas as pd 

def ReadLangList(path='langlist.txt'):
	return pd.read_csv(path,header=None).loc[:,0].tolist()
def p(*args):
	path = args[0][1]
	fileindex1 = int(args[0][2])
	fileindex2 = int(args[0][3])
	for lang in ReadLangList():
		with open('.\\URL\\'+lang+'.txt', 'wb') as f:
			for i in xrange(fileindex1,fileindex2+1):
				print lang,i
				if i<=9:
					filename = 'part-0000'+str(i)	
				elif i>9 and i<=99 :
					filename = 'part-000'+str(i)
				else :
					filename = 'part-00'+str(i)	
				
				df = pd.read_csv(path+filename,sep='\t',header=None)
				# print len(df)
				for j in xrange(len(df)):
					pkg_name = df.loc[j,0]
					content = 'https://play.google.com/store/apps/details?id='+pkg_name+'&hl='+lang
					f.write(content)
					f.write('\n')
	pass

def gen(*args):
	path = args[0][1]
	for lang in ReadLangList():
		print lang
		with open('.\\URL\\'+lang+'.txt', 'wb') as f:
			df = pd.read_csv(path,sep='\t',header=None)
			# print len(df)
			for j in xrange(len(df)):
				pkg_name = df.loc[j,0]
				content = 'https://play.google.com/store/apps/details?id='+pkg_name+'&hl='+lang
				f.write(content)
				f.write('\n')
	pass

if __name__ == '__main__':
	gen(sys.argv)