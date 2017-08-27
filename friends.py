import os
import sys
import random
import dircache

def getRandomFolderPath():

	folder=False
	temp=None
	while not folder:
		temp=random.choice(dircache.listdir("."))
		if not os.path.isdir(temp):
			continue
		
		x=[name for name in os.listdir(temp) if os.path.isfile(os.path.join(temp,name))]
		number=len(x)
			
		os.chdir(temp)
		if number >=10 or (number in range(1,3)):
				
			return temp
		
		
		return temp+"/"+getRandomFolderPath()



folderpath=getRandomFolderPath()
temp=random.choice(os.listdir(".") )

filters=[".db",".jpg",".png",".tiff",".jpeg",".txt",".srt",".SRT",".TXT","README"]

while (any([x in temp for x in filters])):
	temp=random.choice(os.listdir(".") )
temp=os.path.abspath(temp)

temp=temp.replace(' ','\ ')
temp=temp.replace("'","\\'")
temp=temp.replace('"','\\"')
temp=temp.replace('(','\(')
temp=temp.replace(')','\)')
print temp


finalcommand="vlc "+temp
os.system(finalcommand)



