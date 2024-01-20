From: https://tryhackme.com/room/passwordattacks ; Task 9 - Password Spray Attacks [with edits, etc.]

Difference between brute-force attack and password spray attack:
* brute-force - test many common/predictable passwords against one username
* password spraying - test one common/predictable password against many usernames
Note: password spraying attacks are less likely than brute-force attacks to trigger account lockouts

Common and weak passwords often follow a pattern and format, e.g.

* SeasonYear (e.g. Fall2020)
* MonthYear (e.g. November2020)
* CompanyNameRandomNumbers (e.g. TryHackMe01)
Note: If a password complexity policy is enforced within the organization, we may need to create a password that includes symbols to fulfill the requirement, such as October2021!, Spring2021!, October2021@, etc.
Note: For better success in a password spraying attack, first enumerate the target and gather OSINT to compile a list of valid usernames/email addresses.

Tools for password spraying at various services:
* hydra [sample syntax: hydra -L usernames-list.txt -p Spring2021 ssh://10.1.1.10]
* https://github.com/xFreed0m/RDPassSpray - against RDP [sample syntax: python3 RDPassSpray.py -U usernames-list.txt -p Spring2021! -t 10.100.10.240:3026]
* Metasploit (auxiliary/scanner/smb/smb_login) - against smb
* https://github.com/blacklanternsecurity/TREVORspray 
TREVORspray is a modular password sprayer with threading, clever proxying, loot modules, and more!
* https://github.com/knavesec/CredMaster
Launch a password spray / brute force attach via Amazon AWS passthrough proxies, shifting the requesting IP address for every authentication attempt. This dynamically creates FireProx APIs for more evasive password sprays.
* https://github.com/dafthack/MailSniper
MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used as a non-administrative user to search their own email or by an Exchange administrator to search the mailboxes of every user in a domain.
MailSniper also includes additional modules for password spraying, enumerating users and domains, gathering the Global Address List (GAL) from OWA and EWS and checking mailbox permissions for every Exchange user at an organization.
-----------------------------------------------------------------------------------------------------------------
