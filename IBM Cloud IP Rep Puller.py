import requests

response = requests.get("https://api.xforce.ibmcloud.com/ip/history/216.58.217.163")
#these prints are temporary while I fix the if else statement. Use this for now.
print response
print response.json()

#Still under work
#if response == '<Response [200]>':
	#print response.json()
#else:
#	print('ERROR: Connection not correctly established!')
#	print 'ERROR CODE: ', response
