IAM Enumeration
----------------
After compromising an AWS environment, AWS principals and credentials related to the environment can be enumerated in a number of ways:

The AWS Boto3 SDK (Python) provides access to AWS services through APIs. According to it's documentation Boto3 searches in the following locations in order to locate credentials when executing AWS command:

1)
Environment Variables: Boto3 searches for credentials defined as environment variables, namely:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

2)
Shared Credentials File: This file (typically ~/.aws/credentials) is a common storage location for IAM user access keys or configurations for assuming roles using Single Sign-On (SSO).

3)
AWS Config File: This file (typically ~/.aws/config) may reference credential sources such as helper scripts or external credential providers.

4)
Assume Role Provider: When using AWS SSO or similar mechanisms to assume a role via the AWS CLI, temporary credentials are cached for each role session at ~/.aws/cli/cache/{role_session_id}. Boto3 can utilize these cached credentials.

5)
Boto2 Config File (Legacy): Boto2, the predecessor to Boto3, may still be used in some older clients. Boto3 can search for credentials within the legacy Boto2 config file if present.

6)
Instance Metadata Service (IMDS): On Amazon EC2 instances with an IAM role configured, Boto3 can retrieve credentials through the Instance Metadata Service.

7)
Metadata Endpoints: Boto3 searches for credentials stored at the "metadata endpoint".

8)
AWS Elastic Container Service (ECS) tasks also have a metadata endpoint (http://169.254.170.2/v2/metadata) with a different credential storage mechanism.

9)
AWS Lambda functions store credentials as environment variables.

10)
AWS CloudShell utilizes a local host metadata endpoint for credential storage.

It is worth checking these locations after compromising an AWS environment in order to enumerate principals and creds.
