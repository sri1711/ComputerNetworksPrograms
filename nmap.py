import nmap

portScanner = nmap.PortScanner()
host_scan = input('HostScan : ')
portlist = "21,22,23,14,80"
portScanner.scan(hosts=host_scan,arguments='-n -p'+portlist)
print(portScanner.command_line())
hosts_list = [(x,portScanner[x]['status']['state']) for x in portScanner.all_hosts()]
for host,status in hosts_list:
    print(host,status)
for protocol in portScanner[host].all_protocols:
    print("Protocol:",protocol)
listport = portScanner[host]['tcp'].keys()
for port in listport:
    print("port :",port,portScanner[host][protocol][port]['state'])