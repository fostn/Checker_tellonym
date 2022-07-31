import requests,random,time
from colorama import Fore
R = Fore.RED
G =Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
c = Fore.LIGHTMAGENTA_EX
b = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
w = Fore.WHITE
y = Fore.LIGHTYELLOW_EX
g = Fore.LIGHTGREEN_EX
print(b+"""
   ___ _           _             _____        _ _   _           
  / __| |_  ___ __| |_____ _ _  |_   _|_ __ _(_) |_| |_ ___ _ _ 
 | (__| ' \/ -_) _| / / -_) '_|   | | \ V  V / |  _|  _/ -_) '_|
  \___|_||_\___\__|_\_\___|_|     |_|  \_/\_/|_|\__|\__\___|_|
  --------------------------------------------------------------
Checker Twitter By fostn : insta @f09l - Telegram Channel @ifostn  
""")

print(g+"[1] normal check with save file ")
print(r+"[2] Send users to telegram bot ")
choose = input(B+"please choose : ")
def normal():
    a = 0
    valid = 0
    unvalid = 0
    
    thecount = int(input(B+"Enter The Count : "))
    length = int(input(B+"Enter The Length : "))
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuio_pasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn_m12345678901234567890"
    headd = {
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'referer':'https://twitter.com/i/flow/signup',
        'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"macOS"',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token':'3a2c2e6c788c3815afb45b70dcc49c3fb4c2ec4f57cb002b7de46c1217abc1036ad236bf3637c03f1f4e4a2a9aeceeb643e4536a43d434e360b9331866a58457280b433d72db8cb930ffd2b00e4bf1b3',
        'x-guest-token':'1548901195728801793',
        'x-twitter-active-user':'yes',
        'x-twitter-client-language':'en',
    }

    while a < thecount:
        users = str("".join(random.choice(chars)for i in range(length)))
        time.sleep(0.5)
        url = (f"https://twitter.com/i/api/i/users/username_available.json?full_name=fostn&suggest=false&username={users}")
        r = requests.get(url,headers=headd)
        if '"reason":"taken"' in r.text:
            unvalid = unvalid+1
            print(R+f"unvalid : {users} ")
            
        elif '"reason":"available"' in r.text:
            print(G+f"valid : {users}")
            with open('twitter_hits.txt','a')as save:
                save.write(users+'\n')
            valid = valid+1
        else:
            print(Y+"Error ! ")
            break
        a = a+1
    print(G+f"success complete .")
    print(f"{G}valid [{valid}] {w}| {R}unvalid [{unvalid}]")
def send_to_bot():
    a = 0
    valid = 0
    unvalid = 0
    id = input("Enter Your id on telegram : ")
    token = input("Enter Your Token : ")
    thecount = int(input(B+"Enter The Count : "))
    length = int(input(B+"Enter The Length : "))
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuio_pasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn_m12345678901234567890"
    headd = {
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'referer':'https://twitter.com/i/flow/signup',
        'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"macOS"',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-csrf-token':'3a2c2e6c788c3815afb45b70dcc49c3fb4c2ec4f57cb002b7de46c1217abc1036ad236bf3637c03f1f4e4a2a9aeceeb643e4536a43d434e360b9331866a58457280b433d72db8cb930ffd2b00e4bf1b3',
        'x-guest-token':'1548901195728801793',
        'x-twitter-active-user':'yes',
        'x-twitter-client-language':'en',
    }

    while a < thecount:
        users = str("".join(random.choice(chars)for i in range(length)))
        time.sleep(0.5)
        url = (f"https://twitter.com/i/api/i/users/username_available.json?full_name=fostn&suggest=false&username={users}")
        r = requests.get(url,headers=headd)
        if '"reason":"taken"' in r.text:
            unvalid = unvalid+1
            print(R+f"unvalid : {users} ")
            
        elif '"reason":"available"' in r.text:
            print(G+f"valid : {users}")
            valid = valid+1
            bot =requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= Twitter Checker \nnew hit : {users}')
        else:
            print(Y+"Error ! ")
            break
        a = a+1
    print(G+f"success complete .")
    print(f"{G}valid [{valid}] {w}| {R}unvalid [{unvalid}]")
if choose == '1':
    normal()
elif choose == "2":
    send_to_bot()
else:
    print(R+"try again ")
