# python-ip-checker
IP Blacklist Verification

VERSION 1.0

Download blcheck.sh, ipchecker.py, and ipcopy.py. Initialize blcheck within your system, and then run ipchecker.py. Ensure that you have actually changed the accessible files within the script to match what you have downloaded.

Also make sure that you have the files CLOSED or else the program will not be able to write to them. 

To come in VERSION 2.0:
 - Multi threading to speed up the process?
 - A way to verify non-blacklisted IP's against IBM's repository for verification. The functionality isn't the problem, it's the limited number of requests we can do per month.
 - VirusTotal2 implementation. Right now, the information accessed doesn't work well within the specs of the excel document.

MAIN GOAL FOR RIGHT NOW:

Take the blchecker, virusttotal, and xforce API checker and combine them into one script. Heirarchy within that script should be as follows:

1. Excel file opened
2. Ip address from Excel file is passed to blchecker
3. if blchecker returns a 0, nothing happens/on to the next IP
3. if blchecker returns anything above a 0, the IP gets passed to a second excel sheet.
4. When complete, the system will then run the xforce script and the virusttotal script on the second sheet and report back information about the blacklisted IP's

This should be a fairly small script. The main script should import the modules/other scripts we have created and combine them all together.
