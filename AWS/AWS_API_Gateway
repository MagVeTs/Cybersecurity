AWS API Gateway
------------------
[from: https://tryhackme.com/room/awsapigateway]


API Components -

Endpoint: This is the URL location of the API, e.g., the address where you can "call" an API and the resources it can access on your behalf.

Method: This specifies the type of request being made to the API, such as GET, POST, PUT, DELETE, etc.

Headers: These are a component of HTTP, but are used by APIs to contain additional information about the request, such as authentication details, content type, and other metadata.

Request body: This is the data sent to the API as part of the request. GET requests won't typically have a request body, but POST, PUT, and DELETE requests almost always do.

Response: This is the data that the API sends in response to the request. It may include a status code, headers, and a response body.

API Purpose - 

APIs provide a granular mechanism for developers to allow user access to (potentially) sensitive "back-end" resources. Not only do APIs expose these capabilities for end users, but they also allow third-parties to build reliable ecosystems around a product that exposes an API. 

Furthermore, as mentioned, modern APIs often expose a number of sensitive "back-end" resources hosted on behalf of the API. These resources are often "micro-services" that proxy the user request as a direct database write or query to the various systems that may be supporting the API functionality. If security errors are made in the development of the API capabilities, they may be exposed to any user who can authenticate to the API or even to unauthenticated users who attempt to use the API. These characteristics make AWS API Gateway a prime target for attackers.

AWS API Gateway -

These API Gateways allow customers to deploy REST, HTTP/S, and WebSocket APIs while making use of "serverless" infrastructure; REST and HTTP/S APIs are similar to each other (https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html); WebSocket APIs allow bi-directional communication; WebSocket APIs can push data to clients who connected at some point without the need for the client to send another request.

API Gateway as the Integration Hub:

AWS API Gateway acts as a management layer for APIs, allowing them to interact with various backend resources within the AWS ecosystem. These interactions are known as integrations (https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-integration-settings.html). When a client sends a request to an API hosted behind API Gateway, it triggers the configured integration to handle the logic and potentially access other AWS services.

Lambda's Privileged Role:

Among all the available integrations, Lambda functions hold a unique position. API Gateway treats Lambda as the default service proxy for its endpoints. This means that Lambda functions are the primary target for routing incoming API requests. This tight coupling simplifies development as developers can focus solely on writing the Lambda function's logic without needing to worry about underlying server infrastructure.

Serverless Magic with Lambda:

Lambda functions are the embodiment of serverless computing. Developers write code snippets (typically in languages like Python, Node.js, Java) containing the desired functionality. API Gateway then manages the execution environment and triggers the Lambda function upon receiving an API request. This eliminates the need for server provisioning and management, offering a cost-effective and scalable solution.

Beyond Integrations: Lambda Authorizers for Granular Access Control

While Lambda functions are popular choices for integrations with API Gateway, they offer another powerful capability: Lambda authorizers. These custom-developed Lambda functions act as gatekeepers, enforcing access control on API Gateway endpoints.

Configurable Access Decisions:

Lambda authorizers provide fine-grained control by analyzing incoming API requests and making authorization decisions based on pre-defined criteria. This criteria can be tailored to your specific needs, leveraging factors like:

Request parameters: Validate specific parameters within the request to ensure they meet authorization requirements.
API keys or tokens: Implement token-based authentication mechanisms like JWT to identify and authorize requests.
Custom logic: Craft authorization rules based on any relevant data available to the Lambda function, enabling highly secure and dynamic access control.
Security Implications of Misconfiguration:

Improperly configured Lambda authorizers can introduce significant security vulnerabilities. If not implemented cautiously, they could grant unintended access to sensitive resources behind your API Gateway. It's crucial to thoroughly test and secure your authorizer functions to maintain a robust authorization layer.

AWS API Gateway: Functionality Overview
Integration Capabilities:
AWS Managed API G ateways are available 
Serverless Integration: API Gateway integrates with AWS Lambda to trigger serverless functions upon receiving API requests. Lambda functions handle request processing and response generation.
Microservices Communication: Facilitate communication and integration between microservices (servers, containers, or serverless functions) by creating, deploying, and managing APIs for each service. Further integration with messaging services (SNS, SQS, EventBridge) is supported.
Data Access: API Gateway seamlessly integrates with data storage services like Amazon DynamoDB and S3. This enables retrieval and modification of data as needed by API operations.
Real-time Communication: Establish bi-directional, real-time communication channels between clients and servers using WebSockets integrated with API Gateway.
API Management Suite: API Gateway offers a comprehensive suite for API monitoring, logging, and management. Gain insights into API usage patterns and maintain control over API behavior.
Security Features: Prioritizes security with OAuth 2.0 and IAM integration for access control. Additionally, SSL/TLS encryption safeguards data transmission.
Additional Notes:
API Gateway is a highly flexible and scalable service, enabling a wide range of integration possibilities beyond the listed functionalities.

API Gateway as a Reverse Proxy:

The AWS API Gateway service can be leveraged to function as a serverless reverse proxy. In this context, a reverse proxy acts as an intermediary between clients and a target server. It accepts client requests, forwards them to the target server, and relays the server's responses back to the clients. Traditional applications of reverse proxies include load balancing, caching, SSL termination, and concealing the identity of the backend server. 

Potential Misuse Cases:

While not the intended use case, malicious actors could potentially exploit API Gateway's reverse proxy functionality for the following purposes:

Identity Masking: Hackers might utilize the proxy to mask their true IP address while launching attacks on web servers or other targets.

IP Address Rotation: When configured as a "passthrough" proxy with a pool of IP addresses, API Gateway could be used to make requests appear as if they originate from any address within the pool See: https://bond-o.medium.com/aws-pass-through-proxy-84f1f7fa4b4b.

This could be used to:

Bypass IP-based Restrictions: Certain web applications or systems might block requests originating from specific IP addresses associated with suspicious activity. Rotating IP addresses could circumvent such restrictions.
Evasion of Detection: Security measures might identify and block requests from known security tester IP addresses. Rotating addresses could help evade such detection.
Simulating Real-world Scenarios: Real-world users access applications from diverse IP addresses. Rotating addresses allows for simulating these scenarios and potentially uncovering security vulnerabilities that might be exposed under varying IP origins.

There are different options available for rotating IP addresses when using a proxy: 1) use a rotating proxy service; automatically switches within a pool of proxy servers; each request sent from different IP address. 2)  manually switch between different proxy servers; one can manually configure proxy settings in browser to do so 3) use tool designed to facilitate quick switching between proxy servers
A tool called FireProx (created by Mike Felch ; Black Hills Information Security) grants this capability: https://github.com/ustayready/fireprox.
FireProx uses AWS API Gateway to rotate IP addresses for web requests. It uses an API Gateway endpoint to redirect requests to configured domain/IP.
Can be used for password spraying and other cred attacks (see: https://github.com/knavesec/CredMaster).
Can be used to make requests to HTTP/S or WebSocket endpoints that have IP-based restrictions or use rate-limiting.
See: MagVeTs/Cybersecurity/tools/FireProx

Lambda Authorizers for AWS API Gateway
Functionality:

Lambda authorizers are custom AWS Lambda functions that enforce authorization policies for API requests processed by API Gateway.
These functions execute prior to API request processing and determine access rights for specific resources protected by API Gateway.
The Lambda authorizer returns a policy document specifying whether a request is authorized or not.
Benefits:

Complex Authorization Logic: Enables implementation of intricate authorization rules within the Lambda function.
Reduced Infrastructure Management: Eliminates the need for separate infrastructure to handle authorization tasks.
Customizable Access Control: Provides flexibility in defining access requirements for API resources.
Offloading Resource-intensive Tasks: Leverages Lambda's serverless architecture for potentially resource-heavy authorization logic.

Cautions When Using Wildcards with Lambda Authorizers in API Gateway Paths
Greedy Wildcard Behavior:

The * wildcard in regular expressions is a greedy operator, matching the largest possible string within a path.
When employed in API Gateway path matching with Lambda authorizers, this can lead to unintended consequences if not used cautiously.
Example:

A path pattern like /resource/* with a greedy * might unintentionally match additional path segments beyond the intended /resource portion. This could grant access to unintended resources.

Mitigation Strategies:

Grouping and Lazy Quantifiers: Utilize grouping constructs (parentheses) and non-greedy quantifiers (e.g., *?) to precisely control the matching behavior. These ensure the wildcard only matches the desired segment of the path. [see here: "In the lazy mode, the quantifiers match their preceding elements as few as possible and return the smallest matches. When quantifiers use the lazy mode, they’re often referred to as non-greedy quantifiers or lazy quantifiers. To transform a greedy quantifier into a non-greedy quantifier, you add an extra question mark to it" [https://www.javascripttutorial.net/regular-expression-non-greedy/])

Security Implications:

Inadvertent authorization due to greedy wildcards can introduce security vulnerabilities. Unauthenticated users might gain access to restricted resources if unintended paths are matched by the authorization policy.
External Reference:

For a detailed analysis of this security concern in the context of AWS API Gateway, refer to "The Fault In Our Stars" by Tenchi Security (https://www.tenchisecurity.com/the-fault-in-our-stars/).

Abusing Greedy Expansion of Lambda Authorizer Policies
"[When pentesting] Once we identify an API, we would typically use a tool such as ffuf (https://github.com/ffuf/ffuf) or kiterunner (https://github.com/assetnote/kiterunner) to perform the discovery of API endpoints through fuzzing. These techniques and tools can help identify potentially interesting endpoints and opportunities to expose data or gain additional access."

