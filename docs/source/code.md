# IP2Proxy Python API

## IP2Proxy Class
```{py:class} IP2Proxy()
Construct the IP2Location Class.
```

```{py:function} open(binpath)
Load the IP2Proxy BIN database for lookup.

:param str binpath: (Required) The file path links to IP2Proxy BIN databases.
```

```{py:function} get_package_version()
Return the database's type, 1 to 10 respectively for PX1 to PX11. Please visit https://www.ip2location.com/databases/ip2proxy for details.

:return: Returns the package version.
:rtype: string
```

```{py:function} get_module_version()
Return the version of module.

:return: Returns the module version.
:rtype: string
```

```{py:function} get_database_version()
Return the database's compilation date as a string of the form 'YYYY-MM-DD'.

:return: Returns the database version.
:rtype: string
```

```{py:function} get_all(ip)
Retrieve geolocation information for an IP address.

:param string ip: (Required) The IP address (IPv4 or IPv6).
:return: Returns the geolocation information in array. Refer below table for the fields avaliable in the array
:rtype: array

**RETURN FIELDS**

| Field Name       | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| country_short    |     Two-character country code based on ISO 3166. |
| country_long    |     Country name based on ISO 3166. |
| region     |     Region or state name. |
| city       |     City name. |
| isp            |     Internet Service Provider or company\'s name. |
| domain         |     Internet domain name associated with IP address range. |
| usage_type      |     Usage type classification of ISP or company. |
| asn            |     Autonomous system number (ASN). |
| as_name             |     Autonomous system (AS) name. |
| last_seen       |     Proxy last seen in days. |
| threat         |     Security threat reported. |
| proxy_type      |     Type of proxy. |
| provider       |     Name of VPN provider if available. |
| fraud_score       |     Potential risk score (0 - 99) associated with IP address. |
```