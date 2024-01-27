Linux Services (called daemons)

[from: Network Chuck - start, stop, restart Linux services (daemon HUNTING!!) // Linux for Hackers // EP 6 ; https://www.youtube.com/watch?v=wOWhfNB_r-0&list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL&index=7]
- Linux services (called daemons) can be identified by the letter "d" appended to their name (e.g. the service that provides SSH is called sshd)
- systemd - the so-called master daemon that all the other services (in this context referred to as as units), "fork" out from (a process tree). Systemd is an initialization system and service manager for all other services.

commands:
systemctl is the basis for the commands to control Linux services. It interacts with systemd which contols Linux services (daemons).

* sudo systemtemctl stop <NAME_OF_SERVICE>
stop a Linux service from running
* sudo systemtemctl start <NAME_OF_SERVICE>
start a Linux service that has been stopped or not yet started
* sudo systemtemctl restart <NAME_OF_SERVICE>
stop and restart a Linux service (this is often used when a service is not working properly; often restarting it will fix the problem)
* sudo systemtemctl reload <NAME_OF_SERVICE>
reloads services configuration without restarting; not available for all services; you can also use the command 'sudo systemtemctl reload-or-restart <NAME_OF_SERVICE>' and it will reload if it can and if not it will restart
* sudo systemtemctl disable <NAME_OF_SERVICE>
will prevent service from starting at boot; however, if service is running now it will continue running
* sudo systemtemctl enable <NAME_OF_SERVICE>
will cause the service to start at boot
* sudo systemtemctl status <NAME_OF_SERVICE>
check status of a Linux service 
- if under "Active:" it says "inactive (dead)" the service is stopped; if it says "active (running) the service is running
- if a service is running but has been disabled from starting at boot it will have "disabled" listed under "Loaded"
* sudo systemctl list-units
lists all active services (you can '| grep <NAME_OF_SERVICE>' to pull out specific service you are interested in)
* sudo systemctl list-units --all
lists active and inactive services
* sudo systemctl list-unit-files
lists the files of all services on the system; including files that have not yet been parsed and loaded into memory
* sudo journalctl -xe
- journalctl is the logs for systemd; it enables you to troubleshoot issues with services; this command will let you view all the logs; you can grep for a particular service that you are interested in
