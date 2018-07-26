import os,sys #needed to run  bash scripts
import openpyxl #needed to mess with excel
import time #needed to make a pause
import subprocess #needed to make the program fun a shell script within the python environment
import re #regular expressions

wb = openpyxl.load_workbook('testfile.xlsx') #change file name to whatever
ws = wb['Sheet1']
ss = wb['Sheet2']

value = 2
letter = 'A'

ip = 'i'

print_value = str(value)
cell = letter+print_value

while ws[cell].value: #basically, while the cell has an obtainable value, do this
	print_value = str(value)
	cell = letter+print_value
	ip = str(ws[cell].value)
	print(ip)
	if ws[cell].value is None: #if there is no obtainable information
		break
	ip_report = os.system('./blcheck ' + ip)
	child = subprocess.Popen(ip_report,shell=True,stdout=subprocess.PIPE)
	output = str(child.communicate()[0])
	output = re.findall(r'\d+',output)
	print(int(output[0]))
	value += 1