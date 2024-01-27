Managing Users
--------------
[From: Network Chuck - sudo = POWER!! (managing users in Linux) // Linux for Hackers // EP4 ; https://www.youtube.com/watch?v=jwnvKOjmtEA&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=4]

* whoami
* groups - this command will list all the groups the user account you are in is a member of
* adduser <NAME_OF_USER_ACCOUNT_BEING_CREATED> <--usually you will create new user accounts with this command; it will walk you through the full creation of the new user account and automatically creates a home directory for the account
* useradd <NAME_OF_USER_ACCOUNT_BEING_CREATED> <--this one does not do as much; it will create the account but you will have to add password and home directory later (see 'usermod')
* usermod - allows you to modify an existing user account, including adding the user to groups (syntax: sudo usermod -aG <GROUP_NAME> <USER_NAME>)
[Removing a user from a group, syntax: sudo gpasswd -d <USER_NAME> <GROUP_NAME>]
* cat /etc/passwd - list of users
* su - <NAME_OF_USER_BEING_SWITCHED_TO>
The 'su -' command is used for changing users (su = switch user). [Note: using 'su -' without giving a user name will default to switching to the root user.] Typing 'exit', 'logout' or CTRL-D will return you to your original user account.
* sudo - stands for "super user do" change to root user for one command then it switches back
The list of users who have sudo rights is found in the sudoers file. The safe, best practice way to edit this file is using the command: 'sudo visudo'
* userdel - delete a user
* groupadd - add a group (list of groups stored in /etc/group; every user automatically is assigned their own group which is the same as their username; they can also be assigned to created groups)
* groupdel - delete a group (syntax: sudo groupdel <GROUP_NAME>)
--------------------------------------------------------------------------------------------------------------------------------------------------------
