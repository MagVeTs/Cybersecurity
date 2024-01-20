Using hashes for integrity
----------------------------
Subresource Integrity Hash [see here: https://tryhackme.com/room/owasptop102021 ; Task 19 - Software Integrity Failures]
https://www.srihash.org/
"SRI is a new W3C specification that allows web developers to ensure that resources hosted on third-party servers have not been tampered with. Use of SRI is recommended as a best-practice, whenever libraries are loaded from a third-party source."

--------------------------------------------------------
* Checking hashes in Linux Terminal [from: https://tryhackme.com/room/owasptop102021 ; task 18]
$ md5sum <NAME_OF_FILE>
$ sha1sum <NAME_OF_FILE>
$ sha256sum <NAME_OF_FILE>

* Another type of hashing option is supplied by HMAC (Hash-based message authentication code). This method combines the hashing function with a secret key. The same file will receive different hashes depending on the key that is chosen. One must know the secret key in order to check the hash (checksum) of the file you are examining against the hash of the original file in ordr to confirm there has been no tampering.
The following Linux tools can be used for HMAC: 
- hmac256
- sha224hmac
- sha256hmac
- sha384hmac
- sha512hmac
Example syntax:
$ hmac256 s!Kr37 message.txt
$ sha256hmac message.txt --key s!Kr37
[from: https://tryhackme.com/room/cryptographyintro ; Task 5 - Hashing]
