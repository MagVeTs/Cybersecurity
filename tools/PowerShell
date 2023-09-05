PowerShell 
-----------

also see: privilege_escalation > WindowsOS in this repository

--------------------------
[from: https://tryhackme.com/room/powershell ; with some editing, etc.]
"Powershell is the Windows Scripting Language and shell environment built using the .NET framework.
This also allows Powershell to execute .NET functions directly from its shell. Most Powershell commands, called cmdlets, are written in .NET. Unlike other scripting languages and shell environments, the output of these cmdlets are objects - making Powershell somewhat object-oriented.
This also means that running cmdlets allows you to perform actions on the output object (which makes it convenient to pass output from one cmdlet to another). The normal format of a cmdlet is represented using Verb-Noun; for example, the cmdlet to list commands is called Get-Command
Common verbs to use include:
Get
Start
Stop 
Read
Write
New
Out
To get the complete list of approved verbs, visit this link: https://learn.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.3

PS > Get-Command
- lists all cmdlets currently installed on the machine

PS > Get-Command <verb>-*
OR
PS > Get-Command *-<noun>
- displays all cmdlets that include the given verb or noun

PS > Get-Help <name_of_a_cmdlet>
- displays info about a cmdlet

PS > Get-Help <name_of_a_cmdlet> -Examples
- displays info about a cmdlet and gives usage examples

Object Manipulation
--------------------
... the output of every cmdlet is an object. If we want to manipulate the output, we need to figure out a few things:

passing the output to other cmdlets
using specific object cmdlets to extract information
The Pipeline(|) is used to pass output from one cmdlet to another. A major difference compared to other shells is that Powershell passes an object to the next cmdlet instead of passing text or string to the command after the pipe. Like every object in object-oriented frameworks, an object will contain methods and properties.

You can think of methods as functions that can be applied to output from the cmdlet, and you can think of properties as variables in the output from a cmdlet. To view these details, pass the output of a cmdlet to the Get-Member cmdlet:

Verb-Noun | Get-Member 

An example of running this to view the members for Get-Command is:

PS > Get-Command | Get-Member -MemberType Method"

From the above flag in the command, you can see that you can also select between methods and properties.

Creating Objects From Previous cmdlets
--------------------------------------
One way of manipulating objects is pulling out the properties from the output of a cmdlet and creating a new object. This is done using the Select-Object cmdlet. 

Here's an example of listing the directories and just selecting the mode and the name:
PS > Get-ChildItem | Select-Object -Property Mode, Name

You can also use the following flags to select particular information:

first - gets the first x object
last - gets the last x object
unique - shows the unique objects
skip - skips x objects

Filtering Objects
-----------------
When retrieving output objects, you may want to select objects that match a very specific value. You can do this using the Where-Object to filter based on the value of properties. 

The general format for using this cmdlet is 

Verb-Noun | Where-Object -Property PropertyName -operator Value

Verb-Noun | Where-Object {$_.PropertyName -operator Value}

The second version uses the $_ operator to iterate through every object passed to the Where-Object cmdlet.

Powershell is quite sensitive, so don't put quotes around the command!

Where -operator is a list of the following operators:

-Contains: if any item in the property value is an exact match for the specified value
-EQ: if the property value is the same as the specified value
-GT: if the property value is greater than the specified value
For a full list of operators, use this link: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.3

Here's an example of checking the stopped processes:
PS > Get-Service | Where-Object -Property Status -eq Stopped

Sort-Object
-----------

When a cmdlet outputs a lot of information, you may need to sort it to extract the information more efficiently. You do this by pipe-lining the output of a cmdlet to the Sort-Object cmdlet.

The format of the command would be:

Verb-Noun | Sort-Object

Here's an example of sorting the list of directories:
PS > Get-ChildItem | Sort-Object
--------------------------------------------------------
From: https://deskel.github.io/posts/thm/hacking-with-powershell

Search for the path to a particular file:
PS > Get-ChildItem -Path C:\ -Include *.txt -File -Recurse -ErrorAction SilentlyContinue
Meaning of the flags:
-Path: in this case we are instructing PowerShell to search the entire C drive
-Include: the name of the file being searched for; in this case it is just a wildcard and the file extension (*.txt), but it could be an exact file name
-File: only return files (not folders)
-Recurse: carry out a recursive search (meaning: search through the entire nested treee of folders and files within the specified path)
-ErrorAction SilentlyContinue: ignore any generated errors; do not clutter up the terminal with errors generated by, for example, folders that you are denied access to view the contents of

Read a file:
PS > Get-Content -Path '<full_path_to_file>'

Count all the cmdlets available on the system:
PS > Get-command | measure

Print current working directory
PS > Get-Location

Verify whether a particular file is on the system in a particular place:
PS > Get-Location "C:\Users\Administrator\Documents\Passwords"
- an error message indicates the file is not in the given path

Invoke a web request
see: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.3&viewFallbackFrom=powershell-6
example syntax:
PS > Invoke-WebRequest -URI https://<url>






