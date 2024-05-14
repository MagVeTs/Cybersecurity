EC2
---

------------------------------------------------------------------------------------------------------------
Connecting to an EC2 to Administrate It
----------------------------------------

[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 4 - "Connecting to your EC2 Instance"]

SSH 
----
- used from Linux machines; use public/private key pair created during creation of EC2
- NOTE: best security practice is to place EC2 server in private subnet without public IP address. In such cases, in order to connect using SSH from another device one would first set up a proxy jump host that is tunneled to the EC2 and has a public IP, then one would connect to the EC2 by way of the jump host. Another option is to set up a VPN.

RDP
----
- used from Windows machines
- the SSH Key is needed to decrypt the Administrator Password; this is then used to sign in using RDP (Remote Desktop Protocol)

EC2 Connect
------------
- a newer AWS service called EC2 Instance Connect can be used
- it is a browser-based ssh interface 
- it uses temporary SSH public/private key pairs deployed by an agent using AWS IAM Permissions.


AWS SSM
-------

EC2 Serial Console
-------------------

Summary of the major ways to connect to an EC2 Instance
Method	        Requires Direct Network Access	Requires Agent	Requires EC2 IAM Permissions
Direct SSH/RDP	          YES	                        NO	                    NO
EC2 Instance Connect	    YES	                        YES                     NO
                                              (Installed on amazon linux2)	    
SSM Run Command	           NO	                        YES	                    YES
SSM Session Manager	       NO	                        YES	                    YES
EC2 Serial Console	       NO	                        NO                      NO
                                         (but users must have a password set)
------------------------------------------------------------------------------------------------------------

EC2 instances connecting to services using Instance MetaDataService (IMDS)
[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 5 - "Instance Permissions"]


- EC2 instances can connect to services using IMDS which listens on 169.254.169.254 and is a component of AWS Hypervisor
CLI commands using EC2 Instance Console to connect to the instance and work with its IMDS:

user@machine$ role_name=$( curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/ )
user@machine$ echo "Role Name is $role_name"
# gets the role name; stores role name in environment variable role_name; and echoes out role name

user@machine$ curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/${role_name}
# request session credentials for role

