# Brute Force Python
Generic brute force program for POST requests

I created this program because when using hydra, I received several false positives and when I used other python scripts, the program crashed because the wordlist was large.


<h2>How to use</h2>

Step 1: clone the repository: ```git clone https://github.com/Gutierre0x80/BruteForcePython.git```

Step 2: Execute the program using the exemle: ```python3 BruteForcer.py -url https://target/admin_login/check -u user -p pass -pU "User" -pP "Password" -e incorrect```

-url: The url of the target, Don´t forget to put the endpoint where password validation is done as in the example

-u and -p : User wordlist/Password wordlist, remember to create a word list.

-pU and -pP: User parameter and Password parameter. I recommend you look for this in the "network" tab of your browser's element inspector

-e: Error message. A unique phrase that appears only when the digital password is INCORRECT
