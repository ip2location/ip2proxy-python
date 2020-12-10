# -*- coding: utf-8 -*-

import pytest

import os, IP2Proxy

db = IP2Proxy.IP2Proxy()

db.open(os.path.join("data", "IP2PROXY-IP-PROXYTYPE-COUNTRY-REGION-CITY-ISP.SAMPLE.BIN"))

def testfunctionexist():
    assert hasattr(db, 'get_all') == True, "Function did not exist."

def testipv4countrycode():
    rec = db.get_all("8.8.8.8")
    assert rec['country_short'] == "-", "Test failed because country code not same."

def testipv4countryname():
    rec = db.get_all("8.8.8.8")
    assert rec['country_long'] == "-", "Test failed because country name not same."

def testipv4unsupportedfield():
    rec = db.get_all("8.8.8.8")
    assert rec['city'] == "-", "Test failed because city name not same."

def testipv6countrycode():
    rec = db.get_all("2001:4860:4860::8888")
    assert rec['country_short'] == "-", "Test failed because country code not same."

def testipv6countryname():
    rec = db.get_all("2001:4860:4860::8888")
    assert rec['country_long'] == "-", "Test failed because country name not same."

def testipv6unsupportedfield():
    rec = db.get_all("2001:4860:4860::8888")
    assert rec['city'] == "-", "Test failed because city name not same."
