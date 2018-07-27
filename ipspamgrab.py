import requests
import re
import openpyxl
url = "http://www.ipspamlist.com/public_feeds.csv"
r = requests.get(url, allow_redirects=True)
open('ipspamlist.csv', 'wb').write(r.content)

f = open("ipspamlist.csv", "r")
#print("Name of file: ", f.name)

fullList = f.readlines()
badipList = ""

for i in range(len(fullList)):
	fullList[i]=fullList[i].strip()										#strip all the newlines
	newStr = re.findall(r'[0-9]+(?:\.[0-9]+){3}', fullList[i])			#finds all IP's thru regex
	if(i+1) == len(fullList):
		badipList += str(newStr)
	else:
		badipList += str(newStr)+ "\n"										#add some more newlines cuz yolo



badipList = badipList.replace("[", "")
badipList = badipList.replace("'", "")
badipList = badipList.replace("]", "")									#strip all the garbo from the list items


wb = openpyxl.load_workbook("example_testfile.xlsx")
ws = wb.active
ws = wb["Sheet1"]
col = ws["A"]

counter = 0

badip = []
badip = badipList.split()
foundIp = []
for i in range(len(col)):
	for j in range(len(badip)):
		if badip[j] == col[i].value:	#this has been tested as working
			foundIp.append(badip[j])


print(foundIp)							#this list will hold all matched IP's				


f.close()
