# -*- coding: utf-8 -*-

import pytest

import os, sys, IP2Proxy

db = IP2Proxy.IP2Proxy()

def testinvaliddatabase():
    try:
        db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    except ValueError as e:
        assert "The database file does not seem to exist." == str(e)

def testfunctionexist():
    errors = []
    functions_list = ['open', 'close', 'get_module_version', 'get_package_version', 'get_database_version', 'get_all', 'is_proxy', 'get_proxy_type', 'get_country_short', 'get_country_long', 'get_region', 'get_city', 'get_isp', 'get_domain', 'get_usage_type', 'get_asn', 'get_as_name', 'get_last_seen', 'get_threat']
    for x in range(len(functions_list)): 
        # assert hasattr(db, functions_list[x]) == True, "Function did not exist."
        if (hasattr(db, functions_list[x]) == False):
            errors.append("Function " + functions_list[x] + " did not exist.")
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def testinvalidip():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_all("1.0.0.x")
    assert rec['country_short'] == "INVALID IP ADDRESS"

def testipv4countrycode():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_all("1.0.0.8")
    assert rec['country_short'] == "US", "Test failed because country code not same."

def testipv4countryname():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_all("1.0.0.8")
    assert rec['country_long'] == "United States of America", "Test failed because country name not same."

def testgetcountryshort():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_country_short("1.0.0.8")
    assert rec == "US", "Test failed because country code not same."

def testgetcountrylong():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_country_long("1.0.0.8")
    assert rec == "United States of America", "Test failed because country name not same."

def testgetregion():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_region("1.0.0.8")
    assert rec == "California"

def testgetcity():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_city("1.0.0.8")
    assert rec == "Los Angeles"

def testgetisp():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_isp("1.0.0.8")
    assert rec == "APNIC and CloudFlare DNS Resolver Project"

def testgetdomain():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_domain("1.0.0.8")
    assert rec == "cloudflare.com"

def testgetusagetype():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_usage_type("1.0.0.8")
    assert rec == "CDN"

def testgetasn():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_asn("1.0.0.8")
    assert rec == "13335"

def testgetasname():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_as_name("1.0.0.8")
    assert rec == "CLOUDFLARENET"

def testgetlastseen():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_last_seen("1.0.0.8")
    assert rec == "22"

def testgetthreat():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_threat("1.0.0.8")
    assert rec == "-"

def testisproxy():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.is_proxy("1.0.0.8")
    assert rec == 2

def testgetproxytype():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_proxy_type("1.0.0.8")
    assert rec == "DCH"

def testipv6countrycode():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_all("2c0f:ffa0::4")
    assert rec['country_short'] == "UG", "Test failed because country code not same."

def testipv6countryname():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    rec = db.get_all("2c0f:ffa0::4")
    assert rec['country_long'] == "Uganda", "Test failed because country name not same."

def testgetmoduleversion():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    assert db.get_module_version() == "3.1.2"

def testgetpackageversion():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    assert db.get_package_version() == "10"

def testgetdatabaseversion():
    db.open(os.path.join("data", "PX10.SAMPLE.BIN"))
    assert db.get_database_version() == "2020.10.23"