user@machine$ instance_id=$( curl -s http://169.254.169.254/latest/meta-data/instance-id )
user@machine$ echo "My Instance ID is $instance_id"
user@machine$ aws ec2 modify-instance-metadata-options --instance-id $instance_id --http-tokens required --region us-east-1
# enable IMDSv2 (safer than IMDSv1); require token to call instance metadata

user@machine$ TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
user@machine$ echo $TOKEN
# get the token; token set for 21,600 seconds = 6 hours

user@machine$ role_name=$( curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/ )
user@machine$ echo "Role Name is $role_name"
user@machine$ curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/${role_name}
# get credentials
# `-H "X-aws-ec2-metadata-token: $TOKEN"` = "adds a custom header to your HTTP call. This makes it much more difficult to leverage standard SSRF exploits to access and exfiltrate AWS credentials via the IMDS."
------------------------------------------------------------------------------------------------------------
[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 6 - "EC2 Networking & Storage"]

EC2 Networking
---------------
 * EC2 Networking makes use of the Elastic Network Interface (ENI)
* Each EC2 Instances has an ENI ; it is possible to configure multiple ENIs for an instance (used as a network device between two subnets, to add network capacity, or to provide a failover)
* Each ENI has at least one Security Group to define what IP source addresses, ports, and protocols may communicate with ENI
* By AWS Network Security default EC2's can only recieve traffic addressed to their IP; they can only send traffic originating in their IP; in order to use an EC2 as NAT/firewall/router disable this default check of source/destination

[in: AWS CLI / CloudShell]
$ aws ec2 describe-network-interfaces | jq '.NetworkInterfaces[0]'
# helps understand netwotk topology outputs info re network interfaced; e.g. public IP, Private IP, and name/ID of Security Group, Subnet, and VPC

(from ChatGPT, more info on the command:
"This command utilizes the AWS Command Line Interface (CLI) to describe network interfaces of EC2 instances. Let's break down the components:

- `aws ec2 describe-network-interfaces`: This part of the command instructs the AWS CLI to retrieve information about network interfaces associated with EC2 instances. It communicates with the EC2 service in your AWS account to fetch this information.

- `|`: This symbol is the pipe operator in Unix-like operating systems. It takes the output from the preceding command (`aws ec2 describe-network-interfaces`) and passes it as input to the next command.

- `jq '.NetworkInterfaces[0]'`: This part of the command utilizes `jq`, a lightweight and flexible command-line JSON processor. The command `.NetworkInterfaces[0]` is a filter applied by `jq` to the JSON output received from the previous command. It selects the first element (`[0]`) from the array of network interfaces (`NetworkInterfaces`). Essentially, it extracts information about the first network interface returned by the `aws ec2 describe-network-interfaces` command.

In summary, the entire command fetches information about network interfaces associated with EC2 instances using the AWS CLI and then uses `jq` to filter and extract details about the first network interface from the JSON output. This could be useful for scripting or automation purposes where you want to extract specific information about network interfaces."

------------------------------------------------------------------------------------------------------------
[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 6 - "EC2 Networking & Storage"]

EC2 Storage
------------
* Amazon Elastic Block Store (EBS) provides hard disk storage for EC2 Instances
* hard disks are called EBS Volumes and may be SSD, HDD, or IOPS; available capacity: 1GB - 64TB
* EBS Volumes provide snapshotting; used for backup and sharing; EBS Snapshots stored in Amazon S3 Buckets to save money
* some types of EC2 instances can have ephemeral storage; these use SSD drives present in the device; ephemeral storage automatically erased on reboot; snapshots cannot be stored on ephemeral storage
* both EBS Volumes and Snapshots are able to be encrypted; different types of KMS Encryption is available
* EBS Snapshots able to be shared across AWS Accounts 
* Note: danger exists that they may contain sensitive data, source code, or secrets

CLI commands to:
1) grab a public EBS Snapshot
2) use it to create an EBS Volume
3) mount the EBS Volume to an EC2 instance
4) the volume can now be accessed and searched for secrets

