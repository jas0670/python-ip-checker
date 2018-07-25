# python-ip-checker
IP Blacklist Verification


MAIN GOAL FOR RIGHT NOW:

Take the blchecker, virusttotal, and xforce API checker and combine them into one script. Heirarchy within that script should be as follows:

1. Excel file opened
2. Ip address from Excel file is passed to blchecker
3a. if blchecker returns a 0, nothing happens/on to the next IP
3b. if blchecker returns anything above a 0, the IP gets passed to a second excel sheet.
4. When complete, the system will then run the xforce script and the virusttotal script on the second sheet and report back information about the blacklisted IP's

This should be a fairly small script. The main script should import the modules/other scripts we have created and combine them all together.
