secretsdump.py

---------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course ; https://academy.tcm-sec.com/courses/1152300/lectures/48489922
- dumps many types of secrets (including SAM hashes)
syntax:
$ secretsdump.py <domain>/<username>:'<password>'@<target_ip>
OR
$ secretsdump.py <username>@<target_ip> -hashes <NTLMv1_hash>
---------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
"Dumping the NTDS.dit" - https://academy.tcm-sec.com/courses/1152300/lectures/48496935

- the NTDS.dit is a database for storing AD data; including:
* user info
* group info
* security descriptors
* password hashes
- it can be dumped using secretsdump.py with the following syntax:

$ secretsdump.py <domain>/<username>:'<password>'@<target_ip> -just-dc-ntlm

NOTE: when getting an NTLM hash in order to attempt to crack it you need the NT part of the hash, not the LM part. The NT part is the SECOND part of the hash; the part that comes AFTER the colon.
TIP from HA: One can, of course, write a simple Bash script to break the lines of each NTLM account at the colons and extract just the username and NT hash. However, if you have Microsoft Excel you can:
* copy the whole file and paste into a spreadsheet
* choose the Data option and then the Text to Columns option
* choose Delimited
* choose Other and enter :
* choose Next and Finish
* you will now have everything in nice columns and you can delete all but the username and NT hash columns and then begin to crack them.
[The ability to parse text into columns using delimiters is also available in Google Sheets (Data > Split text to Columns) --MagVeTS]
NOTE: See the linked lecture video above for even more information regarding working with spreadsheets to merge the data showing the username-hash combinations with a spreadsheet containing hash-password combinations retrieved from hashcat. This will allow you to create one spreadsheet with columns for username-hash-password combinations. The process involves using the vlookup function. Here is a link to an article about using vlookup in Google Sheets: https://www.makeuseof.com/use-vlookup-function-google-sheets/. Here is info on using vlookup in Excel: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1. --MagVeTs]
---------------

