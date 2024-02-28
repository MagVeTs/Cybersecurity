General
--------

from:
https://tryhackme.com/room/cloud101aws ; Task 4 - More Reliable"
https://tryhackme.com/room/cloud101aws ; Task 5 - "Distributed Across the World (and in Space)"
https://tryhackme.com/room/awsbasicconcepts ; Task 2 - "Basic Concept — AWS Account and Root User"
https://tryhackme.com/room/awsbasicconcepts ; Task 5 - "Basic Concept — AWS Organizations"
https://tryhackme.com/room/awsbasicconcepts ; Task 6 - "Basic Concept — Virtual Private Cloud (VPC)"
https://tryhackme.com/room/introductiontoawsiam ; Task 2 - "Introduction to AWS IAM"
https://tryhackme.com/room/iamprincipals
https://tryhackme.com/room/iampermissions
https://tryhackme.com/room/resourcepoliciesscps
https://tryhackme.com/room/iamcredentials

Regions and Availability Zones
-------------------------------
"AWS defines a "region" as "a physical location around the world where we cluster data centers." A region will be made up of one or more "availability zones." These data centers that make up an availability zone will all be located within 60 miles of each other in the given region ... An Availability Zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. These separations mean that an outage of one AZ due to lost power, networking issues, or ISP connectivity issues should not affect any other AZ. AWS further intends for availability zones to be the key failover capability required by end-customers ... applications built on AWS are generally considered to be highly resilient if deployed in a multi-AZ configuration."

Naming Conventions
-------------------
"AWS names regions and availability zones are based on a common naming convention. For regions, names commonly start with one of a few different designations:

af (Africa)
ap (Asia Pacific)
ca (Canada)
eu (Europe)
me (Middle East)
sa (South America)
us (United States)
A cardinal direction (North, South, East, West, Central) or a combination (SouthEast, NorthWest) is appended to the abbreviation based on where the region is inside of the geography of the region (e.g., us-east for those data centers considered to be in the eastern USA). The convention follows with a numerical designation (1, 2, 3, etc.) based on whether it is the first, second, third, etc. region within the geographic location.

For example, af-south-1 is located in Cape Town, South Africa. It is a region on the African continent (af), in the southern portion of that geographic area (south), and the first such region (1). There are other designations that are less common such as US GovCloud, and those associated with AWS China, but the general naming convention can provide you with helpful context as you use AWS."

Fighting Latency
----------------
AWS regions allow geo-distribution of servers. This allows servers to be physically near client machines - cuts down on latency
AWS provides  CloudFront, the AWS Content Delivery Network (CDN) - "enables intelligent traffic routing and caching for end user requests" - cuts down on latency
AWS provides DNS service Route53 which "allows customers to route traffic based on traffic geo-location" - cuts down on latency
AWS provides EC2 Elastic Load Balancers (ELBs) - cuts down on latency

AWS Account
-----------
AWS account:
- container for AWS resources
- designated by a unique non-reusable 12-digit number, the Account ID
- acts as a security boundary by working with AWS Identity and Access Management (AWS IAM)

Root User
----------
- every account has root user connected with a specific email address
- a particular email can only be associated with a root user for one AWS account
- root user is IAM "superuser" with complete administrative permissions over associated AWS account
- even root users are NOT default MFA enforced; must be deliberately enabled
- there are tools that can enumerate root user email addresses, e.g.:
  Quiet Riot
  https://github.com/righteousgambit/quiet-riot
  "Unauthenticated enumeration of AWS, Azure, and GCP Principals"

AWS Organizations
------------------
* AWS provides a structure (known as an "AWS Organization") to allow large enterprises to manage their many AWS accounts.

* An AWS Organization contains a "parent container" called the "Organization Root"

* The Organization Root can contain many "Organizational Units (OUs)"

* OUs can themselves contain many nested OUs

* OUs can each contain many "AWS Accounts"

* Each AWS Account can contain many "User Accounts"

* An AWS Organization has a primary account to manage the whole AWS Organization; this account is called the "AWS Organization Management Account"

* The AWS Organization Management Account has an assigned role called  "OrganizationAccountAccessRole" which gives it access to any account within its AWS Organization (see https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html)

* Other User Accounts within the AWS Organization can be given privileges that allow them to "switch-role/assume-role" in regards to some of the administrative permissions held by the AWS Organization Management Account, thereby allowing them to perform needed admin duties within the AWS Organization

* The AWS Organization Management Account also hosts the logging capabilities for the whole AWS Organization using the AWS service called CloudTrail Organization Trail.

* The AWS Organization Management Account also hosts SSO capabilities using integrated IdPs like Azure AD or Okta.

* AWS Organizations have AWS Organization Policies (e.g. Service Control Policies [SCPs]) which can be configured to put access and privilege restrictions on OUs and Accounts.
NOTE: Organization Policies have no control over AWS Organization Management Accounts

Virtual Private Clouds (VPCs)
-----------------------------
* Many organizations set up their AWS infrastructure as VPCs: "a software-defined network topology that represents AWS's "traditional" network infrastructure offering for customers. VPCs allow AWS users to restrict the connectivity to sensitive resources designed to be isolated or segmented from other workloads, and critically, from the public internet".

* VPCs often contain:

