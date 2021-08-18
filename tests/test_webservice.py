# -*- coding: utf-8 -*-

import pytest

import IP2Proxy

apikey = "demo"
package = "PX11"
usessl = True

ws = IP2Proxy.IP2ProxyWebService(apikey,package,usessl)

def testcountrycode():
    # ws = IP2Proxy.IP2ProxyWebService(apikey,package,usessl)
    rec = ws.lookup("8.8.8.8")
    assert rec['country_code'] == "US", "Test failed because country code not same."

def testgetcredit():
    credit = ws.getcredit()
    assert str(credit).isdigit() == True, "Test failed because it is no a digit value."

def testfunctionexist():
    functions_list = ['lookup', 'getcredit']
    for x in range(len(functions_list)): 
        assert hasattr(ws, functions_list[x]) == True, "Function did not exist."