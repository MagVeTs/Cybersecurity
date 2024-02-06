PATH
----
from: https://phoenixnap.com/kb/linux-add-to-path
"PATH is an environment variable that instructs a Linux system in which directories to search for executables. The PATH variable enables the user to run a command without specifying a path."
"When a user invokes a command in the terminal, the system executes a program. Therefore, Linux has to be able to locate the correct executable. PATH specifies program directories and instructs the system where to search for a program to run."

$ echo $PATH
# prints all the directories that are currently in the PATH; executables that reside in any of these places can be run without specifying their path; as long as the executable's name is given in the command, the system will search all the directories in the PATH and find the executable and run it

$ printenv PATH
# does the same thing as the `echo $PATH` command

$ which whoami
# tells you the directory where the script for the command or executable (in this case `whoami`) resides

$ export PATH="/Directory1:$PATH"
# temporarily add `/Directory1` to PATH (for duration of terminal session)

To permanently add a directory to PATH for current user:
1) Open .bashrc file:
$ nano /etc/bash.bashrc
2) Scroll to end of file
3) add the following text:
export PATH="/Directory1:$PATH"
4) save the file and exit it
5) reboot 
6) verify by running:
$ echo $PATH
NOTE: the .bashrc file may be in different places dpending on the distro. Here is the location for some popular distros:
/etc/bash.bashrc (Debian, Ubuntu, Linux Mint, Backtrack, Kali etc)
(https://unix.stackexchange.com/questions/211713/where-is-bashrc-file-found-in-linux)

To permanently add a directory to PATH for all users:
1) Open .profile file:
$ nano ~/.profile
2) Scroll to end of file
3) add the following text:
export PATH="/Directory1:$PATH"
4) save the file and exit it
5) reboot 
6) verify by running:
$ echo $PATH

see the article (https://phoenixnap.com/kb/linux-add-to-path) for info on removing directories from PATH

