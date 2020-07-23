import IP2Proxy

db = IP2Proxy.IP2Proxy()

# open IP2Proxy BIN database for proxy lookup
# db.open(os.path.join("data", "IP2PROXY-IP-PROXYTYPE-COUNTRY-REGION-CITY-ISP.SAMPLE.BIN"))
db.open("IP2PROXY-IP-PROXYTYPE-COUNTRY-REGION-CITY-ISP-DOMAIN-USAGETYPE-ASN-LASTSEEN-THREAT-RESIDENTIAL.BIN")

# get versioning information
print ('Module Version: ' + db.get_module_version())
print ('Package Version: ' + db.get_package_version())
print ('Database Version: ' + db.get_database_version())

# individual proxy data check
print ('Is Proxy: ' + str(db.is_proxy("4.0.0.47")))
print ('Proxy Type: ' + db.get_proxy_type("4.0.0.47"))
print ('Country Code: ' + db.get_country_short("4.0.0.47"))
print ('Country Name: ' + db.get_country_long("4.0.0.47"))
print ('Region Name: ' + db.get_region("4.0.0.47"))
print ('City Name: ' + db.get_city("4.0.0.47"))
print ('ISP: ' + db.get_isp("4.0.0.47"))
print ('Domain: ' + db.get_domain("4.0.0.47"))
print ('Usage Type: ' + db.get_usage_type("4.0.0.47"))
print ('ASN: ' + db.get_asn("4.0.0.47"))
print ('AS Name: ' + db.get_as_name("4.0.0.47"))
print ('Last Seen: ' + db.get_last_seen("4.0.0.47"))
print ('Threat: ' + db.get_threat("4.0.0.47"))

# single function to get all proxy data returned in array
record = db.get_all("4.0.0.47")

print ('Is Proxy: ' + str(record['is_proxy']))
print ('Proxy Type: ' + record['proxy_type'])
print ('Country Code: ' + record['country_short'])
print ('Country Name: ' + record['country_long'])
print ('Region Name: ' + record['region'])
print ('City Name: ' + record['city'])
print ('ISP: ' + record['isp'])
print ('Domain: ' + record['domain'])
print ('Usage Type: ' + record['usage_type'])
print ('ASN: ' + record['asn'])
print ('AS Name: ' + record['as_name'])
print ('Last Seen: ' + record['last_seen'])
print ('Threat: ' + record['threat'])

# close IP2Proxy BIN database
db.close()