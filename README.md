# IP2Proxy Python Library

This library allows user to query an IP address if it was being used as open proxy, web proxy, VPN anonymizer and TOR exits. It lookup the proxy IP address from **IP2Proxy BIN Data** file. This data file can be downloaded at

* Free IP2Proxy BIN Data: https://lite.ip2location.com
* Commercial IP2Proxy BIN Data: https://www.ip2location.com/proxy-database

For more details, please visit:
[https://www.ip2location.com/ip2proxy/developers/python](https://www.ip2location.com/ip2proxy/developers/python)

## Methods

Below are the methods supported in this library.

|Method Name|Description|
|---|---|
|open|Open the IP2Proxy BIN data with **File I/O** mode for lookup.|
|close|Close and clean up the file pointer.|
|get_package_version|Get the package version (1 to 4 for PX1 to PX4 respectively).|
|get_module_version|Get the module version.|
|get_database_version|Get the database version.|
|is_proxy|Check whether if an IP address was a proxy. Returned value:<ul><li>-1 : errors</li><li>0 : not a proxy</li><li>1 : a proxy</li><li>2 : a data center IP address</li></ul>|
|get_all|Return the proxy information in array.|
|get_proxy_type|Return the proxy type. Please visit <a href="https://www.ip2location.com/databases/px4-ip-proxytype-country-region-city-isp" target="_blank">IP2Location</a> for the list of proxy types supported|
|get_country_short|Return the ISO3166-1 country code (2-digits) of the proxy.|
|get_country_long|Return the ISO3166-1 country name of the proxy.|
|get_region|Return the ISO3166-2 region name of the proxy. Please visit <a href="https://www.ip2location.com/free/iso3166-2" target="_blank">ISO3166-2 Subdivision Code</a> for the information of ISO3166-2 supported|
|get_city|Return the city name of the proxy.|
|get_isp|Return the ISP name of the proxy.|

## Requirements
1. Python 2.2 and above

## Installation
1. Unzip the package.
2. Execute python setup.py build
3. Execute python setup.py install

or

To install this module type the following (for PyPI):

	pip install IP2Location


## Testing
    python sample.py
    python test.py

## Support
Email: support@ip2location.com.
URL: [https://www.ip2location.com](https://www.ip2location.com)
