Burp Suite and Foxy Proxy
---------------------------

Burp Suite
-----------
* Burp Suite is preinstalled on Kali Linux
* Download latest Burp Suite release: https://portswigger.net/burp/releases


Foxy Proxy
------------
* Install Foxy Proxy (for the Firefox browser):
- https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/
[Standard has an extra function called "Patterns" that "basic" does not have; see here: https://proxyway.com/guides/foxyproxy-chrome-firefox]
- https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-basic/
* see: https://tryhackme.com/room/burpsuitebasics ; Task 9 - "Connecting through the Proxy (FoxyProxy)"
-----------------------------------------------------------------------------------------------------------------------------------------------------
Guides to Burp Suite (and Foxy Proxy):

* https://tryhackme.com/room/burpsuitebasics
* https://tryhackme.com/room/burpsuiterepeater

------------------------------------------------------------------------------------------------------------------------------------------------------
Extensive introduction to Burp Suite: https://tryhackme.com/room/burpsuitebasics


from: https://tryhackme.com/room/burpsuitebasics ; Task 2 - "What is Burp Suite"
"In essence, Burp Suite is a Java-based framework designed to serve as a comprehensive solution for conducting web application penetration testing. It has become the industry standard tool for hands-on security assessments of web and mobile applications, including those that rely on application programming interfaces (APIs).

Simply put, Burp Suite captures and enables manipulation of all the HTTP/HTTPS traffic between a browser and a web server. This fundamental capability forms the backbone of the framework. By intercepting requests, users have the flexibility to route them to various components within the Burp Suite framework ... The ability to intercept, view, and modify web requests before they reach the target server or even manipulate responses before they are received by our browser makes Burp Suite an invaluable tool for manual web application testing ... Burp Suite Community Edition ... is freely accessible for non-commercial use within legal boundaries ... Burp Suite also offers Professional and Enterprise editions, which come with advanced features and require licensing"
-----------------------------------------------------------------------------------------------------------------------------------------------------
from: https://tryhackme.com/room/burpsuitebasics ; Task 13 - "Proxying HTTPS"

"When intercepting HTTP traffic, we may encounter an issue when navigating to sites with TLS enabled. For example, when accessing a site like https://google.com/, we may receive an error indicating that the PortSwigger Certificate Authority (CA) is not authorised to secure the connection. This happens because the browser does not trust the certificate presented by Burp Suite."

In order to fix this issue we need to add the Port Swigger (Burp Suite) CA to the list of accptable certificate authorities
We do this by uploading Port Swigger's certificate and authorizing the bearer of that certificate (Burp Suite) to act as CA for visited domains.
The steps to do this in the Firefox browser are as follows:

"1. Download the CA Certificate: With the Burp Proxy activated, navigate to http://burp/cert. This will download a file called cacert.der. Save this file somewhere on your machine.

2. Access Firefox Certificate Settings: Type about:preferences into your Firefox URL bar and press Enter. This will take you to the Firefox settings page. Search the page for "certificates" and click on the View Certificates button.

3. Import the CA Certificate: In the Certificate Manager window, click on the Import button. Select the cacert.der file that you downloaded in the previous step.

4. Set Trust for the CA Certificate: In the subsequent window that appears, check the box that says "Trust this CA to identify websites" and click OK."

from: https://tryhackme.com/room/burpsuitebasics ; Task 13 - "Proxying HTTPS"
------------------------------------------------------------------------------------------------------------------------------------------------------
see: Heath Adams - The Cyber Mentor ; Practical Ethical Hacking - The Complete Course
Lab Setup - https://academy.tcm-sec.com/courses/1152300/lectures/47848127 (starting at approximately 06:34 in the video)
------------------------------------------------------------------------------------------------------------------------------------------------------



