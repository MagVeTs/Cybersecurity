GetUserSPNs.py
---------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
"Kerberoasting Overview" ; https://academy.tcm-sec.com/courses/1152300/lectures/48493804
"Kerberoasting Walkthrough" ; https://academy.tcm-sec.com/courses/1152300/lectures/48493807

$ sudo GetUserSPNs.py <DOMAIN/username:password> -dc-ip <ip_of_DC> -request

- this will dump the Kerberos hash from the DC which you will then attempt to crack (e.g. using hashcat)
- SPN stands for ServicePrincipalName ; a service account (e.g. SQLService) within the AD
- once Kerberos hash is dumped copy the entire hash (starting from $krb5tgs and going all the way to the end) and paste it into a text doc for cracking
- the hashcat mode for Kerberos hashes is 13100
