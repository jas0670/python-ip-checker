import requests

response = requests.get("https://api.xforce.ibmcloud.com/ipr/history/181.214.206.148")
#these prints are temporary while I fix the if else statement. Use this for now.
print(response)
print(response.json())

#Still under work
#if response == '<Response [200]>':
	#print response.json()
#else:
#	print('ERROR: Connection not correctly established!')
#	print 'ERROR CODE: ', response