[in: AWS CLI / CloudShell
$ aws ec2 describe-snapshots --snapshot-ids <SNAPSHOT_ID_NUMBER(s)>
# gather info about a discovered snaoshot; e.g. encryption, volume size, AWS account in which it was created

[in: EC2 Instance Console]
$  TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
$ curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone
# discover Availability Zone (AZ) of instance (this is a subcategory of Region); this is needed for the next step (creating the volume) because volumes must be in the same AZ as the machine they are mounted to

[in: EC2 Instance Console]
$ aws ec2 create-volume --snapshot-id <SNAPSHOT_ID_NUMBER> --volume-type gp3 --region <REPLACE-WITH-REGION> --availability-zone <REPLACE-WITH-AZ>
# create volume from snapshot
# gp3 was chosen for `--volume-type` because it is cheap
# make sure to note volume-ID in output in order to use it for the next step

[in: EC2 Instance Console]
$ instance_id=$( curl  -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id )
$ aws ec2 attach-volume --region <REPLACE-WITH-REGION> --device /dev/sdh --instance-id $instance_id --volume-id vol-REPLACE-WITH-YOUR-VOLUME_ID>

[in: EC2 Instance Console]
$ sudo fdisk -l
# check on new volume; output includes size of volume and name (e.g. /dev/nvme0n1p1)

(from ChatGPT, more info on the command:
"In the context of AWS CLI, the command sudo fdisk -l doesn't directly interact with AWS services. Instead, it's a Linux command typically used to list the partition tables for all disks on the system. Here's what each part of the command does:

sudo: This command is used to execute another command with elevated privileges, typically requiring administrative permissions. It stands for "superuser do."

fdisk: This is a command-line utility used for disk partitioning. When invoked with the -l option, it lists the partition tables for all disks attached to the system.

So, when you run sudo fdisk -l in the context of AWS CLI, it will display information about the disk partitions on the local EC2 instance. This command does not directly interact with AWS services; rather, it provides information about the local storage configuration of the EC2 instance.")

[in: EC2 Instance Console]
$ sudo mkdir /snapshot-recovery
$ sudo mount /dev/nvme1n1 /snapshot-recovery
# mount new volume (in this case called: /dev/nvme1n1)

[in: EC2 Instance Console]
$ ls /snapshot-recovery
# now the volume can be searched for secrets
------------------------------------------------------------------------------------------------------------
[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 7 - "EC2 Configuration"]


[command issued from CloudShell]
$ aws ec2 describe-images --owners 019181489476
# see a list of Amazon Machine Images (AMIs) available to your account that were configured by the 019181489476 (TryHackme AWS Development) account
# omitting the `--owners` flag will pull a list of all available AMI's - which will be too big to handle and will time out

------------------------------------------------------------------------------------------------------------
[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 7 - "EC2 Configuration"]

EC2 instances can be configured using UserData (which may contain secrets).
The UserData can be accessed within an instance by going to:
/var/lib/cloud/instance/scripts/part-001
as root (sudo or su)

Another way to access the UserData of an instance is to connect to it using EC2 Instance Connect or the SSM Session Manager and to issue the following commands:

[commands issued from EC2 Instance Connect or the SSM Session Manager]
$  TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
$  instance_id=$( curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id )
$  aws ec2 describe-instance-attribute --attribute userData --instance-id $instance_id --region us-east-1 --query UserData --output text  | base64 -d
#  takes output of `describe-instance-attribute` call; pulls UserData field (--query UserData); pipes through base64 decode to make readable the shell script


(Info from ChatGPT that breaks down the commands nicely:
"These commands are used in conjunction with the AWS Command Line Interface (CLI) to retrieve metadata and user data from an EC2 instance in the AWS cloud. Let's break down each command:

1. `TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")`

   - This command uses the `curl` command-line tool to send an HTTP PUT request to a specific URL (`http://169.254.169.254/latest/api/token`). This URL is a well-known IP address within AWS EC2 instances that provides metadata and other information.
   - The `-s` option is used to silence the progress output of `curl`.
   - The `-X PUT` option specifies that the HTTP request method should be PUT.
   - The `-H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` option sets a custom HTTP header named `X-aws-ec2-metadata-token-ttl-seconds` with a value of `21600`. This header specifies the time to live (TTL) for the token.
   - The response from this request is expected to contain a token that will be stored in the `TOKEN` variable for later use.

2. `instance_id=$( curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/instance-id )`

   - This command uses the `curl` command-line tool to send an HTTP GET request to another URL (`http://169.254.169.254/latest/meta-data/instance-id`), which is another well-known URL for retrieving instance metadata.
   - The `-H "X-aws-ec2-metadata-token: $TOKEN"` option sets a custom HTTP header named `X-aws-ec2-metadata-token` with the value of the previously retrieved token stored in the `TOKEN` variable.
   - The `-s` option is used to silence the progress output of `curl`.
   - The response from this request is expected to contain the instance ID of the EC2 instance, which will be stored in the `instance_id` variable for later use.

3. `aws ec2 describe-instance-attribute --attribute userData --instance-id $instance_id --region us-east-1 --query UserData --output text | base64 -d`

   - This command uses the AWS CLI (`aws ec2`) to describe an instance attribute called `userData` for the specified instance ID (`$instance_id`).
   - `--region us-east-1` specifies the AWS region to use (in this case, US East 1). You may need to adjust this to match your region.
   - `--query UserData --output text` specifies that the output should be in text format and should contain the value of the `UserData` attribute.
   - The output of the `aws ec2 describe-instance-attribute` command, which is base64 encoded, is then piped (`|`) to the `base64 -d` command, which decodes the base64-encoded user data.
   - The final output of this command should be the decoded user data associated with the specified EC2 instance.

Overall, these commands are typically used within a script or automation to retrieve instance metadata and user data from within an EC2 instance in the AWS cloud.")
------------------------------------------------------------------------------------------------------------
[from: https://tryhackme.com/room/amazonec2attackdefense ; Task 8 -  "Load Balancers, Launch Configs, and AutoScaling"; rewritten by ChatGPT]

"Many web applications hosted in the cloud are set up to automatically adjust their capacity, a process known as "auto scaling." This means that the application can dynamically increase or decrease the number of server instances it's running based on the current demand. This approach is cost-effective because it allows companies to utilize the cloud provider's surplus resources during peak usage instead of investing in hardware that may only be needed occasionally.

In the realm of EC2 Auto Scaling, there are three main components:

1. Elastic Load Balancers (ELBs) distribute incoming requests among a variable number of instances. They often trigger the addition or removal of instances based on demand.
2. Launch Configurations contain the specifications needed to create a new instance, such as the Amazon Machine Image (AMI) and instance type.
3. The Auto Scaling Group (ASG) is responsible for monitoring capacity and managing the creation or termination of instances in response to changes in demand.

From a security standpoint, a few key considerations apply to EC2 Auto Scaling:

- When scaling down, ASGs prioritize terminating the oldest instance. This means that the instance with the longest exposure to potentially untrusted traffic is usually the first to be removed.
- Only the Load Balancer needs to be publicly accessible. The ELBs handle external traffic and then forward it internally to the EC2 instances using private Virtual Private Cloud (VPC) addressing. As a result, the EC2 instances don't require public IP addresses.
- Depending on the type of Load Balancer used, it can handle the termination of encrypted TLS connections using the free AWS Certificate Management (ACM) system. Advanced Load Balancers like Application Load Balancers (ALBs) can also be equipped with an AWS Web Application Firewall (WAF), which helps detect and block common layer-7 (application layer) attacks as defined by OWASP (Open Web Application Security Project)."
------------------------------------------------------------------------------------------------------------
[from: https://tryhackme.com/room/amazonec2dataexfiltration ; Task 3 - "Phase 1 - Initial Access / Credential Access"]

aws elbv2 describe-load-balancers --query LoadBalancers[].DNSName --output text
# after using `aws configure` command to sign-in to a specific AWS account and a particular region within that account
# list all load balancers in account in chosen region; display only their DNS Name

------------------------------------------------------------------------------------------------------------
Issue command from Attack Box CLI:

user@machine$ aws ec2 describe-instances   --query 'Reservations[*].Instances[*].[Tags[?Key == `Name`].Value,InstanceId,State.Name,InstanceType,PublicIpAddress,PrivateIpAddress]' --profile <PROFILE_NAME> --output text | sed 'N;s/\n/ /'
# discovers all EC2 instances in a Profile's account; returns a list that includes EC2 Name, InstanceId, Status (running, stopped, etc), and Public and Private IPs
# removing `--query` parameter and `sed`, and changing `--output` to json will return full data on each instance
[from: https://tryhackme.com/room/amazonec2dataexfiltration]
------------------------------------------------------------------------------------------------------------
Issue command from Attack Box CLI:

user@machine$ LIST=`aws ec2 describe-instances --region <REGION> --query Reservations[].Instances[].InstanceId --output text --profile <PROFILE_NAME>
# retrieves list of all EC2 Instance IDs in Profile's account; saves Instance IDs as "environment variable" called: LIST

user@machine$ for i in $LIST ; do
  aws ec2 describe-instance-attribute --profile <PROFILE_NAME> --instance-id $i --attribute userData --output text --query UserData --region us-east-1 | base64 --decode > $i-USERDATA.txt
done
# shell command; consults the list of all instances (from environment variable LIST), and in "for" loop, downloads user data file for each instance, then base64 decodes the contents of each user data file into a separate text file [one for each instance]

[from: https://tryhackme.com/room/amazonec2dataexfiltration]
------------------------------------------------------------------------------------------------------------



