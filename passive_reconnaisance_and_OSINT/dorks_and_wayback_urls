https://securitytrails.com/blog/top-shodan-dorks

https://securitytrails.com/blog/google-hacking-techniques

https://securitytrails.com/blog/github-dorks

--------------------------------------------------------------------
Search Engine Syntax:

https://www.google.com/advanced_search
https://support.google.com/websearch/answer/2466433
[hat tip: TryHackMe]

https://help.duckduckgo.com/duckduckgo-help-pages/results/syntax/
[hat tip: TryHackMe]

https://help.bing.microsoft.com/apex/index/18/en-US/10002
[hat tip: TryHackMe]
---------------------------------------------------------------------
GHDB (Google Hacking Database)
https://www.exploit-db.com/google-hacking-database
huge searchable/filterable database of Google dorks
---------------------------------------------------------------------
TomNomNom's WaybackURLs
https://github.com/tomnomnom/waybackurls

see: 
example from TryHackme [https://tryhackme.com/room/enumerationbruteforce ; Task 6 - OSINT] of installing this tool and then running it to pull a list of no longer extant URLs that were once associated with TryHackMe. In a pentest, one can use this tool to locate no longer extant URLs that look promising to search for exposed secrets and then visit them in the Internet Archive's Wayback Machine (https://webcf.waybackmachine.org/):

user@tryhackme $ git clone https://github.com/tomnomnom/waybackurls
user@tryhackme $ cd waybackurls
user@tryhackme $ sudo apt install golang-go -y # This command is optional
user@tryhackme $ go build
user@tryhackme $ ls -lah
total 6.6M
drwxr-xr-x 4 user user 4.0K Jul  1 18:20 .
drwxr-xr-x 9 user user 4.0K Jul  1 18:20 ..
drwxr-xr-x 8 user user 4.0K Jul  1 18:20 .git
-rw-r--r-- 1 user user   36 Jul  1 18:20 .gitignore
-rw-r--r-- 1 user user  454 Jul  1 18:20 README.mkd
-rw-r--r-- 1 user user   49 Jul  1 18:20 go.mod
-rw-r--r-- 1 user user 5.4K Jul  1 18:20 main.go
drwxr-xr-x 2 user user 4.0K Jul  1 18:20 script
-rwxr-xr-x 1 user user 6.5M Jul  1 18:20 waybackurls
user@tryhackme $ ./waybackurls tryhackme.com
[-- snip --]
https://tryhackme.com/.well-known/ai-plugin.json
https://tryhackme.com/.well-known/assetlinks.json
https://tryhackme.com/.well-known/dnt-policy.txt
https://tryhackme.com/.well-known/gpc.json
https://tryhackme.com/.well-known/nodeinfo
https://tryhackme.com/.well-known/openid-configuration
https://tryhackme.com/.well-known/security.txt
https://tryhackme.com/.well-known/trust.txt
[-- snip --]
---------------------------------------------------------------------

