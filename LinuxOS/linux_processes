Linux Processes
-----------------


-----------------------------------------------------------------------------------
[From: Network Chuck - KILL Linux processes!! (also manage them) // Linux for Hackers // EP 7 ; https://www.youtube.com/watch?v=LfC6pv8VISk&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=10]

commands:
* ps 
shows running processes; however default is just to show processes running in the terminal you are entering the command from - you will usually need to add arguments

* ps --help
will show you ps help options; you have to then choose from them to see a help guide

* ps -aux
the arguments -aux are the most commonly used arguments for ps:
a = show processes from all users
u = list the user that each process belongs to
x = show processes from everywhere (not just the processes executed from the terminal you are entering the command from)
you can '| grep' for a particular process (not every system has pgrep installed)

* pgrep <NAME_OF_PROCESS>
this combines ps with grep to find a particular process and return its PID (process ID) - which is necessary for killing a process (Note: not every system has pgrep installed; you might need to do: ps -aux | grep <NAME_OF_PROCESS>)

* kill <PID (PROCESS ID)>
stops a process; used to stop unresponsive processes
[in order to ensure that a process is killed immediately under all circumstances add -9 to the kill command: kill -9 <PID (PROCESS ID)>]
<CTRL>-Z - puts process that is running in foreground (see below) of your terminal to sleep (i.e. stops it [stop here means pause])
<CTRL>-C - kills process that is running in foreground (see below) of your terminal (i.e. ends it permanently)

* pkill <NAME_OF_PROCESS(S)>
will kill all processes with the name you inputted [can also be used with -9]

* top
shows all currently running processes sorted in real time by CPU usage
hitting 'q' exits top

* htop
the same information as top but with a nicer display
hitting 'q' exits htop

Processes can either be:
foreground processes - these can be interacted with
background processes - these must be first switched to foreground to interact with them [Note: you may be able to see data being generated from a background process - you just cannot interact with the process (e.g. you cannot stop or kill it).]
* bg <JID> (see below under 'jobs' for info on JID)
background a process [Note: if you put an ampersand (&) at the end of a command that launches a process it will start as a background process, e.g. ping -c 300 google.com &]
* fg <JID>

* jobs
shows a list of all running and sleeping (called stopped [meaning paused]) jobs in your terminal, and the identifying number (JID [Job ID] - not the same as the PID) that has been assigned to them
-------------------------------------------------------
