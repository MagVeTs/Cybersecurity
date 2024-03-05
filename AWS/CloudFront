CloudFront
-----------

from: https://tryhackme.com/room/awss3service ; Task 4 - "CloudFront Overview"

* CloudFront is AWS's Content Distribution Network (CDN) service
* it distributes a particular website's content to web servers around the worl in order to cut down on latency
* CloudFront can also provide the ability to set restrictions on access based on geolocation or other factors
* CloudFront also works with other AWS services such as an AWS WAF and the AWS anti-DDoS service called AWS Shield
* CloudFront must draw the data and code that it distributes to servers around the world from some origin S3 bucket, EC2 instance, or other AWS service this is known as the CloudFront Origin and may be a target of attack
* Only CloudFront should be able to access the CloudFront Origin; there should be no direct access to the Origin; this can be accomplished by creating a proper Origin Access Identity (OAIs) as a Resource-based Policy for the resource that is acting as the Origin
* as an example:
{ "Sid": "1", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EAF5XXXXXXXXX" }, "Action": "s3:GetObject", "Resource": "arn:aws:s3:::{your_bucket}/*" }
- this OAI will ensure that only the correct CloudFront service can access the S3 bucket; the bucket can not be accessed directly
