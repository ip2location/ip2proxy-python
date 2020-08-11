import os, IP2Proxy, sys, ipaddress

# database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"), "SHARED_MEMORY")
# database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"))
database = IP2Proxy.IP2Proxy("C:\\OoiKaiWen\\work\\code\\perl\\ip2proxy\\databases\\IP2PROXY-IP-PROXYTYPE-COUNTRY-REGION-CITY-ISP-DOMAIN-USAGETYPE-ASN-LASTSEEN-THREAT-RESIDENTIAL.BIN")

try:
    ip = sys.argv[1]

    if ip == '' :
        print ('You cannot enter an empty IP address.')
        sys.exit(1)
    else:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            print ('Invalid IP address')
            sys.exit(1)

    rec = database.get_all(ip)
    print (rec)

except IndexError:
    print ("Please enter an IP address to continue.")

database.close()