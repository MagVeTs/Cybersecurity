NTLM hashes
------------

NTLM to Password
"Input NT/LM hashes in hex format, one per line"
https://ntlm.pw/
-----------------------------------------------------------------------------
LM, NTLM, Net-NTLMv2, oh my!
A Pentester’s Guide to Windows Hashes
https://medium.com/@petergombos/lm-ntlm-net-ntlmv2-oh-my-a9b235c58ed4
------------------------------------------------------------------------------
"Windows hashes are the way Windows stores passwords on machines. First, let's clarify things.
NTLM (aka NT) hashes are local users hashes
NTLMv1/v2 (aka Net-NTLMv1/v2) hashes are used for network authentication
MSCASHv1/v2 (aka DCCv1/v2) hashes are domain users hashes

NTLM ≠ NTLMv1/v2 ≠ MSCASHv1/v2

NTLM hashes are composed of two parts:

LM hash (turned off since Windows Vista / Windows 2008)
NT hash (can be lonely, it stays NTLM hash)"

- the LM hash is listed first, followed by a colon, followed by the NT hash:
<LM>:<NT>
[from: https://aas-s3curity.gitbook.io/cheatsheet/internalpentest/active-directory/post-exploitation/extracting-credentials/retrieve-windows-hashes]
------------------------------------------------------------------------------
Heath Adams - The Cyber Mentor
Practical Ethical Hacking - The Complete Course
"Pass Attacks" - https://academy.tcm-sec.com/courses/1152300/lectures/48489919

HA says that pass-the-hash attacks work for NTLMv1; not NTLMv2. NTLMv2 works for relay attacks.
-----------------------------------------------------------------------------------------------------------------
from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course ; https://academy.tcm-sec.com/courses/1152300/lectures/48489922
When CRACKING an NTLM hash you only need the NT part (given AFTER the colon) not the LM part (given BEFORE the colon)
