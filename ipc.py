import re
import grequests
import csv
import requests
import time
import os
from openpyxl import *

class IPC():
	def __init__(self):
		self.startrow = 2
		self.filename = ''
		self.workbook = ''
		self.sheet = ''

	def load(self):
		# Start by getting Excel filename and opening it, get first sheet
		self.filename = input("Enter excel filename with extension (xls, xlsx): ")
		self.workbook = load_workbook(self.filename) #,on_demand = True)
		self.sheet = self.workbook.active

		# Menu options
		choice = 0
		while choice < 1 or choice > 3:
			print("\n*** Wipro Python IP Checker ***\n")
			print("		1) Start from beginning")
			print("		2) Start from last checked")
			print("		3) Exit\n")
			choice = int(input("  > "))

		# Set starting row based off user choice
		self.startrow = 2
		if choice == 2:
			for x in range(2, self.sheet.max_row + 1):
				print(self.sheet.cell(x, 2))
				if self.sheet.cell(x, 2).value is None:
					self.startrow = x
					break
		elif choice == 3:
			exit()

	# Pulls data from the Xforce Exchange API
	def xforce(self):
		# Collect list of all Xforce Exchange API URLs for each IP
		# Due to restrictions of Xforce Exchange API, only request 10 IPs at a time
		# Code will gather all urls in one list, and then split into chunks for sending 10 at a tim
		responses = []
		urls = []
		for row in self.sheet.iter_rows(min_row=self.startrow, max_col=1, max_row=self.sheet.max_row):
			for cell in row:
				urls.append("https://api.xforce.ibmcloud.com/ipr/history/{}".format(cell.value))

		url_lists = [urls[x:x+10] for x in range(0, len(urls), 10)]
		for l in url_lists:
			request_list = (grequests.get(u, timeout=1000) for u in l)
			print("Sending request of {} IPs...".format(len(l)))
			responses.extend(grequests.map(request_list))

		scores = []
		for r in responses:
			try:
				scores.append(r.json()['history'][-1]['score'])
			except:
				scores.append("Timeout")

		# Add scores back to spreadsheet and save
		for cell in [x for t in self.sheet['B{}'.format(self.startrow):'B{}'.format(self.sheet.max_row)] for x in t]:
			cell.value = scores.pop(0)

	# Pulls data from the IPSpamList daily top IPs 1000 CSV
	def ipspamlist(self):
		with requests.Session() as s:
		    download = s.get('http://www.ipspamlist.com/public_feeds.csv')

		    decoded_content = download.content.decode('utf-8')

		    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
		    my_list = list(cr)
		    # Remove header row
		    my_list.pop(0) 
		    for row in my_list:
		    	# Put code here for processing each IP in the list
		    	# Index 2 is the IP
		        print(row[2])

	# Pulls data from the TotalVirus API
	def totalvirus(self):
		# Put Code here
		return None
	
	# Save the workbook
	def save(self):
		self.workbook.save(self.filename)


checker = IPC()
checker.load()
# Commented out for testing purposes
#checker.xforce()
checker.ipspamlist()
checker.save()