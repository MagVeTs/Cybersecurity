---------------------------------------------------------------
From: https://tryhackme.com/room/protocolsandservers2 ; task 4
Protocol  Default Port	Secured Protocol	Default Port with TLS
--------  ------------  ----------------  ---------------------
HTTP	         80         	HTTPS	             443
FTP          	 21	          FTPS	             990
SMTP	         25	          SMTPS	             465
POP3	         110	        POP3S	             995
IMAP	         143	        IMAPS	             993
---------------------------------------------------------------
From: https://tryhackme.com/room/protocolsandservers2 ; task 5; with some editing

For Telnet (23), use SSH (22) instead.

Secure Shell (SSH) was created to provide a secure way for remote system administration. In other words, it lets you securely connect to another system over the network and execute commands on the remote system. Put simply, the “S” in SSH stands for secure, which can be summarized simply as:

1. You can confirm the identity of the remote server
2. Exchanged messages are encrypted and can only be decrypted by the intended recipient
3. Both sides can detect any modification in the messages

The above three points are ensured by cryptography. In more technical terms, they are part of confidentiality and integrity, made possible through the proper use of different encryption algorithms.

To use SSH, you need an SSH server and an SSH client. The SSH server listens on port 22 by default. The SSH client can authenticate using:

A username and a password
A private and public key (after the SSH server is configured to recognize the corresponding public key)

On Linux, macOS, and MS Windows builds after 2018, you can connect to an SSH server using the following command ssh USERNAME@SERVER_MACHINE_IP. This command will try to connect to the server of IP given IP address with the given username. If an SSH server is listening on the default port, it will ask you to provide the password for username. Once authenticated, the user will have access to the target server’s terminal. 

Note that if this is the first time we connect to this system, we will need to confirm the fingerprint of the SSH server’s public key to avoid man-in-the-middle (MITM) attacks ... MITM takes place when a malicious party, E, situates itself between A and B, and communicates with A, pretending to be B, and communicates with B pretending to be A, while A and B think that they are communicating directly with each other. In the case of SSH, we don’t usually have a third party to check if the public key is valid, so we need to do this manually.

We can use SSH to transfer files using SCP (Secure Copy Protocol) based on the SSH protocol. An example of the syntax is as follows:
scp mark@10.10.16.40:/home/mark/archive.tar.gz ~
This command will copy a file named archive.tar.gz from the remote system located in the /home/mark directory to ~, i.e., the root of the home directory of the currently logged-in user.

Another example syntax is:
scp backup.tar.bz2 mark@10.10.16.40:/home/mark/
This command will copy the file backup.tar.bz2 from the local system to the directory /home/mark/ on the remote system.

...FTP could be secured using SSL/TLS by using the FTPS protocol which uses port 990. It is worth mentioning that FTP can also be secured using the SSH protocol which is the SFTP protocol. By default this service listens on port 22, just like SSH.

---------------------------------------------------------------------------------

