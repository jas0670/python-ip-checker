import openpyxl
import requests
from requests.auth import HTTPBasicAuth

wb = openpyxl.load_workbook('example_testfile.xlsx')
ws = wb['Sheet2']

value = 2
letter = 'A'

ip = 'i'

print_value = str(value)
cell = letter+print_value

while ws[cell].value:
	print_value = str(value)
	cell = letter+print_value
	ip = str(ws[cell].value)
	print(ip)
	if ws[cell].value is None:
		break
	response = requests.get("https://api.xforce.ibmcloud.com/ipr/history/"+ip, auth=HTTPBasicAuth('f0d4525f-a4da-42ef-ba45-17d82d812531', '92209c34-896d-4f08-b787-723f2b71b336'))
	print(response)
	response_data = response.json()
	cell = 'C'+print_value
	ws[cell].value = ''.join(list(response_data['history'][-1]['categoryDescriptions'].keys()))
	value += 1
	print("end of loop")
	wb.save('example_testfile.xlsx')
