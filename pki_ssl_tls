PKI - SSL/TLS
--------------

https://tryhackme.com/room/cryptographyintro ; Task 6 - "PKI and SSL/TLS"

Generate Certificate Signing Request (CSR):

$ openssl req -new -nodes -newkey rsa:4096 -keyout key.pem -out cert.csr

# req -new = create a new certificate signing request
# -nodes = save private key without a passphrase
# -newkey = generate a new private key
# rsa:4096 = generate an RSA key of size 4096 bits
# -keyout = specify where to save the key
# -out = save the certificate signing request

- you will be asked a series of questions to get the info to put in the CSR
- after generation the CSR can be sent to an official Certificate Authority (CA) to get it signed

For a self-signed certificate the following syntax is used:

$ openssl req -x509 -newkey -nodes rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
# -x509 = generate self-signed certificate
# -sha256 = use SHA256 digest
# -days 365 = make certificate valid for 1 year

$ openssl x509 -in cert.pem -text
# this syntax will let you view the certificate you just created

