FireProx
---------

[from: https://tryhackme.com/room/awsapigateway ; Task 5 - "Using API Gateway for Offensive Purposes"]

https://github.com/ustayready/fireprox


There are different options available for rotating IP addresses when using a proxy: 1) use a rotating proxy service; automatically switches within a pool of proxy servers; each request sent from different IP address. 2)  manually switch between different proxy servers; one can manually configure proxy settings in browser to do so 3) use tool designed to facilitate quick switching between proxy servers
A tool called FireProx (created by Mike Felch ; Black Hills Information Security) grants this capability: https://github.com/ustayready/fireprox.
FireProx uses AWS API Gateway to rotate IP addresses for web requests. It uses an API Gateway endpoint to redirect requests to configured domain/IP.
Can be used for password spraying and other cred attacks (see: https://github.com/knavesec/CredMaster).
Can be used to make requests to HTTP/S or WebSocket endpoints that have IP-based restrictions or use rate-limiting.

Initial Commands:

user@machine$ git clone https://github.com/ustayready/fireprox

user@machine$ cd fireprox

user@machine$ pip3 install -r requirements.txt

user@machine$ python fire.py
# outputs help info

Usage:

1) Create a FireProx endpoint to use as a proxy that will switch IP address with each request:

user@machine$ python fire.py --command create --url https://api.examplecompany.com
Creating => https://api.examplecompany.com...
[2024-04-27 23:10:07-06:00] (bnyqzbg5pc) fireprox_examplecompany => https://bnyqzbg5pc.execute-api.us-east-1.amazonaws.com/fireprox/ (https://api.examplecompany.com)
# creates a FireProx endpoint (known in this case as `bnyqzbg5pc`) to interact with https://api.examplecompany.com

2) Use a proxy such as Burp Suite (or curl command from CloudShell) to interact with https://api.examplecompany.com; each request from https://bnyqzbg5pc.execute-api.us-east-1.amazonaws.com/fireprox/ to https://api.examplecompany.com will come from a different IP address.

3) When finished interacting with https://api.examplecompany.com delete https://bnyqzbg5pc.execute-api.us-east-1.amazonaws.com/fireprox/.

If you do not remember name of created endpoint you can first list them with the command:

user@machine$ python fire.py --command list
Listing API's...
[2024-04-27 23:19:12-13:00] (bnyqzbg5pc) fireprox_examplecompany: https://bnyqzbg5pc.execute-api.us-east-1.amazonaws.com/fireprox/ => https://api.examplecompany.com/

Then delete the endpint with the command:
user@machine$ python fire.py --command delete --api_id bnyqzbg5pc                                      
Deleting bnyqzbg5pc => Success!


















