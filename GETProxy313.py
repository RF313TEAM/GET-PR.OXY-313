#YA MAHDI 313 TEAM
import requests
import os
import time
os.system("clear")
print('''


	YA MAHDI


''')
print("Waiting 5/s .........")
time.sleep(5)
os.system("clear")
print('''

	@ya-mahdi 313
	-------------------------
	@choose only(http or socks4 or socks5)


''')
m=input("Enter only server:")
print('''
	----------------------
	@choose country exam:US or FR or CA

''')
hack99=input("Enter  country proxy:")
agent=[
"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0"
,
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
,
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"

]
r=requests.get("https://www.proxy-list.download/api/v1/get?type="+m+"&country="+hack99)
print(r.text)
H=open("proxy.txt","a")
k=H.write(r.text)
print("Save in:"+os.getcwd()+"/proxy.txt")
	