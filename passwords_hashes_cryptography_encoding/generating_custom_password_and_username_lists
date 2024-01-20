How to prep password lists for use by combining multiple lists and removing duplicates:
> cat list1.txt list2.txt list3.txt > aggregated_list.txt
> sort aggregated_list.txt | uniq -u > deduplicated_aggregated_list.txt
[hat tip: https://tryhackme.com/room/passwordattacks - Task 3]
------------------------------------------------------------------------------
It is worthwhile to create a custom list for a company. The cewl tool will crawl and scrape a company's website and pull strings that fit certain criteria and generate a wordlist for brute forcing based on those strings.
example syntax:
> cewl -w list.txt -d 5 -m 5 http://thm.labs
`-w` - output file
`-d` - minimum string length
`-m` - webcrawling/spidering depth level (2 is default)
`http://thm.labs` - url to search
----------------------------------------------------------------------------
Employ the tool `username_generator` to create a list of possible usernames to bruteforce. One supplies employee names and `username_generator` produces a list that combines them in many different ways.
example: John Smith, becomes:
johnsmith
smithjohn
jsmith
josmith
smithj
john_smith
smith_john
etc.
syntax:
> git clone https://github.com/therodri2/username_generator.git
> cd username_generator
> python3 username_generator.py -h [shows help message and arguments]
> echo "John Smith" > users.txt
> python3 username_generator.py -w users.txt
----------------------------------------------------------------------------
Crunch
------
Employ the tool `crunch` to generate all possible random combinations of designated letters/numbers/symbols in order to use them in a brute force attack:
syntax:
crunch -h 
help screen

crunch 2 2 01234abcd -o crunch.txt
generates "words" of minimum 2 characters and maximum 2 characters using all possible combinations of the following numbers/letters: 01234abcd Output is written to crunch.txt file.

crunch also lets us specify a character set using the -t option to combine words of our choice. Here are some of the other options that could be used to help create different combinations of your choice:

@ - lower case alpha characters

, - upper case alpha characters

% - numeric characters

^ - special characters including space
For example, if part of the password is known to us, and we know it starts with pass and is followed by two numbers, we can use the % symbol from above to match the numbers. Here we generate a wordlist that contains "pass" followed by 2 numbers:
crunch 6 6 -t pass%%
[From: https://tryhackme.com/room/passwordattacks ; Task 4 ; with editing, etc.]
---------------------------------------------------------------------------------------------------
CUPP - Common User Passwords Profiler
------------------
Python tool for creating custom wordlists to brute force from. The wordlists are created based on information you supply regarding the user. There is a 1337/leet mode option which will replace letters wiyh leetspeak numbers and characters.
The git repository is here: https://github.com/Mebus/cupp.
syntax:
> git clone https://github.com/Mebus/cupp.git
change to the CUPP directory and run:
> python3 cupp.py
[add -h for help page]
> python3 cupp.py -i
interactive mode where you fill in info about user; press enter to skip fields you do not know the answer to
> python3 cupp.py -l
see and choose from a list of custom wordlists that can be chosen; e.g. languages (japanese, yiddish, italian) or subjects (literature, music, movieTV)
> python3 cupp.py -a
pull a list of default usernames/passwords from the Alecto database
[From: https://tryhackme.com/room/passwordattacks ; Task 4 ; with editing, etc.]
-------------------------------------------------------------------------------------------------------