- Internet gateway - between VPC and internet
- Egress-only internet gateway - IPv6 IP address allowed to initiate outbound connections to the internet; blocks inbound.
- Carrier gateways - to telecommunications carrier networks.
- NAT gateways - Network Address Translation service (NAT) gateways; connect private subnets to services outside VPC
- DHCP - "by default, all EC2 instances (VMs) in a non-default VPC receive an unresolvable host name assigned by AWS. This can be updated to leverage custom domains." 
- DNS - "by default, AWS provides DNS resolution to VPCs via the Route 53 Resolver, a global AWS DNS service."
- Public and Elastic IP addressing -  "AWS maintains over 100 million public IPv4 IP addresses. Many of these addresses can be assigned by customers to specific resources. When using a Public IP address (AWS term), if the associated EC2 instance is stopped, the IP address will be reallocated to AWS, and a new IP address will be assigned if the public EC2 instance is ever restarted. However, with an Elastic IP address, the IP address is allocated to an AWS account ongoing and can be assigned to arbitrary resources as the customer chooses."

IAM (Identification and Access Management)
------------------------------------------
- Recognizes IAM Users and IAM Roles
- IAM Users = "combine authentication, identity, and authorization into a single unit"
- IAM Roles =  "typically delegate the authentication and identity to another system and primarily manage authorization"

ARN (Amazon Resource Name)
--------------------------
-  IDs a resource uniquely across the entirety of AWS
- used for identifying a resource in IAM policies, Amazon Relational Database Service (Amazon RDS) tags, API calls, etc.
- ARN made up of AWS Region, AWS Account ID, Service, and resource identifiers such as the resource name
- ARN structure cheat sheet (from: https://towardsthecloud.com/amazon-resource-names-arns):

arn:partition:service:region:account-id:resource-id
arn:partition:service:region:account-id:resource-type/resource-id
arn:partition:service:region:account-id:resource-type:resource-id

partition – is the location where the resource is located. The available options are: aws, aws-cn and aws-us-gov.
service – is the AWS service name that’s being used as a reference. For the ARN format, you need to use the service prefix name (see 2nd column in the table at: https://towardsthecloud.com/amazon-resource-names-arns).
region – is the region that’s being used in your AWS account for the deployment of your AWS services/resources e.g. eu-central-1 for the data center in Frankfurt.
account-id – is the ID of the AWS account that owns the resource, this typically consists of 12 numbers, and here are instructions on how to find it on your account: https://towardsthecloud.com/find-aws-account-id.
resource-id – is a unique identifier to distinguish multiple resources from the same AWS resource.
resource-type – AWS Services contain different types of resources, hence the resource type attribute. This lets you specify the resource in a more granular detail e.g. the service Amazon EC2 has a resource type called VPC.

IAM Identities aka IAM Principals
------------------------------------
- Used to access AWS Accounts and their resources through authentication and authorization
- define who/what is allowed access

- One type of IAM Identity/Principal is: IAM Users
- IAM Users can be person or an app
- IAM Users exist within one AWS Account
- IAM Users may have:
* LoginProfile = password to access AWS Web Console
* Access Keys (up to two); keys are generated by AWS; each Access Key is comprised of a Key ID and a Secret

- Another type of IAM Identity/Principal is: IAM Role
- IAM Role can apply to a person, Service, or Resource
- It allows the person/Service/Resource to carry out a certain action (e.g. a specific EC2 instance might be assigned an IAM Role that allows it to interact in some way with an S3 bucket)
- Each IAM Role has its own "AssumeRoleTrust Policy" that dictates what Principals can assume that role


IAM Groups
----------
* IAM Users can be added to IAM Groups and permissions can be set for the group which are then inherited by all users that are member of that group

IAM Policies vs. Resource Policies vs. Service Control Policies (SCPs)
-----------------------------------------------------------------------
IAM Policies - attached to IAM Principal; define resources upon which principal can act
Resource Policies - attached to Resource; define Principals allowed to act on Resource
Service Control Policies (SCP)- set by AWS Organizations; sit outside AWS Accounts; part of an organization's Mangement Account; apply to all users in accounts including root users; used to prevent disabling of logging or other problematic actions

IAM Credentials
---------------
Root
- root account; enjoying all privileges
- Note: for accounts created through AWS Organizations using API call CreateAccount the root password will be randomly generated and not viewable; in orser to login as root the password must first be reset
- to login as root or to reset the root password, visit: https://signin.aws.amazon.com/signin ;from there one can choose to login as root or as a regular IAM User

AWS Access Keys
----------------
- access keys are used to interact with AWS API
- AWS Console also uses access keys on its backend

- two types of access keys:

1) Long Term Access Keys
- begin with the string `AKIA` (Access Key ID)
- contain: Access Key ID and Secret Access Key
- do not expire; best practice is to rotate them on a regular basis
- only available for IAM Users and the Root User
- best practice not to generate them for Root User
- Root User/IAM User can only have two Access Keys at one time
- both the Access Key ID and the Secret Access Key are generated by AWS
- access keys can be set to be inactive
- created in AWS Console or AWS CLI:
user@machine$ aws iam create-access-key --user-name <USER_NAME>

2) Temporary Session Keys
- begin with the string `ASIA` (Access Key ID)
- contain: Access Key ID, Secret Access Key, and Session Token
- have expiration date
- cannot be deleted or set to inactive
- generated by AWS Security Token Service (sts):
user@machine$ aws sts get-session-token







