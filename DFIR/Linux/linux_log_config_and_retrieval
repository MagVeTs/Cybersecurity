Linux Log Config and Retrieval
------------------------------

-------------------------------------------------------------------------------------------------------------------------------------
from: https://tryhackme.com/room/introtologs ; Task 4 "Collection, Management, and Centralisation" (with some minor editing)

A)

Synchronize time in the device in order to ensure logs will have correct timestamps:

$ ntpdate pool.ntp.org
# synchronize (requires internet connectivity)
$ date
# check date/time

B)

Use rsyslog to collect logs. 
Example use config of rsyslog to log all sshd messages to designated file

1) Open a Terminal.
2) Ensure rsyslog is Installed: You can check if rsyslog is installed by running the command:
$ sudo systemctl status rsyslog
3) Create a Configuration File: Use a text editor to create a new configuration file, for example: 
$ gedit /etc/rsyslog.d/98-websrv-02-sshd.conf
or
$ nano /etc/rsyslog.d/98-websrv-02-sshd.conf
or
$ vi /etc/rsyslog.d/98-websrv-02-sshd.conf
or
$ vim /etc/rsyslog.d/98-websrv-02-sshd.conf
4) Add the Configuration: Add the following lines in /etc/rsyslog.d/98-websrv-02-sshd.conf to direct the sshd messages to the specific log file:
$FileCreateMode 0644
:programname, isequal, "sshd" /var/log/websrv-02/rsyslog_sshd.log
5) Save and Close the Configuration File.
6) Restart rsyslog: Apply the changes by restarting rsyslog with the command:
$ sudo systemctl restart rsyslog
7) Verify the Configuration: You can verify the configuration works by initiating an SSH connection to localhost via ssh localhost or by checking the log file after a minute or two:
$ ssh localhost
$ cd /var/log/websrv-02/
$ ls -lsa
-------------------------------------------------------------------------------------------------------------------------------------
from: https://tryhackme.com/room/introtologs ; Task 5 - "Storage, Retention, and Deletion"

logrotate - "a tool that automates log file rotation, compression, and management, ensuring that log files are handled systematically. It allows automatic rotation, compression, and removal of log files."

Example: configure log management for /var/log/websrv-02/rsyslog_sshd.log using logrotate

Running this script will take an existing log file (in this case rsyslog_sshd.log) compress it and hash the compression. The final result will be that the original log file has been replaced by a compressed version of the log file and a separate document containing a hash of the compression. It is explained in https://tryhackme.com/room/introtologs - Task 6 that hashes of logs are important in order to assure admissibility in court (by preventing tampering).

1) Create a config file:
$ sudo gedit /etc/logrotate.d/98-websrv-02_sshd.conf
# or use nano, vi, vim, etc.
2) Define settings:

/var/log/websrv-02/rsyslog_sshd.log {
    daily
    rotate 30
    compress
    lastaction
        DATE=$(date +"%Y-%m-%d")
        echo "$(date)" >> "/var/log/websrv-02/hashes_"$DATE"_rsyslog_sshd.txt"
        for i in $(seq 1 30); do
            FILE="/var/log/websrv-02/rsyslog_sshd.log.$i.gz"
            if [ -f "$FILE" ]; then
                HASH=$(/usr/bin/sha256sum "$FILE" | awk '{ print $1 }')
                echo "rsyslog_sshd.log.$i.gz "$HASH"" >> "/var/log/websrv-02/hashes_"$DATE"_rsyslog_sshd.txt"
            fi
        done
        systemctl restart rsyslog
    endscript
}
3) Save and close
4) manually execute:
$ sudo logrotate -f /etc/logrotate.d/98-websrv-02_sshd.conf
-------------------------------------------------------------------------------------------------------------------------------------
from: https://tryhackme.com/room/introtologs ; Task 6 - "Hands-on Exercise: Log analysis process, tools, and techniques"

Free open source program to view log files in the browser:
LogViewer
https://github.com/sevdokimov/log-viewer
"Web UI for viewing logs"
"LogViewer is a Web application for monitoring server logs in real-time in the browser.
The tool provides powerful UI with highlighting, filtering, search, folding inconsiderable text. Merging several logs into one view works as well.
LogViewer can show huge log files without significant resource consumption because it reads only the part of the file that a user is watching. No indexing."
Demo video: https://www.youtube.com/watch?v=OE7nAiNX07Q
-------------------------------------------------------------------------------------------------------------------------------------
from: https://tryhackme.com/room/introtologs ; Task 6 - "Hands-on Exercise: Log analysis process, tools, and techniques"
Use Linux command line tools to parse, select, manipulate, and sort un-parsed log files before viewing.
Use tools such as: cat, grep, sort, uniq, awk, and sed.
Check MagVeTs > Cybersecurity > tools folder for more info on some of these tools.
-------------------------------------------------------------------------------------------------------------------------------------
