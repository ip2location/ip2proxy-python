import sys
import struct
import socket

if sys.version < '3':
    def u(x):
        return x.decode('utf-8')
    def b(x):
        return str(x)
else:
    def u(x):
        if isinstance(x, bytes):
            return x.decode()
        return x
    def b(x):
        if isinstance(x, bytes):
            return x
        return x.encode('ascii')
        
# Windows version of Python does not provide it
#          for compatibility with older versions of Windows.
if not hasattr(socket, 'inet_pton'):
    def inet_pton(t, addr):
        import ctypes
        a = ctypes.WinDLL('ws2_32.dll')
        in_addr_p = ctypes.create_string_buffer(b(addr))
        if t == socket.AF_INET:
            out_addr_p = ctypes.create_string_buffer(4)
        elif t == socket.AF_INET6:
            out_addr_p = ctypes.create_string_buffer(16)
        n = a.inet_pton(t, in_addr_p, out_addr_p)
        if n == 0:
            raise ValueError('Invalid address')
        return out_addr_p.raw
    socket.inet_pton = inet_pton

_VERSION = '1.0.1'
_FIELD_NOT_SUPPORTED = 'NOT SUPPORTED'
_INVALID_IP_ADDRESS  = 'INVALID IP ADDRESS'

class IP2ProxyRecord:
    ''' IP2Proxy record with all fields from the database '''
    ip = None
    country_short = _FIELD_NOT_SUPPORTED
    country_long = _FIELD_NOT_SUPPORTED
    region = _FIELD_NOT_SUPPORTED
    city = _FIELD_NOT_SUPPORTED
    isp = _FIELD_NOT_SUPPORTED
    proxy_type = _FIELD_NOT_SUPPORTED

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

_COUNTRY_POSITION             = (0, 2, 3, 3, 3)
_REGION_POSITION              = (0, 0, 0, 4, 4)
_CITY_POSITION                = (0, 0, 0, 5, 5)
_ISP_POSITION                 = (0, 0, 0, 0, 6)
_PROXYTYPE_POSITION           = (0, 0, 2, 2, 2)

