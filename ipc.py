import xlrd
import re
import warnings
warnings.filterwarnings("ignore",category=UserWarning, module='bs4')

# Pull info from excel and print out relevant IP info to screen

# Start by getting Excel filename and opening it, get first sheet
filename = input("Enter excel filename with extension (xls, xlsx): ")
workbook = xlrd.open_workbook(filename) #,on_demand = True)
sheet = workbook.sheet_by_index(0) 

# Menu options
choice = 0
while choice < 1 or choice > 3:
	print("\n*** Wipro Python IP Checker ***\n")
	print("		1) Start from beginning")
	print("		2) Start from last checked")
	print("		3) Exit\n")
	choice = int(input("  > "))

# Set starting row based off user choice
startrow = 1
if choice == 2:
	for x in range(1, sheet.nrows):
		if (sheet.cell_type(x, 1) == xlrd.XL_CELL_EMPTY):
			startrow = x + 1
			break
elif choice == 3:
	exit()

