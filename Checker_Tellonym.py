import requests , random 
from colorama import Style,Fore

R = Fore.RED
G =Fore.GREEN
B = Fore.BLUE
Y =Fore.YELLOW
print(B+"""

   ____ _               _               _       _ _                             
  / ___| |__   ___  ___| | _____ _ __  | |_ ___| | | ___  _ __  _   _ _ __ ___  
 | |   | '_ \ / _ \/ __| |/ / _ \ '__| | __/ _ \ | |/ _ \| '_ \| | | | '_ ` _ \ 
 | |___| | | |  __/ (__|   <  __/ |    | ||  __/ | | (_) | | | | |_| | | | | | |
  \____|_| |_|\___|\___|_|\_\___|_|     \__\___|_|_|\___/|_| |_|\__, |_| |_| |_|
                                                                |___/           
                                    version 2
-----------------------------------------------------------------------------------
 By Fostn : Telegram Channel https://t.me/ifostn : Twitter @lwv5 : Instagram @f09l
-----------------------------------------------------------------------------------

""")

countt = int(input(" Enter The Count : "))
length = int(input(" Enter The Length : "))
save_file = input(Y+"Enter the name of the file to save it : ")
chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
a = 0
theheader = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://tellonym.me',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'tellonym-client': 'web:3.24.11',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
while a < countt:
    users = str("".join(random.choice(chars)for i in range(length)))
    url = (f'https://api.tellonym.me/profiles/name/{users}?limit=1')
    r = requests.get(url,headers=theheader)
    if r.status_code == 404:
        print(G+f" Available {users}")
        open(save_file+".txt","a").write(f"{users}\n")

        
    elif r.status_code == 200:
        print(R+f" Not Available {users} ")
        
    else:
        print("To match requests !! ")
        break
    a = a+1


print("\n"+Y+"{ Done With ["+str(countt)+"] Users }")
