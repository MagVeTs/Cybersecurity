THC Hydra
https://github.com/vanhauser-thc/thc-hydra
From: https://tryhackme.com/room/protocolsandservers2 ; task 6 [with some editing]
Hydra supports many protocols, including FTP, POP3, IMAP, SMTP, SSH, and all methods related to HTTP. The general command-line syntax is:
hydra -l USERNAME -P WORDLIST.TXT SERVER SERVICE

where we specify the following options:

-l USERNAME: -l should precede the username, i.e. the login name of the target.
-P WORDLIST.TXT: -P precedes the wordlist.txt file, which is a text file containing the list of passwords you want to try with the provided username, e.g. /usr/share/wordlists/rockyou.txt
SERVER is the hostname or IP address of the target server.
SERVICE indicates the service which you are trying to launch the dictionary attack (e.g. ftp or imap)

Consider the following concrete examples:

hydra -l mark -P /usr/share/wordlists/rockyou.txt 10.10.69.61 ftp will use mark as the username as it iterates over the provided passwords against the FTP server.
hydra -l mark -P /usr/share/wordlists/rockyou.txt ftp://10.10.69.61 is identical to the previous example. 10.10.69.61 ftp is the same as ftp://10.10.69.61.
hydra -l frank -P /usr/share/wordlists/rockyou.txt 10.10.69.61 ssh will use frank as the user name as it tries to login via SSH using the different passwords.

There are some extra optional arguments that you can add:

-s PORT to specify a non-default port for the service in question.
-V or -vV, for verbose, makes Hydra show the username and password combinations that are being tried. This verbosity is very convenient to see the progress, especially if you are still not confident of your command-line syntax.
-t n where n is the number of parallel connections to the target. -t 16 will create 16 threads used to connect to the target.
-d, for debugging, to get more detailed information about what’s going on. The debugging output can save you much frustration; for instance, if Hydra tries to connect to a closed port and timing out, -d will reveal this right away.
Once the password is found, you can issue CTRL-C to end the process. 

More hydra information [from: https://tryhackme.com/room/passwordattacks ; Task 8 [with edits, etc.]:
Hydra can attack many types of network services to brute-force, etc. their passwords (e.g. http web-logins, FTP, SMTP, and SSH)
Often, within hydra, each service has its own options and the syntax hydra expects takes getting used to. It's important to check the help options for more information and features.

ftp
example syntax:
hydra -l ftp -P passlist.txt ftp://10.10.x.x
-l ftp we are specifying a single username, use-L for a username wordlist
-P Path specifying the full path of wordlist, you can specify a single password by using -p.
ftp://10.10.x.x the protocol and the IP address or the fully qualified domain name (FDQN) of the target.
Remember that sometimes you don't need to brute-force and could first try default credentials.

smtp
example syntax:
hydra -l email@company.xyz -P /path/to/wordlist.txt smtp://10.10.x.x -v 
Note: same as ftp; only with a different service (an SMTP server) specified instead; also note the `-v` flag for verbose so that each attempted login appears in terminal

ssh
example syntax:
hydra -L users.lst -P /path/to/wordlist.txt ssh://10.10.x.x -v
Note: same as ftp and smtp; only, in this example a file of possible users was employed by using the `-L` flag and naming the file

http login pages
Using hydra, it is important to specify the type of HTTP request, whether GET or POST. Checking hydra options: hydra http-get-form -U, we can see that hydra has the following syntax for the http-get-form option:

<url>:<form parameters>:<condition string>[:<optional>[:<optional>]

... we need to analyze the HTTP request that we need to send, and that could be done either by using your browser dev tools or using a web proxy such as Burp Suite.
sample syntax:
hydra -l admin -P 500-worst-passwords.txt 10.10.x.x http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:S=logout.php" -f 
-l admin  we are specifying a single username, use-L for a username wordlist

-P Path specifying the full path of wordlist, you can specify a single password by using -p.

10.10.x.x the IP address or the fully qualified domain name (FQDN) of the target.

http-get-form the type of HTTP request, which can be either http-get-form or http-post-form.

Next, we specify the URL, path, and conditions that are split using `:`

login-get/index.php the path of the login page on the target webserver.

username=^USER^&password=^PASS^ the parameters to brute-force, we inject ^USER^ to brute force usernames and ^PASS^ for passwords from the specified dictionary.

The following section is important to eliminate false positives by specifying the 'failed' condition with F= or specifying success conditions with S=. You will get more information about these conditions by analyzing the webpage or in the enumeration stage! What you set for these values depends on the response you receive back from the server for a failed login attempt and a successful login attempt. For example, if you receive a message on the webpage 'Invalid password' after a failed login, set F=Invalid Password.

If during the enumeration, we found that the webserver serves a page called logout.php it may be guessed that upon logging into the login page with valid credentials the logout.php link will appear somewhere on the page in order to enable a logout at the end of the session. Therefore, in order to have proof that the login was successful we could tell hydra to look for the text logout.php within the HTML for every request. We do this by setting `S=logout.php` as the success condition to identify the valid credentials.

-f this flag tells hydra to stop the brute-forcing attacks after finding a valid username and password as signified by the presence of the success condition (in this case logout.php).
