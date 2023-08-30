PlumHound (sister program to BloodHound; you must have neo4j and BloodHound running to use PlumHound; see BloodHound in Tools in this repository)

"Although BloodHound is a powerful tool to graph Active Directory, it can be mind-bending to correlate between information on maps of large networks ... To end the confusion over graphs, a new tool was introduced: PlumHound. PlumHound ... operates by wrapping BloodHoundAD’s Neo4J backend cipher queries into reports ... BloodHound should be active to generate reports with PlumHound."
from: "BloodHound + PlumHound = ❤" [https://cesidt.medium.com/bloodhound-plumhound-bbd5f8a60f00]

----------
https://github.com/PlumHound/PlumHound

* see: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course ; "Domain Enumeration with Plumhound" - https://academy.tcm-sec.com/courses/1152300/lectures/48515111
syntax:
$ cd /opt
$ sudo git clone https://github.com/PlumHound/PlumHound.git
$ cd PlumHound
$ sudo pip3 install -r requirements.txt
$ sudo python3 PlumHound.py --easy -p <your_neo4j_password>
- this command is done to make sure that PlumHound is working properly; it does a very basic domain query that does not generate much info; if it executes the task correctly you move on to other more helpful queries
$ sudo python3 PlumHound.py -x tasks/default.tasks -p <your_neo4j_password>
- this is the default task for PlumHound; see the GitHub documentation for other options; however, HA says that the default works very well
- the output is many report files which are placed in the reports/ directory; PlumHound also creates a zip file of all the reports in that directory
- one of the output files is index.html; that is the one you can use to see all the reports in your browser
$ cd reports
$ firefox index.html



