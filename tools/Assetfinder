Assetfinder - IMPORTANT! see: tools/HA_script_domain_enumeration
------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
"Finding subdomains with Assetfinder" - https://academy.tcm-sec.com/courses/1152300/lectures/24781573

https://github.com/tomnomnom/assetfinder
"Find domains and subdomains related to a given domain"

HA holds highly of Tomnomnom

to install:
- make sure you have Go installed on your Kali (see the pimpmykali file in the "tools" folder in this repository for an easy way to accomplish this)
$ go get -u github.com/tomnomnom/assetfinder

after installation:
$ assetfinder <name_of_domain>.<tld>
[e.g. tesla.com]

- you can easily direct the assetfinder output to a file:
e.g. assetfinder tesla.com >> tesla_subdomains.txt
- the output will be both subdomains AND domains that may be related even if they are NOT subdomains. If you only want subdomains then add the following argument:
$ assetfinder --subs-only <domain>
- the best option, in HA's opinion, is to run the full assetfinder discovery and then grep the subdomains.
------------------------------------------------------------------------------------------------------------------------------------





