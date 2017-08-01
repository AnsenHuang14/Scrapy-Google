# -*- coding: utf-8 -*-. 
import sys
import pandas as pd 

def p(*args):
	fileindex1 = int(args[0][1])
	fileindex2 = int(args[0][2])
	num_10 = 0
	num_50 = 0
	num_100 = 0
	num_500 = 0 
	num_1000 = 0
	num_over1000 = 0
	total = 0
	with open('.\\PkgNameByNum\\_10.txt', 'wb') as f:
		for i in xrange(fileindex1,fileindex2+1):
			if i<=9:
				filename = 'part-0000'+str(i)	
			elif i>9 and i<=99 :
				filename = 'part-000'+str(i)
			else :
				filename = 'part-00'+str(i)			
			df = pd.read_csv(".\\PkgNameFile\\"+filename,sep='\t',header=None)
			# print len(df)
			for j in xrange(len(df)):
				total+=1
				num = df.loc[j,1]
				if num<=10: 
					num_10+=1
					f.write(df.loc[j,0])
					f.write('\n')
				elif num>10 and num<=50 : 
					num_50+=1
				elif num>50 and num<=100: 
					num_100+=1
				elif num>100 and num<=500:
					num_500+=1
				elif num>500 and num<=1000:
					num_1000+=1
				elif num>1000 :
					num_over1000+=1
					
			print i,total,num_10,num_50,num_100,num_500,num_1000,num_over1000
	pass

def read_url(path=''):
    start_urls = list()
    with open(path, 'rb') as f:
        start_urls.append(f.read())
    start_urls = start_urls[0].split('\n')
    return start_urls
def read(path=''):
	df = pd.read_csv(path,sep='\t',header=None)
	print df.loc[:,0]

if __name__ == '__main__':
	# p(sys.argv)
	print read('.\\PkgNameByNum\\10_50_2.txt')