Lambda
---------

[from: https://tryhackme.com/room/awslambda]

Lambda exposes several avenues for misconfiguration or exploitation, with insecure code being a primary concern. Given that Lambda functions often trigger based on user-generated events, failure to properly validate user inputs can open the door to security compromises.

Another risk stems from the inadvertent exposure of sensitive data through STDOUT, which then becomes visible in CloudWatch logs, accessible to any account with read permissions.

Misconfigurations in execution roles pose an additional threat. Overly permissive roles grant excessive permissions, magnifying the potential impact of any code vulnerabilities exploited by attackers. Role Permissions, accessible via environment variables like AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, if compromised, could lead to privilege escalation or data exfiltration.

Despite user-defined environment variables being encrypted (using KMS), they are often easily accessible, either within the function or through APIs and the AWS Console. Consequently, secrets passed through environment variables are vulnerable to exfiltration.

Security misconfigurations may also arise from how Lambda functions are invoked, particularly if the resource policy is flawed. For instance, using overly permissive resource policies could grant unauthorized users the ability to upload new code, posing a significant security risk.

Fpr example: typically associated with the `lambda:invokeFunction` IAM Action, substituting `lambda:*` instead grants the principal the capability to upload new code. Also, introducing a resource policy that permits access to all AWS users (i.e., `Principal: *`) poses a significant security risk.

Understanding Lambda concurrency is crucial for both attackers and defenders. Attackers can exploit concurrency limits for Denial of Service attacks, while defenders can mitigate such attacks by implementing reserved concurrency and understanding throttling mechanisms.

Manipulating Lambda layers provides a means to inject malicious code into numerous functions, amplifying the scope of potential attacks.

Lastly, leveraging the lambda:GetFunction API can aid in discovering pre-signed URLs for downloading code zip files, potentially exposing hardcoded sensitive information in applications.

---------------------------------------------
[from: https://tryhackme.com/room/lambdadataexfiltration]

user@machine$ aws lambda list-functions
