import virustotal2
import os
import time
import openpyxl


wb = openpyxl.load_workbook('testfile.xlsx')
ws = wb['Sheet1']
ss = wb['Sheet2']

value = 2
letter = 'A'
vt = virustotal2.VirusTotal2("1fd2648228dde4b02c2438110543db84030033c0e4d9addd12a993b1c126d347")

n = 0
ip = 'i'

while ip is not None:
	while n < 4:
		print_value = str(value)
		cell = letter+print_value
		ip = str(ws[cell].value)
		print ip
		ip_report = vt.retrieve(ip, raw = True)
		new_cell = 'B'+print_value
		ws[new_cell].value = ip_report
		n += 1
		value += 1

	print n
	time.sleep(60)
	n = 0


wb.save('example_testfile.xlsx')
