import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="IP2Proxy",
	version="3.1.2", 
	author="IP2Location",
	author_email="support@ip2location.com",
	description="Python API for IP2Proxy database. It can be used to query an IP address if it was being used as open proxy, web proxy, VPN anonymizer and TOR exits.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['IP2Proxy'],
	url="https://github.com/ip2location/ip2proxy-python",
	packages=setuptools.find_packages(),
	tests_require=['pytest>=3.0.6'],
	classifiers=(
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
)
