import os, sys
ip = input("Enter IP:\n")
#os.system("./blcheck " + ip)
command = "./blcheck " + ip

import subprocess
import re

child = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
output = str(child.communicate()[0])


output = re.findall(r'\d+', output)
print(int(output[0]))