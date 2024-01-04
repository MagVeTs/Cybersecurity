Investigating Suspicious Emails
--------------------------------

Get SPF record to check which IPs, etc. are permitted to send an email for a particular domain:

Linux Bash:

$ nslookup -type=txt example.com

OR

$ dig +short TXT example.com

the output will look like this:

v=spf1 include:_spf.google.com include:example.net ~all

In this case the SPF record gives server names (as opposed to IPs) that are authorized to send emails for the domain (example.com). The ~all at the end means other servers should "soft fail", showing that they are not authorized but not completely rejected
[from ChatGPT]
