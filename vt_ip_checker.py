import virustotal2

vt = virustotal2.VirusTotal2("1fd2648228dde4b02c2438110543db84030033c0e4d9addd12a993b1c126d347")

ip_report = vt.retrieve("IP_ADDR_HERE", raw = True)

print ip_report
