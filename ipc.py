import xlrd
import re
import warnings
warnings.filterwarnings("ignore",category=UserWarning, module='bs4')
from robobrowser import RoboBrowser

#pull info from excel and prints out relevant ip info to screen.
workbook = xlrd.open_workbook('ReferenceData_Test_ThreatConnect Botnet IPs Results_asc.xlsx') #,on_demand = True)
sheet = workbook.sheet_by_index(0) #first sheet of excel
for x in range (0,sheet.ncols):
 for y in range (1,sheet.nrows):
  if sheet.cell_value(y,x) != "":
   print(sheet.cell_value(y,x))
   