class IP2Proxy(object):
    ''' IP2Proxy database '''

    def __init__(self, filename=None):
        ''' Creates a database object and opens a file if filename is given '''
        if filename:
            self.open(filename)

    def __enter__(self):
        if not hasattr(self, '_f') or self._f.closed:
            raise ValueError("Cannot enter context with closed file")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self, filename):
        ''' Opens a database file '''
        # Ensure old file is closed before opening a new one
        self.close()

        self._f = open(filename, 'rb')
        self._dbtype = struct.unpack('B', self._f.read(1))[0]
        self._dbcolumn = struct.unpack('B', self._f.read(1))[0]
        self._dbyear = 2000 + struct.unpack('B', self._f.read(1))[0]
        self._dbmonth = struct.unpack('B', self._f.read(1))[0]
        self._dbday = struct.unpack('B', self._f.read(1))[0]
        self._ipv4dbcount = struct.unpack('<I', self._f.read(4))[0]
        self._ipv4dbaddr = struct.unpack('<I', self._f.read(4))[0]
        self._ipv6dbcount = struct.unpack('<I', self._f.read(4))[0]
        self._ipv6dbaddr = struct.unpack('<I', self._f.read(4))[0]
        self._ipv4indexbaseaddr = struct.unpack('<I', self._f.read(4))[0]
        self._ipv6indexbaseaddr = struct.unpack('<I', self._f.read(4))[0]

    def close(self):
        if hasattr(self, '_f'):
            # If there is file close it.
            self._f.close()
            del self._f

    def get_module_version(self):
        return _VERSION

    def get_package_version(self):
        return str(self._dbtype)

    def get_database_version(self):
        return str(self._dbyear) + "." + str(self._dbmonth) + "." + str(self._dbday)

    def get_country_short(self, ip):
        ''' Get country_short '''
        try:
            rec = self._get_record(ip)
            country_short = rec.country_short
        except:
            country_short = _INVALID_IP_ADDRESS
        return country_short

    def get_country_long(self, ip):
        ''' Get country_long '''
        try:
            rec = self._get_record(ip)
            country_long = rec.country_long
        except:
            country_long = _INVALID_IP_ADDRESS
        return country_long

    def get_region(self, ip):
        ''' Get region '''
        try:
            rec = self._get_record(ip)
            region = rec.region
        except:
            region = _INVALID_IP_ADDRESS
        return region

    def get_city(self, ip):
        ''' Get city '''
        try:
            rec = self._get_record(ip)
            city = rec.city
        except:
            city = _INVALID_IP_ADDRESS
        return city

    def get_isp(self, ip):
        ''' Get isp '''
        try:
            rec = self._get_record(ip)
            isp = rec.isp
        except:
            isp = _INVALID_IP_ADDRESS
        return isp

    def get_proxy_type(self, ip):
        ''' Get usage_type '''
        try:
            rec = self._get_record(ip)
            proxy_type = rec.proxy_type
        except:
            proxy_type = _INVALID_IP_ADDRESS
        return proxy_type

    def is_proxy(self, ip):
        ''' Determine whether is a proxy '''
        try:
            rec = self._get_record(ip)
            if self._dbtype == 1:
                is_proxy = 0 if (rec.country_short == '-') else 1
            else:
                is_proxy = 0 if (rec.proxy_type == '-') else ( 2 if (rec.proxy_type == 'DCH') else 1)
        except:
            is_proxy = -1
        return is_proxy

    def get_all(self, ip):
        ''' Get the whole record with all fields read from the file '''
        try:
            rec = self._get_record(ip)
            country_short = rec.country_short
            country_long = rec.country_long
            region = rec.region
            city = rec.city
            isp = rec.isp
            proxy_type = rec.proxy_type

            if self._dbtype == 1:
                is_proxy = 0 if (rec.country_short == '-') else 1
            else:
                is_proxy = 0 if (rec.proxy_type == '-') else ( 2 if (rec.proxy_type == 'DCH') else 1)
        except:
            country_short = _INVALID_IP_ADDRESS
            country_long = _INVALID_IP_ADDRESS
            region = _INVALID_IP_ADDRESS
            city = _INVALID_IP_ADDRESS
            isp = _INVALID_IP_ADDRESS
            proxy_type = _INVALID_IP_ADDRESS
            is_proxy = -1

        results = {}
        results['is_proxy'] = is_proxy
        results['proxy_type'] = proxy_type
        results['country_short'] = country_short
        results['country_long'] = country_long
        results['region'] = region
        results['city'] = city
        results['isp'] = isp
        return results

    def _reads(self, offset):
        self._f.seek(offset - 1)
        n = struct.unpack('B', self._f.read(1))[0]
        return u(self._f.read(n))
        # return self._f.read(n).decode('iso-8859-1').encode('utf-8')

    def _readi(self, offset):
        self._f.seek(offset - 1)
        return struct.unpack('<I', self._f.read(4))[0]

    def _readip(self, offset, ipv):
        if ipv == 4:
            return self._readi(offset)
        elif ipv == 6:
            a, b, c, d = self._readi(offset), self._readi(offset + 4), self._readi(offset + 8), self._readi(offset + 12) 
            return (d << 96) | (c << 64) | (b << 32) | a

    def _readips(self, offset, ipv):
        if ipv == 4:
            return socket.inet_ntoa(struct.pack('!L', self._readi(offset)))
        elif ipv == 6:
            return str(self._readip(offset, ipv))

    def _read_record(self, mid, ipv):
        rec = IP2ProxyRecord()

        if ipv == 4:
            off = 0
            baseaddr = self._ipv4dbaddr
        elif ipv == 6:
            off = 12
            baseaddr = self._ipv6dbaddr

        rec.ip = self._readips(baseaddr + (mid) * self._dbcolumn * 4, ipv)

        def calc_off(what, mid):
            return baseaddr + mid * (self._dbcolumn * 4 + off) + off + 4 * (what[self._dbtype]-1)

        if _COUNTRY_POSITION[self._dbtype] != 0:
            rec.country_short = self._reads(self._readi(calc_off(_COUNTRY_POSITION, mid)) + 1)
            rec.country_long =  self._reads(self._readi(calc_off(_COUNTRY_POSITION, mid)) + 4)

        if _REGION_POSITION[self._dbtype] != 0:
            rec.region = self._reads(self._readi(calc_off(_REGION_POSITION, mid)) + 1)

        if _CITY_POSITION[self._dbtype] != 0:
            rec.city = self._reads(self._readi(calc_off(_CITY_POSITION, mid)) + 1)

        if _ISP_POSITION[self._dbtype] != 0:
            rec.isp = self._reads(self._readi(calc_off(_ISP_POSITION, mid)) + 1)

        if _PROXYTYPE_POSITION[self._dbtype] != 0:
            rec.proxy_type = self._reads(self._readi(calc_off(_PROXYTYPE_POSITION, mid)) + 1)

        return rec

    def __iter__(self):
        low, high = 0, self._ipv4dbcount
        while low <= high:
            yield self._read_record(low, 4)
            low += 1

        low, high = 0, self._ipv6dbcount
        while low <= high:
            yield self._read_record(low, 6)
            low += 1

    def _parse_addr(self, addr): 
        ''' Parses address and returns IP version. Raises exception on invalid argument '''
        ipv = 0
        try:
            socket.inet_pton(socket.AF_INET6, addr)
            # Convert ::FFFF:x.y.z.y to IPv4
            if addr.lower().startswith('::ffff:'):
                try:
                    socket.inet_pton(socket.AF_INET, addr)
                    ipv = 4
                except:
                    ipv = 6
            else:
                ipv = 6
        except:
            socket.inet_pton(socket.AF_INET, addr)
            ipv = 4
        return ipv
        
    def _get_record(self, ip):
        low = 0
        ipv = self._parse_addr(ip) 
        if ipv == 4:
            ipno = struct.unpack('!L', socket.inet_pton(socket.AF_INET, ip))[0]
            off = 0
            baseaddr = self._ipv4dbaddr
            high = self._ipv4dbcount
            if self._ipv4indexbaseaddr > 0:
                indexpos = ((ipno >> 16) << 3) + self._ipv4indexbaseaddr
                low = self._readi(indexpos)
                high = self._readi(indexpos + 4)

        elif ipv == 6:
            a, b = struct.unpack('!QQ', socket.inet_pton(socket.AF_INET6, ip))
            ipno = (a << 64) | b
            off = 12
            baseaddr = self._ipv6dbaddr
            high = self._ipv6dbcount
            if self._ipv6indexbaseaddr > 0:
                indexpos = ((ipno >> 112) << 3) + self._ipv6indexbaseaddr
                low = self._readi(indexpos)
                high = self._readi(indexpos + 4)

        while low <= high:
            mid = int((low + high) / 2)
            ipfrom = self._readip(baseaddr + (mid) * (self._dbcolumn * 4 + off), ipv)
            ipto = self._readip(baseaddr + (mid + 1) * (self._dbcolumn * 4 + off), ipv)

            if ipfrom <= ipno < ipto:
                return self._read_record(mid, ipv)
            else:
                if ipno < ipfrom:
                    high = mid - 1
                else:
                    low = mid + 1
